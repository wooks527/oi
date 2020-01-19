==============
Loss function
==============

Machines learn by means of a loss function. It’s a method of evaluating how well specific algorithm models the given data.

Broadly, loss functions can be classified into two major categories depending upon the type of learning tasks (Regression and classification).


Regression loss
================

* Mean Square Error (MSE) / Quadratic Loss / L2 Loss
* Mean Absolute Error (MAE) / L1 Loss
* Mean Bias Error (MBE)


Classification loss
====================

********************************
Hinge Loss/Multi class SVM Loss
********************************

추후 정리 필요


*********************************************
Cross entropy loss / Negative log likelihood
*********************************************

Classification 문제에서 Loss function으로 Cross entropy를 사용한다. 그 이유는 무엇일까?

-----------
확률론적 접근
-----------

딥러닝 모델을 학습시키기 위해 Maximum likelihood를 사용할 수 있다. 주어진 입력과 파라미터를 기반으로 정답이 나타날 확률이 우도라고 할 수 있다. 그리고 이를 최대화하는 파라미터를 구하는 것이 Maximum likelihood를 구하는 것이라고 할 수 있다.

이를 수식으로 나타내면 결국 Cross entropy와 동일한 형태의 식이 나온다.

--------------
정보 이론적 접근
--------------

두 확률분포 :math:`p` 와 :math:`q` 사이의 차이를 계산할 때 Cross entropy가 사용된다.

Classification 문제에서도 학습 데이터의 분포와 모델이 예측한 결과의 분포 차이가 Loss에 해당하고, 이것이 Cross entropy이다.


 (?)


Reference
==========

* `Towards Data Science <https://towardsdatascience.com/common-loss-functions-in-machine-learning-46af0ffc4d23>`_
* `ratsgo's Blog <https://ratsgo.github.io/deep%20learning/2017/09/24/loss/>`_
