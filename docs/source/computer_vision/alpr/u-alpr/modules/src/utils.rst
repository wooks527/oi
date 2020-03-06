========
Utility
========

src/utils.py
=============

Import libraries
*****************

::

    import numpy as np
    import cv2
    import sys

    from glob import glob

Functions
**********

::

    def im2single(I):
        assert(I.dtype == 'uint8')
        return I.astype('float32') / 255.


    def getWH(shape):
        return np.array(shape[1::-1]).astype(float)


    def IOU(tl1,br1,tl2,br2):
        wh1,wh2 = br1-tl1,br2-tl2
        assert((wh1>=.0).all() and (wh2>=.0).all())
        
        intersection_wh = np.maximum(np.minimum(br1,br2) - np.maximum(tl1,tl2),0.)
        intersection_area = np.prod(intersection_wh)
        area1,area2 = (np.prod(wh1),np.prod(wh2))
        union_area = area1 + area2 - intersection_area;
        return intersection_area/union_area


    def IOU_labels(l1,l2):
        return IOU(l1.tl(),l1.br(),l2.tl(),l2.br())


    def IOU_centre_and_dims(cc1,wh1,cc2,wh2):
        return IOU(cc1-wh1/2.,cc1+wh1/2.,cc2-wh2/2.,cc2+wh2/2.)


    def nms(Labels,iou_threshold=.5):

        SelectedLabels = []
        Labels.sort(key=lambda l: l.prob(),reverse=True)
        
        for label in Labels:

            non_overlap = True
            for sel_label in SelectedLabels:
                if IOU_labels(label,sel_label) > iou_threshold:
                    non_overlap = False
                    break

            if non_overlap:
                SelectedLabels.append(label)

        return SelectedLabels


    def image_files_from_folder(folder,upper=True):
        extensions = ['jpg','jpeg','png']
        img_files  = []
        for ext in extensions:
            img_files += glob('%s/*.%s' % (folder,ext))
            if upper:
                img_files += glob('%s/*.%s' % (folder,ext.upper()))
        return img_files


    def is_inside(ltest,lref):
        return (ltest.tl() >= lref.tl()).all() and (ltest.br() <= lref.br()).all()


    def crop_region(I,label,bg=0.5):

        wh = np.array(I.shape[1::-1])

        ch = I.shape[2] if len(I.shape) == 3 else 1
        tl = np.floor(label.tl()*wh).astype(int)
        br = np.ceil (label.br()*wh).astype(int)
        outwh = br-tl

        if np.prod(outwh) == 0.:
            return None

        outsize = (outwh[1],outwh[0],ch) if ch > 1 else (outwh[1],outwh[0])
        if (np.array(outsize) < 0).any():
            pause()
        Iout  = np.zeros(outsize,dtype=I.dtype) + bg

        offset 	= np.minimum(tl,0)*(-1)
        tl 		= np.maximum(tl,0)
        br 		= np.minimum(br,wh)
        wh 		= br - tl

        Iout[offset[1]:(offset[1] + wh[1]),offset[0]:(offset[0] + wh[0])] = I[tl[1]:br[1],tl[0]:br[0]]

        return Iout

    def hsv_transform(I,hsv_modifier):
        I = cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
        I = I + hsv_modifier
        return cv2.cvtColor(I,cv2.COLOR_HSV2BGR)

    def IOU(tl1,br1,tl2,br2):
        wh1,wh2 = br1-tl1,br2-tl2
        assert((wh1>=.0).all() and (wh2>=.0).all())
        
        intersection_wh = np.maximum(np.minimum(br1,br2) - np.maximum(tl1,tl2),0.)
        intersection_area = np.prod(intersection_wh)
        area1,area2 = (np.prod(wh1),np.prod(wh2))
        union_area = area1 + area2 - intersection_area;
        return intersection_area/union_area

    def IOU_centre_and_dims(cc1,wh1,cc2,wh2):
        return IOU(cc1-wh1/2.,cc1+wh1/2.,cc2-wh2/2.,cc2+wh2/2.)


    def show(I,wname='Display'):
        cv2.imshow(wname, I)
        cv2.moveWindow(wname,0,0)
        key = cv2.waitKey(0) & 0xEFFFFF
        cv2.destroyWindow(wname)
        if key == 27:
            sys.exit()
        else:
            return key

* Link: `augment_sample <preprocessing.html#data-augmentation>`_


src/keras_utils.py
===================

Import libraries
*****************

