=============================
Convolutional Neural Network
=============================

위키피디아에서는 합성곱 신경망 (Convolutional Neural Network, CNN)을 아래와 같이 정의했다.

    In deep learning, a convolutional neural network (CNN, or ConvNet) is a class of deep neural networks, most commonly applied to analyzing visual imagery (출처: `Wikipedia <https://en.wikipedia.org/wiki/Convolutional_neural_network>`_).

즉, CNN은 이미지를 분석하는데 활용되는 Deep neural network라고 할 수 있다. 이러한 CNN을 이해하기 위해서는 합성곱 (Convolution)과 필터 (Filter)에 대한 이해가 필요하다.


Convolution과 필터
==================

Convolution과 필터에 대한 이해를 돕기 위해 먼저 아날로그 신호처리에 대해서 설명하려고 한다.

선형 시불변 시스템 (Linear Time Invariant System, LTI System)은 아날로그 신호의 잡음을 제거해주는 시스템이다. 이러한 잡음을 제거할 때 Convolution이 사용된다.

(이미지 작성 예정)

위 그림처럼 잡음 제거 필터를 신호가 지나가면서 Convolution을 통해 필터에 해당하는 값만 받아들이면 잡음을 제거할 수 있다.

동일한 작업을 이미지에서도 할 수 있다.


Reference
==========

* `Fast campus, 올인원 패키지: 딥러닝/인공지능 > 합성곱 신경망 (CNN) <https://www.fastcampus.co.kr/data_online_deep/>`_
