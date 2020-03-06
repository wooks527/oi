=========
Training
=========

data_generator.py
==================

::
    
    import numpy as np

    from threading import Semaphore, Thread
    from time import sleep
    from random import choice, randint
    from pdb import set_trace as pause

    class DataGenerator(object):

        def __init__(	self, data, process_data_item_func, xshape, yshape, \
                        data_item_selector	= choice, 	\
                        nthreads			= 2,		\
                        pool_size			= 1000,		\
                        min_nsamples		= 1,		\
                        dtype 				= 'single' ):

            assert pool_size >= min_nsamples, \
                'Min. samples must be equal or less than pool_size'
            assert min_nsamples > 0 and pool_size > 0, \
                'Min. samples and pool size must be positive non-zero numbers'

            self._data = data
            self._process_data_item = process_data_item_func
            self._data_item_selector = data_item_selector
            self._xshape = xshape
            self._yshape = yshape
            self._nthreads = nthreads
            self._pool_size = pool_size
            self._min_nsamples = min_nsamples
            self._dtype = dtype
            
            self._count = 0
            self._stop = False
            self._threads = []
            self._sem = Semaphore()

            self._X, self._Y = self._get_buffers(self._pool_size)


        def _get_buffers(self,N):
            X = np.empty((N,) + self._xshape, dtype=self._dtype)
            Y = np.empty((N,) + self._yshape, dtype=self._dtype)
            return X,Y

        def _compute_sample(self):
            d = self._data_item_selector(self._data)
            return self._process_data_item(d)

        def _insert_data(self,x,y):

            self._sem.acquire()

            if self._count < self._pool_size:
                self._X[self._count] = x
                self._Y[self._count] = y
                self._count += 1
            else:
                idx = randint(0,self._pool_size-1)
                self._X[idx] = x
                self._Y[idx] = y

            self._sem.release()

        def _run(self):
            while True:
                x,y = self._compute_sample()
                self._insert_data(x,y)
                if self._stop:
                    break

        def stop(self):
            self._stop = True
            for thread in self._threads:
                thread.join()

        def start(self):
            self._stop = False
            self._threads = [Thread(target=self._run) for n in range(self._nthreads)]
            for thread in self._threads:
                thread.setDaemon(True)
                thread.start()

        def get_batch(self,N):

            # Wait until the buffer was filled with the minimum
            # number of samples
            while self._count < self._min_nsamples:
                sleep(.1)

            X,Y = self._get_buffers(N)
            self._sem.acquire()
            for i in range(N):
                idx = randint(0,self._count-1)
                X[i] = self._X[idx]
                Y[i] = self._Y[idx]
            self._sem.release()
            return X,Y


loss.py
========

Import libraries
*****************

::

    import tensorflow as tf

Loss function
**************

::

    def loss(Ytrue, Ypred):
        """Loss function

        Args:
            Ytrue:
            Ypred:

        Returns:
            res:
        """
        b = tf.shape(Ytrue)[0]
        h = tf.shape(Ytrue)[1]
        w = tf.shape(Ytrue)[2]

        obj_probs_true = Ytrue[..., 0]
        obj_probs_pred = Ypred[..., 0]

        non_obj_probs_true = 1. - Ytrue[..., 0]
        non_obj_probs_pred = Ypred[..., 1]

        affine_pred	= Ypred[..., 2:]
        pts_true 	= Ytrue[..., 1:]

        affinex = tf.stack([tf.maximum(affine_pred[..., 0], 0.), affine_pred[..., 1], affine_pred[..., 2]], 3)
        affiney = tf.stack([affine_pred[..., 3], tf.maximum(affine_pred[..., 4], 0.), affine_pred[..., 5]], 3)

        v = 0.5
        base = tf.stack([[[[-v,-v,1., v,-v,1., v,v,1., -v,v,1.]]]])
        base = tf.tile(base,tf.stack([b, h, w, 1]))

        pts = tf.zeros((b, h, w, 0))

        for i in range(0, 12, 3):
            row = base[..., i:(i + 3)]
            ptsx = tf.reduce_sum(affinex * row, 3)
            ptsy = tf.reduce_sum(affiney * row, 3)

            pts_xy = tf.stack([ptsx, ptsy], 3)
            pts = (tf.concat([pts, pts_xy], 3))

        flags = tf.reshape(obj_probs_true, (b, h, w, 1))
        res   = 1. * l1(pts_true * flags, pts * flags, (b, h, w, 4 * 2))
        res  += 1. * logloss(obj_probs_true, obj_probs_pred, (b, h , w, 1))
        res  += 1. * logloss(non_obj_probs_true, non_obj_probs_pred, (b, h, w, 1))
        return res

* Link: `train-detector.py <../create_and_train_wpod-net.html#train-detector-py>`_

L1 function
************

::

    def l1(true, pred, szs):
        """L1 function
        
        Args:
            true:
            pred:
            szs:

        Returns:
            res
        """
        b,h,w,ch = szs
        res = tf.reshape(true-pred,(b,h*w*ch))
        res = tf.abs(res)
        res = tf.reduce_sum(res,1)
        return res

Log loss function
******************

::

    def logloss(Ptrue, Pred, szs, eps=10e-10):
        """Log loss function

        Args:
            Ptrue:
            Pred:
            szs:
            eps:

        Returns:
            Pred:
        """
        b, h, w, ch = szs
        Pred = tf.clip_by_value(Pred, eps, 1.)
        Pred = -tf.log(Pred)
        Pred = Pred * Ptrue
        Pred = tf.reshape(Pred, (b, h * w * ch))
        Pred = tf.reduce_sum(Pred, 1)
        return Pred
