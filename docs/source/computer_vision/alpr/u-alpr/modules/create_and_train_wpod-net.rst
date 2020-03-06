==========================
WPOD-Net 모델 생성 후 학습
==========================

create-model.py
================

WPOD-Net 모델을 생성하는 부분이다.

Import libraries
*****************

::

    import sys
    import keras

    from keras.layers import Conv2D, MaxPooling2D, BatchNormalization, Add, Activation, Concatenate, Input
    from keras.models import Model
    from keras.applications.mobilenet import MobileNet

    from src.keras_utils import save_model

Main codes
***********

::

    if __name__ == '__main__':

        modules = [func.replace('create_model_','') for func in dir(sys.modules[__name__]) if 'create_model_' in func]

        assert sys.argv[1] in modules, \
            'Model name must be on of the following: %s' % ', '.join(modules)

        modelf = getattr(sys.modules[__name__],'create_model_' + sys.argv[1])
        
        print 'Creating model %s' % sys.argv[1]
        model = modelf()
        print 'Finished'

        print 'Saving at %s' % sys.argv[2]
        save_model(model,sys.argv[2])

Create model
*************

-----------
eccv model
-----------

::

    def res_block(x,sz,filter_sz=3,in_conv_size=1):
        xi  = x
        for i in range(in_conv_size):
            xi  = Conv2D(sz, filter_sz, activation='linear', padding='same')(xi)
            xi  = BatchNormalization()(xi)
            xi 	= Activation('relu')(xi)
        xi  = Conv2D(sz, filter_sz, activation='linear', padding='same')(xi)
        xi  = BatchNormalization()(xi)
        xi 	= Add()([xi,x])
        xi 	= Activation('relu')(xi)
        return xi

    def conv_batch(_input,fsz,csz,activation='relu',padding='same',strides=(1,1)):
        output = Conv2D(fsz, csz, activation='linear', padding=padding, strides=strides)(_input)
        output = BatchNormalization()(output)
        output = Activation(activation)(output)
        return output

    def end_block(x):
        xprobs    = Conv2D(2, 3, activation='softmax', padding='same')(x)
        xbbox     = Conv2D(6, 3, activation='linear' , padding='same')(x)
        return Concatenate(3)([xprobs,xbbox])

    def create_model_eccv():
        
        input_layer = Input(shape=(None,None,3),name='input')

        x = conv_batch(input_layer, 16, 3)
        x = conv_batch(x, 16, 3)
        x = MaxPooling2D(pool_size=(2,2))(x)
        x = conv_batch(x, 32, 3)
        x = res_block(x, 32)
        x = MaxPooling2D(pool_size=(2,2))(x)
        x = conv_batch(x, 64, 3)
        x = res_block(x,64)
        x = res_block(x,64)
        x = MaxPooling2D(pool_size=(2,2))(x)
        x = conv_batch(x, 64, 3)
        x = res_block(x,64)
        x = res_block(x,64)
        x = MaxPooling2D(pool_size=(2,2))(x)
        x = conv_batch(x, 128, 3)
        x = res_block(x,128)
        x = res_block(x,128)
        x = res_block(x,128)
        x = res_block(x,128)

        x = end_block(x)

        return Model(inputs=input_layer,outputs=x)

-------
mobnet
-------

::

    # Model not converging...
    def create_model_mobnet():

        input_layer = Input(shape=(None,None,3),name='input')
        x = input_layer

        mbnet = MobileNet(input_shape=(224,224,3),include_top=True)
        
        backbone = keras.models.clone_model(mbnet)
        for i,bblayer in enumerate(backbone.layers[1:74]):
            layer = bblayer.__class__.from_config(bblayer.get_config())
            layer.name = 'backbone_' + layer.name
            x = layer(x)

        x = end_block(x)

        model = Model(inputs=input_layer,outputs=x)

        backbone_layers = {'backbone_' + layer.name: layer for layer in backbone.layers}
        for layer in model.layers:
            if layer.name in backbone_layers:
                print 'setting ' + layer.name
                layer.set_weights(backbone_layers[layer.name].get_weights())

        return model


train-detector.py
===================

Import libraries
*****************

::

    import sys
    import numpy as np
    import cv2
    import argparse
    import keras

    from random import choice
    from os.path import isfile, isdir, basename, splitext
    from os import makedirs

    from src.keras_utils import save_model, load_model
    from src.label import readShapes
    from src.loss import loss
    from src.utils import image_files_from_folder, show
    from src.sampler import augment_sample, labels2output_map
    from src.data_generator import DataGenerator

    from pdb import set_trace as pause

Main codes
***********

