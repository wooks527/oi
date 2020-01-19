=================
Machine learning
=================

머신러닝을 인터넷에 검색하면 위키피디아나 유명한 연구자들이 정의한 머신러닝을 찾을 수 있다.

* Wikipedia

    * Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to perform a specific task without using explicit instructions, relying on patterns and inference instead (머신러닝은 컴퓨터 시스템이 패턴과 추론에 의지하지 않고 명시적 지시 없이 특정 작업을 수행하기 위해 사용하는 알고리즘 또는 통계적 모델에 대한 과학적 연구이다).

* Arthur Samuel (1959)

    * The field of study that gives computers the ability to learn without being explicitly programmed.

* Tom Mitchel (1998)

    * A computer program is said to learn from experience E with respect to some class of task T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E

뭔가 직관적으로 잘 이해가 되지 않는데, 간단히 말하면 **머신러닝은 데이터에서 모델을 찾아내는 기법** 이다. 그리고 사람이 데이터로부터 모델을 찾는게 아니라, **머신러닝 기법이 스스로 데이터를 분석해 모델을 찾는다.** 그래서 머신러닝이라는 이름이 만들어졌고, 이 때 사용하는 데이터를 학습 데이터 (Training data)라고 한다.

그렇다면 왜 데이터에서 모델을 찾아내는 기법이 나타나게 된 걸까? 지금부터 그 이유를 하나씩 설명하려고 한다.

.. toctree::
    :caption: 목차
    :maxdepth: 1

    intro
    linear_regression
    logistic_regression
    loss_func
    regularization
    optimization
    neural_networks/nn_learning
    recommender_systems


Reference
==========

* `Wikipedia, Machine learning <https://en.wikipedia.org/wiki/Machine_learning>`_
* 딥러닝 첫걸음, 김성필, 2018
