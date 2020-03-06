=================
Troubleshooting
=================

* Vehicle detection 모델을 YOLO v3로 바꾼 후 발생하는 문제

    * bash run.sh -i samples/test -o results/yolov3 -c results/yolov3/results.csv

        * OSError: libdarknet.so: cannot open shared object file: No such file or directory

            * darknet/python/darknet.py 파일 내부에 libdarknet.so 위치 변경
            * lib = CDLL("libdarknet.so", RTLD_GLOBAL) → lib = CDLL("darknet/libdarknet.so", RTLD_GLOBAL)

        * ValueError: need more than 0 values to unpack

            * 에러 내용

            ::

                Traceback (most recent call last):
                File "vehicle-detection.py", line 45, in <module>
                    R,_ = detect(vehicle_net, vehicle_meta, img_path ,thresh=vehicle_threshold)
                ValueError: need more than 0 values to unpack

            * darknet/python/darknet.py 파일의 detect 함수에서 wh 값을 추가하고 반환함

                * Before

                ::

                    def detect(net, meta, image, thresh=.5, hier_thresh=.5, nms=.45):
                        im = load_image(image, 0, 0)
                        num = c_int(0)
                        pnum = pointer(num)
                        predict_image(net, im)
                        dets = get_network_boxes(net, im.w, im.h, thresh, hier_thresh, None, 0, pnum)
                        num = pnum[0]
                        if (nms): do_nms_obj(dets, num, meta.classes, nms);

                        res = []
                        for j in range(num):
                            for i in range(meta.classes):
                                if dets[j].prob[i] > 0:
                                    b = dets[j].bbox
                                    res.append((meta.names[i], dets[j].prob[i], (b.x, b.y, b.w, b.h)))
                        res = sorted(res, key=lambda x: -x[1])
                        free_image(im)
                        free_detections(dets, num)
                        return res

                * After

                ::

                    def detect(net, meta, image, thresh=.5, hier_thresh=.5, nms=.45):
                        im = load_image(image, 0, 0)
                        num = c_int(0)
                        pnum = pointer(num)
                        predict_image(net, im)
                        dets = get_network_boxes(net, im.w, im.h, thresh, hier_thresh, None, 0, pnum)
                        num = pnum[0]
                        if (nms): do_nms_obj(dets, num, meta.classes, nms);

                        res = []
                        for j in range(num):
                            for i in range(meta.classes):
                                if dets[j].prob[i] > 0:
                                    b = dets[j].bbox
                                    res.append((meta.names[i], dets[j].prob[i], (b.x, b.y, b.w, b.h)))
                        res = sorted(res, key=lambda x: -x[1])
                        wh = (im.w,im.h)
                        free_image(im)
                        free_detections(dets, num)
                        return res, wh
        
        * CUDA Error: out of memory (`Link <https://github.com/pjreddie/darknet/issues/791>`_)

            * 에러 내용

            ::

                CUDA Error: out of memory
                python: ./src/cuda.c:36: check_error: Assertion `0' failed.

            * yolov3.cfg의 내용 변경

                * Before

                ::

                    batch=1
                    subdivisions=1
                    width=416
                    height=416

                * After

                ::

                    batch=64
                    subdivisions=16
                    width=608
                    height=608


