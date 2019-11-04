=============
chemical VAE
=============

Installation
=============

* Requirements:

    * Python >= 3.5
    * Keras >= 2.0.0 && 2.0.7 (pip install keras)
    * Tensorflow == 1.1 (pip install tensorflow-gpu)
    * RDKit
    * Pandas, Numpy
    * Matplotlib (pip install matplotlib)

* Installation

    ::

        pip install git+https://github.com/aspuru-guzik-group/chemical_vae.git


* Errors

    * 아래의 오류는 keras 2.0.7의 버그이므로 Keras의 버전을 변경해야 한다.

    ::

        pip install keras==2.0.6

    ::

        /usr/local/lib/python3.5/dist-packages/keras/backend/tensorflow_backend.py in variable(value, dtype, name, constraint)
            321     v._uses_learning_phase = False
            322     # TODO: move to `tf.get_variable` when supported in public release.
        --> 323     v.constraint = constraint
            324     return v


Property prediction
====================




Reference
==========

* `GitHub, chemical_vae <https://github.com/aspuru-guzik-group/chemical_vae>`_
