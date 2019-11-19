====================
Batch normalization
====================

데이터가 큰 경우 하나의 Epoch 내에서 Batch 단위로 학습시킨다. 이 때 각 Batch마다 Feature의 분포가 달라져 Internal covariate shift 문제가 발생할 수 있다.

Internal covariate shift는 학습 시 계층별로 입력의 데이터 분포가 달라지는 현상을 말한다. Batch normalization은 각 Batch 별로 평균과 분산을 이용하여 정규화하는 방법이고, 이를 통해 Overfitting 문제를 해결할 수 있다.

그 이유를 개인적으로 생각해 봤을 때, Feature의 정규분포를 가지도록 만들어 Bias를 줄이기 때문에 Overfitting 문제를 해결할 수 있는 것 같다.


Reference
==========

* `Dongyu Kang blog <http://dongyukang.com/%EB%B0%B0%EC%B9%98-%EC%A0%95%EA%B7%9C%ED%99%94-%EB%85%BC%EB%AC%B8%EC%9D%84-%EC%9D%BD%EA%B3%A0/>`_