모델 불러오기 → 데이터 불러오기 → 데이터 전처리 → 모델 불러오기 → 모델 학습 후 저장 순으로 진행된다.

::

    if __name__ == '__main__':

        # Set args
        parser = argparse.ArgumentParser()
        parser.add_argument('-m' 	,'--model'		,type=str       ,required=True	    ,help='Path to previous model')
        parser.add_argument('-n' 	,'--name'		,type=str       ,required=True	    ,help='Model name')
        parser.add_argument('-tr'	,'--train-dir'		,type=str       ,required=True	    ,help='Input data directory for training')
        parser.add_argument('-its'	,'--iterations'		,type=int       ,default=300000	    ,help='Number of mini-batch iterations (default = 300.000)')
        parser.add_argument('-bs'	,'--batch-size'		,type=int       ,default=32	    ,help='Mini-batch size (default = 32)')
        parser.add_argument('-od'	,'--output-dir'		,type=str       ,default='./'       ,help='Output directory (default = ./)')
        parser.add_argument('-op'	,'--optimizer'		,type=str       ,default='Adam'	    ,help='Optmizer (default = Adam)')
        parser.add_argument('-lr'	,'--learning-rate'	,type=float     ,default=.01	    ,help='Optmizer (default = 0.01)')
        args = parser.parse_args()

        netname 	= basename(args.name)
        train_dir 	= args.train_dir
        outdir 		= args.output_dir

        iterations 	= args.iterations
        batch_size 	= args.batch_size
        dim 		= 208

        if not isdir(outdir):
            makedirs(outdir)

        # Load model and related information
        model, model_stride, xshape, yshape = load_network(args.model, dim)

        # Set train parameters
        opt = getattr(keras.optimizers, args.optimizer)(lr=args.learning_rate)
        model.compile(loss=loss, optimizer=opt)

        # Load images
        print 'Checking input directory...'
        Files = image_files_from_folder(train_dir)

        Data = []
        for file in Files:
            labfile = splitext(file)[0] + '.txt'
            if isfile(labfile):
                L = readShapes(labfile)
                I = cv2.imread(file)
                Data.append([I, L[0]])

        print '%d images with labels found' % len(Data)

        # Generate training dataset (parallel processing)
        dg = DataGenerator( data=Data, \
                            process_data_item_func=lambda x: process_data_item(x, dim, model_stride),\
                            xshape=xshape, \
                            yshape=(yshape[0], yshape[1], yshape[2] + 1), \
                            nthreads=2, \
                            pool_size=1000, \
                            min_nsamples=100 )
        dg.start()

        Xtrain = np.empty((batch_size, dim, dim, 3), dtype='single')
        Ytrain = np.empty((batch_size, dim / model_stride, dim / model_stride, 2 * 4 + 1))

        model_path_backup = '%s/%s_backup' % (outdir, netname)
        model_path_final  = '%s/%s_final'  % (outdir, netname)

        for it in range(iterations):

            print 'Iter. %d (of %d)' % (it + 1, iterations)

            Xtrain, Ytrain = dg.get_batch(batch_size)
            train_loss = model.train_on_batch(Xtrain, Ytrain)

            print '\tLoss: %f' % train_loss

            # Save model every 1000 iterations
            if (it+1) % 1000 == 0:
                print 'Saving model (%s)' % model_path_backup
                save_model(model, model_path_backup)

        print 'Stopping data generator'
        dg.stop()

        print 'Saving model (%s)' % model_path_final
        save_model(model, model_path_final)

* Link: `loss <src/training.html#loss-function>`_, `readShapes <src/preprocessing.html#class-shape>`_

Load model
***********

::

    def load_network(modelpath,input_dim):

        model = load_model(modelpath)
        input_shape = (input_dim,input_dim,3)

        # Fixed input size for training
        inputs  = keras.layers.Input(shape=(input_dim,input_dim,3))
        outputs = model(inputs)

        output_shape = tuple([s.value for s in outputs.shape[1:]])
        output_dim   = output_shape[1]
        model_stride = input_dim / output_dim

        assert input_dim % output_dim == 0, \
            'The output resolution must be divisible by the input resolution'

        assert model_stride == 2**4, \
            'Make sure your model generates a feature map with resolution ' \
            '16x smaller than the input'

        return model, model_stride, input_shape, output_shape

Preprocessing
**************

::

    def process_data_item(data_item, dim, model_stride):
        XX, llp, pts = augment_sample(data_item[0], data_item[1].pts, dim)
        YY = labels2output_map(llp, pts, dim, model_stride)
        return XX, YY

* Link: `augment_sample <src/preprocessing.html#data-augmentation>`_, `labels2output_map <src/preprocessing.html#label-output-vector>`_

