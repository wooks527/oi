===============
Regularization
===============

이미 Machine learning에서 정리하여 Regularization 참고하면 된다. 여기서는 Deep learning에서 Regularization 하는 방법에 대해서 언급하려고 한다.


Overfitting
============

Machine learning에서 언급한 것처럼 모델이 Training dataset에 과도하게 적합되어 새로운 Data에 대해 제대로 추론하지 못하는 경우를 말한다. 이를 해결하는 방법은 다음과 같다.

* Machine learning에서 언급한 방법들 (`Link <../ai/machine_learning/regularization.html#overfitting>`_)

* Early stopping

    * Epoch가 너무 크면 Overfitting 문제가 생결 수 있음
    * 여러 Epoch 동안 Loss가 감소하지 않으면 더 이상 진행하지 않는 방법

* Dropout

    * 지정한 비율의 뉴런을 제거하는 방법

* Batch normalization (:doc::`Link <batch_norm>`)

    * Batch 별로 다른 분포를 가지는 문제를 해결하기 위해 Normalization 하는 방법
    * 이를 통해 Overfitting 문제 개선

* Data augmentation

    * 데이터 수를 늘려 Overfitting 문제를 개선


Reference
==========

* 
