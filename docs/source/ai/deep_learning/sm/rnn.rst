========================
Recurrent neural network
========================

A recurrent neural network (RNN) is a class of artificial neural networks where connections between nodes form a directed graph along a temporal sequence (Ref.: `Wikipedia <https://en.wikipedia.org/wiki/Recurrent_neural_network>`_).

.. figure:: ../img/sm/rnn/rnn_structure.png
  :align: center
  :scale: 50%


RNN basic structure
====================

RNN은 Input layer과 이전 Hidden layer 정보를 활용하여 Output layer를 만들어내는 구조다.

.. figure:: ../img/sm/rnn/rnn_basic.png
  :align: center
  :scale: 50%


다음 예제를 통해 조금 더 자세히 살펴보자. 목적은 "hell"을 입력으로 넣었을 때, "o"가 출력되게 만드는 것이다.

.. figure:: ../img/sm/rnn/rnn_detail.png
  :align: center
  :scale: 50%

위 목적을 이루기 위해 RNN 모델의 Weight를 찾아가는 과정은 크게 Forward propagation과 Back propagation으로 나누어 설명할 수 있다.


Forward propagation
********************

첫 번째 Input layer인 :math:`x_1` 과 :math:`W_{x_1,h_1}` 를 이용해 첫 번째 Hidden layer인 :math:`h_1` 를 구할 수 있다. 그리고 :math:`h_1` 과 :math:`W_{h_1,y_1}` 으로 첫 번째 Output layer인 :math:`y_1` 을 구할 수 있다.

그리고 두 번째 Input layer인 :math:`x_2` 와 :math:`W_{x_2,h_2}` , 그리고 이전 Hidden layer인 :math:`h_1` 과 :math:`W_{h_1,h_2}` 를 이용해 두 번째 Hidden layer인 :math:`h_2` 를 구할 수 있다. 그리고 :math:`h_2` 와 :math:`W_{h_2,y_2}` 로 두 번째 Output layer인 :math:`y_1` 을 구할 수 있다.

이러한 과정을 마지막 Layer까지 진행하면 "o"에 해당하는 Output layer의 값을 구할 수 있다. 이 과정을 Forward propagation이라 하고 이렇게 계산된 Output layer의 값과 실제 정답과의 차이를 이용하여 모델의 Weight를 개선할 수 있다.


Back propagation
*****************


Reference
=========

* `Coursera <https://www.coursera.org/learn/nlp-sequence-models>`_
* `ratsgo's blog <https://ratsgo.github.io/natural%20language%20processing/2017/03/09/rnnlstm/>`_
