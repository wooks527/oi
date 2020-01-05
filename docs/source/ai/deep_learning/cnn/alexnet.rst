========
AlexNet
========

AlexNet은 Krizhevsky의 논문 "ImageNet classification with deep convolution neural network"에서 제안한 모델이다. 여기서 ImageNet ILVRC-2010 120만 개의 이미지를 1000개의 Class로 분류하는데 CNN을 사용했고 압도적인 성과를 얻었다. 또한, GPU 사용과 소스 코드 공개로 다른 연구자들에게 많은 영향을 끼쳤다. 지금부터 하나씩 살펴보자.


Architecture
=============

AlexNet의 기본 구조는 아래와 같다.

.. figure:: ../img/cnn/alexnet/alexnet_architecture.png
    :align: center
    :scale: 80%

.. rst-class:: centered

    출처: `라온피플 (Laon People) <https://laonple.blog.me/220654387455>`_

Krizhevsky는 224x224x3 크기 이미지에 대해 5단계의 Convolution and subsampling을 적용시켰다.

224x224x3 이미지 → **1단계 [11x11 Filter, Stride 4]** → 55x55 Feature map 96개 → **2단계 [Normalization and 5x5 max-pooling]** → 27x27 Feature map 256개 → **3단계 [3x3 Filter]** → 13x13 Feature map 384개 → **4단계 [3x3 Filter]** → 13x13 Feature map 384개 → **5단계 [3x3 Filter]** → 13x13 Feature map 256개

5단계 이후의 과정은 LeNet과 유사하다.


LeNet vs. AlexNet
==================

AlexNet의 구조는 위/아래로 구분되어 있는데 이는 GPU를 적용하기 위함이다. 그리고 이 논문에서 Stride라는 개념을 적용했고, 기존과 다르게 Subsampling 없이 Convolution을 하기도 한다. 또한, Convolution도 기존과 다르게 5단계로 이루어져 있다.


Reference
==========

* 라온피플, Machine learning academy, Part IV. CNN

    * `4. Convolutional layer [1] <https://laonple.blog.me/220623406512>`_

* 라온피플, Machine learning academy, Part V. Best CNN Architecture

    * `3. AlexNet [1] <https://laonple.blog.me/220654387455>`_
