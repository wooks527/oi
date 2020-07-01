Gradient boosting machine (GBM)
================================

===========
Boosting
===========

기계학습에서 부스팅 (Boosting)이란 단순하고 약한 학습기 (Weak Learner)를 결합해서 보다 정확하고 강력한 학습기 (Strong Learner)를 만드는 방식을 의미한다.
정확도가 낮더라도 일단 모델을 만들고, 드러난 약점 (예측 오류)은 두 번째 모델이 보완한다.
이 둘을 합치면 처음보다는 정확한 모델이 만들어지고, 그럼에도 여전히 남아 있는 문제는 다음 모델에서 보완하여 계속 더하는 과정을 반복하는 원리다.


==================
Gradient Boosting
==================

손실함수 (Loss Function)는 예측 모델의 오류를 정량화해준다.
단순하게 말하면, 학습이란 손실함수를 최소화하는 파라미터를 찾는 일이라고도 할 수 있다.
최적의 파라미터를 찾는 방법 중 하나가 Gradient Descent다.
손실함수를 파라미터로 미분해서 기울기를 구하고, 값이 작아지는 방향으로 파라미터를 움직이다 보면 손실함수가 최소화되는 지점에 도달한다.

.. math::

    \theta_{i+1} = \theta_{i} - \rho \frac{\partial{J}}{\partial{\theta_{i}}}

Gradient Boosting은 이 탐색 과정이 함수 공간에서 이루어진다고 생각하면 쉽다.
그래서 손실함수를 파라미터가 아니라 현재까지 학습된 모델 함수로 미분한다.

.. math::

    f_{i+1} = f_{i} - \rho \frac{\partial{J}}{\partial{f_{i}}}

파라미터 공간에서는 계산된 기울기를 따라서 학습률(Learning Rate, :math:`\rho` )에 맞춰 :math:`\theta` 를 업데이트하면 된다.

함수 공간에서는 어떤 일이 생기는지 알아보기 위해 손실함수가 Squared Error: :math:`\frac{1}{2}(y - f_{i})^{2}` 인 경우를 보자.
이 때 기울기는 :math:`y - f_{i}` 로서, 다름아닌 잔차값이다.
모델 함수 (:math:`f_{i}` )에 잔차 (:math:`y-f_{i}` )를 더하면 당연히 :math:`y` 가 나오겠지만, 이건 의미가 없다.

대신 Gradient Boosting은 이 미분값을 다음 모델 (Weak Learner)의 타겟으로 넘긴다.
Squared Error를 쓰는 경우를 예로 들면, 현재 모델의 잔차를 타겟으로 놓고 새로운 모델 피팅을 한다.
기존 모델은 이 새로운 모델을 흡수해서 Bias를 줄인다.
그리고 다시 잔차를 구하고 모델을 피팅해서 더하기를 반복한다.
매우 단순하고 직관적인 방법인데, 이걸 손실함수를 L2로 설정한 Gradient Boosting으로 설명할 수 있다.

정리하면 Gradient Boosting에서는 Gradient가 현재까지 학습된 모델의 약점을 드러내는 역할을 하고, 다른 모델이 그걸 중점적으로 보완해서 성능을 Boosting한다.
위에서는 L2 손실함수를 썼지만 미분만 가능하다면 다른 손실함수도 얼마든지 쓸 수 있다는 것이 장점이다.
부스팅 알고리즘의 특성상 계속 약점 (오분류/잔차)을 보완하려고 하기 때문에 잘못된 레이블링이나 아웃라이어에 필요 이상으로 민감할 수 있다.
이런 문제에 강인한 L1 Loss나 Huber Loss를 쓰고자 한다면 그냥 손실함수만 교체하면 된다.
손실함수의 특성은 Gradient를 통해 자연스럽게 학습에 반영된다.


==================
XGBoost
==================

XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable



**Reference**
    * `Gradient Boosting 알고리즘: 개념 <http://4four.us/article/2017/05/gradient-boosting-simply>`_
    * `boosting 기법 이해 (bagging vs boosting) <https://www.slideshare.net/freepsw/boosting-bagging-vs-boosting>`_
    * `Introduction to Boosted Trees (한국어 버젼) <http://ishuca.tistory.com/388>`_

