===============
Preprocessing
===============

src/label.py
=============

Class: Label
*************

::

    import numpy as np
    from os.path import isfile

    class Label:

        def __init__(self,cl=-1,tl=np.array([0.,0.]),br=np.array([0.,0.]),prob=None):
            self.__tl 	= tl
            self.__br 	= br
            self.__cl 	= cl
            self.__prob = prob

        def __str__(self):
            return 'Class: %d, top_left(x:%f,y:%f), bottom_right(x:%f,y:%f)' % (self.__cl, self.__tl[0], self.__tl[1], self.__br[0], self.__br[1])

        def copy(self):
            return Label(self.__cl,self.__tl,self.__br)

        def wh(self): return self.__br-self.__tl

        def cc(self): return self.__tl + self.wh()/2

        def tl(self): return self.__tl
    
        def br(self): return self.__br

        def tr(self): return np.array([self.__br[0],self.__tl[1]])

        def bl(self): return np.array([self.__tl[0],self.__br[1]])

        def cl(self): return self.__cl

        def area(self): return np.prod(self.wh())

        def prob(self): return self.__prob

        def set_class(self,cl):
            self.__cl = cl

        def set_tl(self,tl):
            self.__tl = tl

        def set_br(self,br):
            self.__br = br

        def set_wh(self,wh):
            cc = self.cc()
            self.__tl = cc - .5*wh
            self.__br = cc + .5*wh

        def set_prob(self,prob):
            self.__prob = prob


    def lread(file_path,label_type=Label):

        if not isfile(file_path):
            return []

        objs = []
        with open(file_path,'r') as fd:
            for line in fd:
                v 		= line.strip().split()
                cl 		= int(v[0])
                ccx,ccy = float(v[1]),float(v[2])
                w,h 	= float(v[3]),float(v[4])
                prob 	= float(v[5]) if len(v) == 6 else None

                cc 	= np.array([ccx,ccy])
                wh 	= np.array([w,h])

                objs.append(label_type(cl,cc-wh/2,cc+wh/2,prob=prob))

        return objs

    def lwrite(file_path,labels,write_probs=True):
        with open(file_path,'w') as fd:
            for l in labels:
                cc,wh,cl,prob = (l.cc(),l.wh(),l.cl(),l.prob())
                if prob != None and write_probs:
                    fd.write('%d %f %f %f %f %f\n' % (cl,cc[0],cc[1],wh[0],wh[1],prob))
                else:
                    fd.write('%d %f %f %f %f\n' % (cl,cc[0],cc[1],wh[0],wh[1]))


    def dknet_label_conversion(R,img_width,img_height):
        WH = np.array([img_width,img_height],dtype=float)
        L  = []
        for r in R:
            center = np.array(r[2][:2])/WH
            wh2 = (np.array(r[2][2:])/WH)*.5
            L.append(Label(ord(r[0]),tl=center-wh2,br=center+wh2,prob=r[1]))
        return L

Class: Shape
*************

::

    class Shape():

        def __init__(self,pts=np.zeros((2,0)),max_sides=4,text=''):
            self.pts = pts
            self.max_sides = max_sides
            self.text = text

        def isValid(self):
            return self.pts.shape[1] > 2

        def write(self,fp):
            fp.write('%d,' % self.pts.shape[1])
            ptsarray = self.pts.flatten()
            fp.write(''.join([('%f,' % value) for value in ptsarray]))
            fp.write('%s,' % self.text)
            fp.write('\n')

        def read(self,line):
            data 		= line.strip().split(',')
            ss 			= int(data[0])
            values 		= data[1:(ss*2 + 1)]
            text 		= data[(ss*2 + 1)] if len(data) >= (ss*2 + 2) else ''
            self.pts 	= np.array([float(value) for value in values]).reshape((2,ss))
            self.text   = text

    def readShapes(path, obj_type=Shape):
        shapes = []
        with open(path) as fp:
            for line in fp:
                shape = obj_type()
                shape.read(line)
                shapes.append(shape)
        return shapes

    def writeShapes(path, shapes):
        if len(shapes):
            with open(path, 'w') as fp:
                for shape in shapes:
                    if shape.isValid():
                        shape.write(fp)

* Link: `train-detector.py <../create_and_train_wpod-net.html#train-detector-py>`_

src/sampler.py
===============

Import libraries
*****************

::

    import cv2
    import numpy as np
    import random

    from src.utils 	import im2single, getWH, hsv_transform, IOU_centre_and_dims
    from src.label	import Label
    from src.projection_utils import perspective_transform, find_T_matrix, getRectPts

