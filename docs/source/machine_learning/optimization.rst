============
Optimization
============

Optimization이라는 단어는 수학적으로 많이 사용되는 단어입니다. 수리 계획 또는 수리 계획 문제라고도 하고 물리학이나 컴퓨터에서의 최적화 문제는 생각하고 있는 함수를 모델로 한 시스템의 에너지를 나타낸 것으로 여김으로써 에너지 최소화 문제라고도 부르기도 합니다. 

딥러닝에서 Optimization 은 학습속도를 빠르고 안정적이게 하는 것이라고 말할 수 있습니다.

.. figure:: img/optimization/optimization_overview.png
  :align: center
  :scale: 45%

.. figure:: img/optimization/optimization_eq.png
  :align: center
  :scale: 20%


Types of optimizations
======================

* :doc:`Gradient descent <linear_regression/univariate_lr>`
* :doc:`Stochastic Gradient Descent (SGD) <large_scale_ml>`
* `Momentum <#momentum>`_
* `AdaGrad <#adamgrad>`_
* `RMSProp <#rmsprop>`_
* `Adam <#adam>`_

.. _momentum:

Momentum
========

모멘텀은 '운동량'을 의미한다. 기울기에서 속도의 개념이 추가된 것으로 고등학교 물리 시간을 떠올려보면 자세히는 아니지만 지상의 마찰력 때문에 물체의 이동속도가 점점 감소한다고 배웠던 기억이 어렴풋이 기억이 난다. 속도가 크게 나올수록 기울기가 크게 업데이트 되어 확률적 경사하강법이 가지는 단점을 보완할 수 있다.

Momentum은 마찰력/공기저항 같은 것에 해당하며 기울기 업데이트 시 이 폭을 조절하는 역할을 한다. 이에 따라 속도 velocity가 변화한다.


AdaGrad 
=======

신경망 학습에서의 학습률 Learning rate의 값은 일종의 보폭으로 생각할 수 있는데 한 번 갱신하는 가중치의 값을 양을 결정한다. 학습률을 너무 작게하면 보폭이 너무 작아서 많은 걸음을 걸어야 하므로 학습 시간을 아주 길게 해야 한다. 반대로 너무 크게 하면 최적의 점을 계속 지나치게 된다.

AdaGrad는 과거의 기울기 값을 제곱해서 계속 더하는 식으로 학습률을 낮추는데 학습이 진행될수록 제곱의 값으로 학습의 정도가 크게 떨어진다. 하지만 학습이 계속되면서 학습률이 0에 가까워져서 학습이 진행이 안되는 문제가 발생한다.


RMSPropab
=========

RMSProp은 이러한 문제를 보완하기 위해서 Exponential moving average를 사용한다. Exponential moving average는 과거의 정보에 가중치를 작게 부여하고 최근 값에 가장 민감하도록 가중치를 높게 부여하는 형태이다.


Adam
=====

잘 모르겠으면 일단 Adam을 사용하라는 말이 있다. 앞에서 언급했던 Momentum과 AdaGrad를 섞은 기법이라고 보면 된다.


Reference
==========

* https://gomguard.tistory.com/187
* https://sacko.tistory.com/42
* http://ruder.io/optimizing-gradient-descent/index.html
