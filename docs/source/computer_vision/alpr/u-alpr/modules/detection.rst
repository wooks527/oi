===================
학습된 모델로 테스트
===================

run.sh
=======

::

    #!/bin/bash

    check_file() 
    {
        if [ ! -f "$1" ]
        then
            return 0
        else
            return 1
        fi
    }

    check_dir() 
    {
        if [ ! -d "$1" ]
        then
            return 0
        else
            return 1
        fi
    }


    # Check if Darknet is compiled
    check_file "darknet/libdarknet.so"
    retval=$?
    if [ $retval -eq 0 ]
    then
        echo "Darknet is not compiled! Go to 'darknet' directory and 'make'!"
        exit 1
    fi

    lp_model="data/lp-detector/wpod-net_update1.h5"
    input_dir=''
    output_dir=''
    csv_file=''


    # Check # of arguments
    usage() {
        echo ""
        echo " Usage:"
        echo ""
        echo "   bash $0 -i input/dir -o output/dir -c csv_file.csv [-h] [-l path/to/model]:"
        echo ""
        echo "   -i   Input dir path (containing JPG or PNG images)"
        echo "   -o   Output dir path"
        echo "   -c   Output CSV file path"
        echo "   -l   Path to Keras LP detector model (default = $lp_model)"
        echo "   -h   Print this help information"
        echo ""
        exit 1
    }

    while getopts 'i:o:c:l:h' OPTION; do
        case $OPTION in
            i) input_dir=$OPTARG;;
            o) output_dir=$OPTARG;;
            c) csv_file=$OPTARG;;
            l) lp_model=$OPTARG;;
            h) usage;;
        esac
    done

    if [ -z "$input_dir"  ]; then echo "Input dir not set."; usage; exit 1; fi
    if [ -z "$output_dir" ]; then echo "Ouput dir not set."; usage; exit 1; fi
    if [ -z "$csv_file"   ]; then echo "CSV file not set." ; usage; exit 1; fi

    # Check if input dir exists
    check_dir $input_dir
    retval=$?
    if [ $retval -eq 0 ]
    then
        echo "Input directory ($input_dir) does not exist"
        exit 1
    fi

    # Check if output dir exists, if not, create it
    check_dir $output_dir
    retval=$?
    if [ $retval -eq 0 ]
    then
        mkdir -p $output_dir
    fi

    # End if any error occur
    set -e

    # Detect vehicles
    python vehicle-detection.py $input_dir $output_dir

    # Detect license plates
    python license-plate-detection.py $output_dir $lp_model

    # OCR
    python license-plate-ocr.py $output_dir

    # Draw output and generate list
    python gen-outputs.py $input_dir $output_dir > $csv_file

    # Clean files and draw output
    rm $output_dir/*_lp.png
    rm $output_dir/*car.png
    rm $output_dir/*_cars.txt
    rm $output_dir/*_lp.txt
    rm $output_dir/*_str.txt

vehicle-detection.py
====================

Import libraries
*****************

::

    import sys
    import cv2
    import numpy as np
    import traceback

    import darknet.python.darknet as dn

    from src.label 				import Label, lwrite
    from os.path 				import splitext, basename, isdir
    from os 					import makedirs
    from src.utils 				import crop_region, image_files_from_folder
    from darknet.python.darknet import detect

Vehicle detection
******************

::

    if __name__ == '__main__':

        try:
        
            input_dir  = sys.argv[1]
            output_dir = sys.argv[2]

            vehicle_threshold = .5

            vehicle_weights = 'data/vehicle-detector/yolo-voc.weights'
            vehicle_netcfg  = 'data/vehicle-detector/yolo-voc.cfg'
            vehicle_dataset = 'data/vehicle-detector/voc.data'

            vehicle_net  = dn.load_net(vehicle_netcfg, vehicle_weights, 0)
            vehicle_meta = dn.load_meta(vehicle_dataset)

            imgs_paths = image_files_from_folder(input_dir)
            imgs_paths.sort()

            if not isdir(output_dir):
                makedirs(output_dir)

            print 'Searching for vehicles using YOLO...'

            for i,img_path in enumerate(imgs_paths):

                print '\tScanning %s' % img_path

                bname = basename(splitext(img_path)[0])

                R,_ = detect(vehicle_net, vehicle_meta, img_path ,thresh=vehicle_threshold)

                R = [r for r in R if r[0] in ['car','bus']]

                print '\t\t%d cars found' % len(R)

                if len(R):

                    Iorig = cv2.imread(img_path)
                    WH = np.array(Iorig.shape[1::-1],dtype=float)
                    Lcars = []

                    for i,r in enumerate(R):

                        cx,cy,w,h = (np.array(r[2])/np.concatenate( (WH,WH) )).tolist()
                        tl = np.array([cx - w/2., cy - h/2.])
                        br = np.array([cx + w/2., cy + h/2.])
                        label = Label(0,tl,br)
                        Icar = crop_region(Iorig,label)

                        Lcars.append(label)

                        cv2.imwrite('%s/%s_%dcar.png' % (output_dir,bname,i),Icar)

                    lwrite('%s/%s_cars.txt' % (output_dir,bname),Lcars)

        except:
            traceback.print_exc()
            sys.exit(1)

        sys.exit(0)
        

license-plate-detection.py
===========================

Import libraries
*****************

::

    import sys, os
    import keras
    import cv2
    import traceback

    from src.keras_utils        import load_model
    from glob                   import glob
    from os.path                import splitext, basename
    from src.utils              import im2single
    from src.keras_utils        import load_model, detect_lp
    from src.label              import Shape, writeShapes

LP detection
*************

::

    def adjust_pts(pts,lroi):
        return pts * lroi.wh().reshape((2, 1)) + lroi.tl().reshape((2, 1))


    if __name__ == '__main__':

        try:
            
            input_dir  = sys.argv[1]
            output_dir = input_dir

            lp_threshold = .5

            # Load WPOD-Net model
            wpod_net_path = sys.argv[2]
            wpod_net = load_model(wpod_net_path)

            # Get image paths
            imgs_paths = glob('%s/*car.png' % input_dir)

            print 'Searching for license plates using WPOD-NET'

            for i, img_path in enumerate(imgs_paths):
                print '\t Processing %s' % img_path

                # Load an image
                bname = splitext(basename(img_path))[0]
                Ivehicle = cv2.imread(img_path)

                # Set resizing parameters for the image
                ratio = float(max(Ivehicle.shape[:2])) / min(Ivehicle.shape[:2])
                side  = int(ratio * 288.)
                bound_dim = min(side + (side % (2**4)), 608)
                print "\t\tBound dim: %d, ratio: %f" % (bound_dim, ratio)

                # LP detection + Rectification
                Llp, LlpImgs, _ = detect_lp(wpod_net, im2single(Ivehicle), bound_dim, 2**4, (240, 80), lp_threshold)

                # Save LP
                if len(LlpImgs):
                    Ilp = LlpImgs[0]
                    Ilp = cv2.cvtColor(Ilp, cv2.COLOR_BGR2GRAY)
                    Ilp = cv2.cvtColor(Ilp, cv2.COLOR_GRAY2BGR)

                    s = Shape(Llp[0].pts)

                    cv2.imwrite('%s/%s_lp.png' % (output_dir, bname), Ilp * 255.)
                    writeShapes('%s/%s_lp.txt' % (output_dir, bname), [s])

        except:
            traceback.print_exc()
            sys.exit(1)

        sys.exit(0)

* Link: `detect_lp <src/utils.html#lp-detection>`_


license-plate-ocr.py
=====================

::

    import sys
    import cv2
    import numpy as np
    import traceback

    import darknet.python.darknet as dn

    from os.path 				import splitext, basename
    from glob					import glob
    from darknet.python.darknet import detect
    from src.label				import dknet_label_conversion
    from src.utils 				import nms


    if __name__ == '__main__':

        try:
        
            input_dir  = sys.argv[1]
            output_dir = input_dir

            ocr_threshold = .4

            ocr_weights = 'data/ocr/ocr-net.weights'
            ocr_netcfg  = 'data/ocr/ocr-net.cfg'
            ocr_dataset = 'data/ocr/ocr-net.data'

            ocr_net  = dn.load_net(ocr_netcfg, ocr_weights, 0)
            ocr_meta = dn.load_meta(ocr_dataset)

            imgs_paths = sorted(glob('%s/*lp.png' % output_dir))

            print 'Performing OCR...'

            for i,img_path in enumerate(imgs_paths):

                print '\tScanning %s' % img_path

                bname = basename(splitext(img_path)[0])

                R,(width,height) = detect(ocr_net, ocr_meta, img_path ,thresh=ocr_threshold, nms=None)

                if len(R):

                    L = dknet_label_conversion(R,width,height)
                    L = nms(L,.45)

                    L.sort(key=lambda x: x.tl()[0])
                    lp_str = ''.join([chr(l.cl()) for l in L])

                    with open('%s/%s_str.txt' % (output_dir,bname),'w') as f:
                        f.write(lp_str + '\n')

                    print '\t\tLP: %s' % lp_str

                else:

                    print 'No characters found'

        except:
            traceback.print_exc()
            sys.exit(1)

        sys.exit(0)


gen-ouputs.py
==============

::

    import sys
    import cv2
    import numpy as np

    from glob						import glob
    from os.path 					import splitext, basename, isfile
    from src.utils 					import crop_region, image_files_from_folder
    from src.drawing_utils			import draw_label, draw_losangle, write2img
    from src.label 					import lread, Label, readShapes

    from pdb import set_trace as pause


    YELLOW = (  0,255,255)
    RED    = (  0,  0,255)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    img_files = image_files_from_folder(input_dir)

    for img_file in img_files:

        bname = splitext(basename(img_file))[0]

        I = cv2.imread(img_file)

        detected_cars_labels = '%s/%s_cars.txt' % (output_dir,bname)

        Lcar = lread(detected_cars_labels)

        sys.stdout.write('%s' % bname)

        if Lcar:

            for i,lcar in enumerate(Lcar):

                draw_label(I,lcar,color=YELLOW,thickness=3)

                lp_label 		= '%s/%s_%dcar_lp.txt'		% (output_dir,bname,i)
                lp_label_str 	= '%s/%s_%dcar_lp_str.txt'	% (output_dir,bname,i)

                if isfile(lp_label):

                    Llp_shapes = readShapes(lp_label)
                    pts = Llp_shapes[0].pts*lcar.wh().reshape(2,1) + lcar.tl().reshape(2,1)
                    ptspx = pts*np.array(I.shape[1::-1],dtype=float).reshape(2,1)
                    draw_losangle(I,ptspx,RED,3)

                    if isfile(lp_label_str):
                        with open(lp_label_str,'r') as f:
                            lp_str = f.read().strip()
                        llp = Label(0,tl=pts.min(1),br=pts.max(1))
                        write2img(I,llp,lp_str)

                        sys.stdout.write(',%s' % lp_str)

        cv2.imwrite('%s/%s_output.png' % (output_dir,bname),I)
        sys.stdout.write('\n')