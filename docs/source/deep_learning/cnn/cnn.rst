=============================
Convolutional neural network
=============================

In deep learning, a convolutional neural network (CNN, or ConvNet) is a class of deep neural networks, most commonly applied to analyzing visual imagery (Ref.: `Wikipedia <https://en.wikipedia.org/wiki/Convolutional_neural_network>`_).

.. figure:: ../img/cnn/cnn_structure.png
  :align: center
  :scale: 70%

Basically, we can use filter which get features to classfy cats.

Filter
======

We can extract specific features using a filter through convlutions. This is an example of using filters.

Example: Edge detection
***********************

---------------------------------
Convolutions on gray scale image
---------------------------------

...

---------------------------------
Convolutions on RGB image
---------------------------------

...


Padding and stride
===================

Padding
*******

**Problem:**

* **Throwing away information from edges of images**
* Shrinking outputs (Duplicate problem)

If using padding, we can get information from edges of images.

---------------------------
Valid and same convolutions
---------------------------

* Valid

    * No padding
    * Output size: :math:`n - f + 1`

* Same

    * Pad so that output size is the same as the input size
    * Output size: :math:`n + 2p - f + 1`
    * Padding size: :math:`n + 2p - f + 1 = n \rightarrow p = \frac{f-1}{2}`

* :math:`f` is usually odd because of calculating the padding size for Same.


Stride
******

**Problem:**

* Throwing away information from edges of images
* **Shrinking outputs (Duplicate problem)**

Stride is the number of steps to pop over for convolutions. The output size is :math:`\lfloor \frac{n+2p-f}{s} + 1 \rfloor \times \lfloor \frac{n+2p-f}{s} + 1 \rfloor.`


Convolutional neural network
============================

One layer of a CNN
*******************

Simple CNN example
******************

Polling layer
=============


Reference
=========

* https://www.coursera.org/learn/convolutional-neural-networks