::

    import numpy as np
    import cv2
    import time

    from os.path import splitext

    from src.label import Label
    from src.utils import getWH, nms
    from src.projection_utils import getRectPts, find_T_matrix

Load and save a model
**********************

::

    def save_model(model,path,verbose=0):
        path = splitext(path)[0]
        model_json = model.to_json()
        with open('%s.json' % path,'w') as json_file:
            json_file.write(model_json)
        model.save_weights('%s.h5' % path)
        if verbose: print 'Saved to %s' % path

    def load_model(path,custom_objects={},verbose=0):
        from keras.models import model_from_json

        path = splitext(path)[0]
        with open('%s.json' % path,'r') as json_file:
            model_json = json_file.read()
        model = model_from_json(model_json, custom_objects=custom_objects)
        model.load_weights('%s.h5' % path)
        if verbose: print 'Loaded from %s' % path
        return model

LP detection
**************
        
::

    def detect_lp(model, I, max_dim, net_step, out_size, threshold):
        """ LP detection

        Args:
            model:
            I:
            max_dim:
            net_step:
            out_size:
            threshold:

        Returns:
            L:
            TLps:
            elapsed:
        """
        # Resize the image
        min_dim_img = min(I.shape[:2])
        factor 		= float(max_dim) / min_dim_img

        w, h = (np.array(I.shape[1::-1], dtype=float) * factor).astype(int).tolist()
        w += (w % net_step != 0) * (net_step - w % net_step)
        h += (h % net_step != 0) * (net_step - h % net_step)
        Iresized = cv2.resize(I, (w, h))

        T = Iresized.copy()
        T = T.reshape((1, T.shape[0], T.shape[1], T.shape[2]))

        # LP detection
        start   = time.time()
        Yr      = model.predict(T)
        Yr      = np.squeeze(Yr)
        elapsed = time.time() - start

        # Rectification
        L, TLps = reconstruct(I, Iresized, Yr, out_size, threshold)

        return L, TLps, elapsed

* Link: `license-plate-detection.py <../detection.html#lp-detection>`_

Rectification
**************

::

    class DLabel (Label):
        """Label ?
        """

        def __init__(self, cl, pts, prob):
            self.pts = pts
            tl = np.amin(pts, 1)
            br = np.amax(pts, 1)
            Label.__init__(self, cl, tl, br, prob)

    def reconstruct(Iorig, I, Y, out_size, threshold=.9):
        """Reconstruct ?

        Returns:
            final_labels:
            TLps:
        """

        net_stride 	= 2 ** 4
        side 		= ((208. + 40.) /2.) / net_stride # 7.75

        Probs = Y[..., 0]
        Affines = Y[..., 2:]
        rx,ry = Y.shape[:2]
        ywh = Y.shape[1::-1]
        iwh = np.array(I.shape[1::-1], dtype=float).reshape((2, 1))

        xx, yy = np.where(Probs > threshold)

        WH = getWH(I.shape)
        MN = WH / net_stride

        vxx = vyy = 0.5 #alpha

        base = lambda vx, vy: np.matrix([[-vx, -vy, 1.], [vx, -vy, 1.], [vx, vy, 1.], [-vx, vy, 1.]]).T
        labels = []

        for i in range(len(xx)):
            y, x = xx[i], yy[i]
            affine = Affines[y, x]
            prob = Probs[y, x]

            mn = np.array([float(x) + .5, float(y) + .5])

            A = np.reshape(affine, (2, 3))
            A[0, 0] = max(A[0, 0], 0.)
            A[1, 1] = max(A[1, 1], 0.)

            pts = np.array(A * base(vxx, vyy)) #*alpha
            pts_MN_center_mn = pts * side
            pts_MN = pts_MN_center_mn + mn.reshape((2, 1))

            pts_prop = pts_MN / MN.reshape((2, 1))

            labels.append(DLabel(0, pts_prop, prob))

        final_labels = nms(labels, .1)
        TLps = []

        # Rectification
        if len(final_labels):
            final_labels.sort(key=lambda x: x.prob(), reverse=True)
            for i, label in enumerate(final_labels):
                t_ptsh  = getRectPts(0, 0, out_size[0], out_size[1])
                ptsh    = np.concatenate((label.pts * getWH(Iorig.shape).reshape((2, 1)),np.ones((1, 4))))
                H       = find_T_matrix(ptsh, t_ptsh)
                Ilp     = cv2.warpPerspective(Iorig, H, out_size, borderValue=.0)

                TLps.append(Ilp)

        return final_labels, TLps
