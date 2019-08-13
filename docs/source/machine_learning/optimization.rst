============
Optimization
============

Optimization이라는 단어는 수학적으로 많이 사용되는 단어입니다. 수리 계획 또는 수리 계획 문제라고도 하고 물리학이나 컴퓨터에서의 최적화 문제는 생각하고 있는 함수를 모델로 한 시스템의 에너지를 나타낸 것으로 여김으로써 에너지 최소화 문제라고도 부르기도 합니다. 

딥러닝에서 Optimization 은 학습속도를 빠르고 안정적이게 하는 것이라고 말할 수 있습니다.

.. figure:: img/optimization/optimization_overview.png
  :align: center
  :scale: 40%

.. figure:: img/optimization/optimization_eq.png
  :align: center
  :scale: 20%


Types of optimizations
======================

* :doc:`Gradient descent <linear_regression/univariate_lr>`
* :doc:`Stochastic Gradient Descent (SGD) <large_scale_ml>`
* `Momentum`_
* `AdaGrad`_
* `RMSProp`_
* `Adam`_


Momentum
========

Momentum 방식은 말 그대로 Gradient Descent를 통해 이동하는 과정에 일종의 ‘관성’을 주는 것이다. 현재 Gradient를 통해 이동하는 방향과는 별개로, 과거에 이동했던 방식을 기억하면서 그 방향으로 일정 정도를 추가적으로 이동하는 방식이다.

.. rst-class:: centered

    :math:`v_t = \gamma v_{t-1} + \eta \nabla_{\theta}J(\theta)`


AdaGrad 
=======

AdaGrad(Adaptive Gradient)는 변수들을 Update할 때 각각의 변수마다 Step size를 다르게 설정해서 이동하는 방식이다. 이 알고리즘의 기본적인 아이디어는

.. rst-class:: centered

    *‘지금까지 많이 변화하지 않은 변수들은 Step size를 크게 하고, 지금까지 많이 변화했던 변수들은 Step size를 작게 하자’*

라는 것이다. 자주 등장하거나 변화를 많이 한 변수들의 경우 optimum에 가까이 있을 확률이 높기 때문에 작은 크기로 이동하면서 세밀한 값을 조정하고, 적게 변화한 변수들은 optimum 값에 도달하기 위해서는 많이 이동해야할 확률이 높기 때문에 먼저 빠르게 loss 값을 줄이는 방향으로 이동하려는 방식이라고 생각할 수 있겠다.

.. rst-class:: centered

    :math:`G_{t} = G_{t-1} + (\nabla_{\theta}J(\theta_t))^2`

    :math:`\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{G_t + \epsilon}} \cdot \nabla_{\theta}J(\theta_t)`


RMSProp
=======

RMSProp은 딥러닝의 대가 제프리 힌톤이 제안한 방법으로서, AdaGrad의 단점을 해결하기 위한 방법이다. AdaGrad의 식에서 Gradient의 제곱값을 더해나가면서 구한 :math:`G_t` 부분을 합이 아니라 지수평균으로 바꾸어서 대체한 방법이다. 이렇게 대체를 할 경우 AdaGrad처럼 :math:`G_t`가 무한정 커지지는 않으면서 최근 변화량의 변수간 상대적인 크기 차이는 유지할 수 있다.


.. rst-class:: centered

    :math:`G = \gamma G + (1-\gamma)(\nabla_{\theta}J(\theta_t))^2`

    :math:`\theta = \theta - \frac{\eta}{\sqrt{G + \epsilon}} \cdot \nabla_{\theta}J(\theta_t)`


Adam
=====

Adam (Adaptive Moment Estimation)은 RMSProp과 Momentum 방식을 합친 것 같은 알고리즘이다. 이 방식에서는 Momentum 방식과 유사하게 지금까지 계산해온 기울기의 지수평균을 저장하며, RMSProp과 유사하게 기울기의 제곱값의 지수평균을 저장한다.

.. rst-class:: centered

    :math:`m_t = \beta_1 m_{t-1} + (1-\beta_1)\nabla_\theta J(\theta)`

    :math:`v_t = \beta_2 v_{t-1} + (1-\beta_2)(\nabla_\theta J(\theta))^2`


Reference
==========

* https://gomguard.tistory.com/187
* http://ruder.io/optimizing-gradient-descent/index.html
* `BEOMSU KIM's BLOG <http://shuuki4.github.io/deep%20learning/2016/05/20/Gradient-Descent-Algorithm-Overview.html>`_