Data augmentation
******************

::

    def pts2ptsh(pts):
        return np.matrix(np.concatenate((pts, np.ones((1, pts.shape[1]))), 0))

    def project(I, T, pts, dim):
        ptsh 	= np.matrix(np.concatenate((pts, np.ones((1, 4))), 0))
        ptsh 	= np.matmul(T, ptsh)
        ptsh 	= ptsh / ptsh[2]
        ptsret  = ptsh[:2]
        ptsret  = ptsret / dim
        Iroi = cv2.warpPerspective(I, T, (dim, dim), borderValue=.0, flags=cv2.INTER_LINEAR)
        return Iroi, ptsret

    def flip_image_and_pts(I, pts):
        """Flip an image
        
        Args:
            I:
            pts:

        Returns:
            I:
            pts:
        """
        I = cv2.flip(I, 1)
        pts[0] = 1. - pts[0]
        idx = [1, 0, 3, 2]
        pts = pts[..., idx]
        return I, pts

    def augment_sample(I, pts, dim):
        """Data augmentation

        Args:
            I:
            pts:
            dim:

        Returns:
            Iroi:
            llp:
            pts:

        """
        maxsum, maxangle = 120, np.array([80., 80., 45.])
        angles = np.random.rand(3) * maxangle
        if angles.sum() > maxsum:
            angles = (angles / angles.sum()) * (maxangle/maxangle.sum())

        I = im2single(I)
        iwh = getWH(I.shape)

        # Aspect-ratio: the LP aspect-ratio is randomly set in the interval [2, 4]
        #               to accommodate sizes from different regions
        whratio = random.uniform(2., 4.)
        wsiz = random.uniform(dim * .2, dim * 1.)
        hsiz = wsiz / whratio

        dx = random.uniform(0., dim - wsiz)
        dy = random.uniform(0., dim - hsiz)

        # Rectification: the entire image is rectified based on the LP annotation,
        #                assuming that the LP lies on a plane
        pph = getRectPts(dx, dy, dx+wsiz, dy+hsiz)
        pts = pts * iwh.reshape((2, 1))
        T = find_T_matrix(pts2ptsh(pts), pph)

        # Rotation: a 3D rotation with randomly chosen angles is performed,
        #           to account for a wide range of camera setups
        H = perspective_transform((dim, dim), angles=angles)
        H = np.matmul(H, T)

        Iroi, pts = project(I, H, pts, dim)
        
        # Colorspace: slight modifications in the HSV colorspace
        hsv_mod = np.random.rand(3).astype('float32')
        hsv_mod = (hsv_mod - .5)*.3
        hsv_mod[0] *= 360
        Iroi = hsv_transform(Iroi, hsv_mod)
        Iroi = np.clip(Iroi, 0., 1.)

        pts = np.array(pts)

        # Mirroring 50% chance
        if random.random() > .5:
            Iroi, pts = flip_image_and_pts(Iroi, pts)

        tl, br = pts.min(1), pts.max(1)
        llp = Label(0, tl, br)

        return Iroi, llp, pts

* Link: `im2single <utils.html#src-utils-py>`_, `process_data_item <../create_and_train_wpod-net.html#preprocessing>`_

Label ￫ Output vector
**********************

::

    def labels2output_map(label, lppts, dim, stride):

        side = ((float(dim) + 40.) / 2.) / stride # 7.75 when dim = 208 and stride = 16

        outsize = dim / stride
        Y  = np.zeros((outsize, outsize, 2 * 4 + 1), dtype='float32')
        MN = np.array([outsize, outsize])
        WH = np.array([dim, dim], dtype=float)

        tlx, tly = np.floor(np.maximum(label.tl(), 0.) * MN).astype(int).tolist()
        brx, bry = np.ceil (np.minimum(label.br(), 1.) * MN).astype(int).tolist()

        for x in range(tlx, brx):
            for y in range(tly, bry):

                mn = np.array([float(x) + .5, float(y) + .5])
                iou = IOU_centre_and_dims(mn / MN, label.wh(), label.cc(), label.wh())

                if iou > .5:

                    p_WH = lppts * WH.reshape((2, 1))
                    p_MN = p_WH / stride

                    p_MN_center_mn = p_MN - mn.reshape((2, 1))

                    p_side = p_MN_center_mn / side

                    Y[y, x, 0] = 1.
                    Y[y, x, 1:] = p_side.T.flatten()

        return Y

* Link: `process_data_item <../create_and_train_wpod-net.html#preprocessing>`_
