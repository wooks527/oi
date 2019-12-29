=============================
Convolutional neural network
=============================

In deep learning, a convolutional neural network (CNN, or ConvNet) is a class of deep neural networks, most commonly applied to analyzing visual imagery (Ref.: `Wikipedia <https://en.wikipedia.org/wiki/Convolutional_neural_network>`_).

.. figure:: ../img/cnn/cnn_structure.png
    :align: center
    :scale: 70%

.. rst-class:: centered

    출처: `Wikimedia <https://commons.wikimedia.org/wiki/File:Typical_cnn.png>`_


History
========

CNN은 1989년 LeCun이 발표한 "Backpropagation applied to handwritten zip code recognition" 논문에서 처음 제안한 모델로, 필기체 인식 프로젝트에서 개발되었다고 한다.

그리고 나서, 뭔가 추가적인 역사가 더 있다.

그렇다면 왜 CNN과 같은 방법이 필요했을까? 그 이유는 다음과 같다.


Why CNN?
=========

Multi-layered neural network의 문제점
************************************

예를 들어, 기존 Multi-layered neural network로 이미지의 글자를 인식한다고 해보자.

* 계산해야 할 파라미터 수가 너무 많음
* 이미지의 작은 변형에도 새로운 학습 데이터가 없으면 성능 X

그 원인은 Topological한 정보를 고려하지 않기 때문이다.




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

* `Coursera, Convolutional neural network <https://www.coursera.org/learn/convolutional-neural-networks>`_
* `라온피플(주) <https://laonple.blog.me/220587920012>`_
