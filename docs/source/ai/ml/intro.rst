====
소개
====

머신러닝의 출현 배경
===================

앞서 언급한 것처럼 머신러닝은 **머신러닝 기법이 스스로 데이터를 분석해 모델을 찾아내는 기법** 을 의미한다. 그렇다면 머신러닝과 같은 방법이 왜 생겨나게 된 것일까? 다음 예제를 통해 그 이유를 살펴보자.

.. figure:: img/intro/numbers.png
    :align: center
    :scale: 100%

.. rst-class:: centered

    출처: `http://neuralnetworksanddeeplearning.com <http://neuralnetworksanddeeplearning.com/images/mnist_100_digits.png>`_

예를 들어 위와 같은 여러 가지 숫자 이미지를 보면, 사람은 이미지에서 어떤 숫자들이 있는지 쉽게 알 수 있다. 하지만 컴퓨터로 위 숫자를 인식하기 위해 전통적인 모델링 방법을 사용하면, 각 숫자를 구분하는 법칙이나 알고리즘을 사람이 찾아야 한다. 하지만 이는 굉장히 어렵고 복잡하다. 그러면 관점을 바꿔서 생각해보자. 우리는 실제로 숫자를 어떻게 인식하고 있는 걸까?

우리가 실제로 숫자를 인식할 때 명확한 기준이나 법칙을 사용한게 아니라, 0이나 1의 모양을 띄고 있으면 그냥 0이나 1이다라고 받아들인 것이다. 그 후로 다양한 숫자들을 보면서 점점 잘 구별하게 된 것이다.

컴퓨터로 숫자를 인식할 때도 비슷한 방법을 사용하면 좋지 않을까라고 생각해서 만들어진 것이 머신러닝이다. 한 마디로 머신러닝은 위 사례처럼 **명시적으로 기준이나 법칙을 가진 모델을 구하기 어려운 경우, 학습 데이터에서 머신러닝 기법 스스로 모델을 찾는 방법** 이다.


머신러닝의 문제점
================

지금까지 설명한 내용을 그림으로 표현하면 다음 그림의 세로축 흐름과 같고, 이는 머신러닝이 스스로 데이터로부터 모델을 찾아내는 과정을 의미한다.

.. figure:: img/intro/ml_process.png
    :align: center
    :scale: 50%

그렇다면 가로축의 흐름은 무엇일까? 이는 세로축 과정으로 학습된 모델을 이용하여 실제 현장 데이터를 이용해 추론 (Inference)하는 과정을 의미한다. 즉, **실제 데이터를 머신러닝 기법으로 찾아낸 (=학습된) 모델에 적용하여 원하는 결과를 도출해내는 과정** 이다 (예: 스팸 필터).

이러한 구조가 머신러닝의 근본적인 문제점이다. 예를 들어 학습 데이터가 실제 데이터의 특성을 잘 반영하고 있지 않은 경우, 학습 데이터에서 머신러닝 기법으로 열심히 모델을 찾아내도 실제로 작동하지 않을 수 있다.

그래서 실제 데이터의 특성이 잘 반영되어 있고 편향되지 않은 학습 데이터를 구하는 것이 중요하다. 결국 학습 데이터로 찾아낸 모델이 다른 실제 데이터에서도 잘 동작하게 하는 것이 궁극적인 목표이고, 이러한 모델이 **일반화 (Generalization)** 가 잘 된 모델이라고 할 수 있다. 그래서 일반화가 잘 된 모델이 성능이 좋다고 해도 과언이 아니다.

.. _overfitting:

과적합
******

일반화된 머신러닝 모델을 만드는데 가장 큰 걸림돌 중 하나는 **과적합 (Overfitting)** 이다. 말 그대로 모델이 학습 데이터에 과도하게 적합되어 있는 상태를 의미한다. 예를 들어 도자기인지 아닌지 구분하는 모델이 있다고 하자.

.. figure:: img/intro/overfitting_ex.png
    :align: center
    :scale: 50%

상단 좌측 그림과 같은 모양의 도자기를 모델이 반복적으로 학습한 후 상단 우측 그림과 같은 새로운 형태의 도자기를 구분하라고 했을 때, 모델은 도자기인지 아닌지 구분을 잘 못할 수 있다. 이러한 상황에서 학습된 모델은 좌측 도자기 이미지에 과적합되어 있다고 할 수 있다.

이처럼 **학습 데이터로 학습한 모델이 주어진 학습 데이터에 과도하게 적합되어 있는 상태** 를 과적합이라고 한다. 즉, 모델이 일부 데이터가 마치 전체 데이터를 의미하는 것으로 받아들이고 학습되어, 학습 데이터와 다른 실제 데이터에서 학습된 모델이 작동하지 않는 문제가 생길 수 있다. 과적합에 대한 더 자세한 내용은 "`과적화 심화 <regularization.html#advanced_overfitting>`_"에서 확인할 수 있다.

그렇다면 과적합 문제를 어떻게 해결할 수 있을까? 대표적인 방법으로 :doc:`정칙화 또는 규제 (Reularization) <regularization>` 와 검증 (Validation)이 있는데 이는 나중에 다시 자세히 설명하려고 한다. 결국 이러한 방법들로 과적합을 해결하여 일반화된 모델을 찾는 것이 목표다.


머신러닝 종류
=============

In ML, there are three algorithms:

.. figure:: img/intro/ml_algorithms.png
    :align: center
    :scale: 40%

Supervised learning
********************

**Point**

* "Right answers" are given

**Types**

* Regression (:doc:`Link <linear_regression>`)
* Classification.

-----------
Regression
-----------

* Map input variables to some continuous functions to predict results within a continuous output
* Example: Housing price prediction

.. figure:: img/intro/regression_ex.png
    :align: center
    :scale: 40%

--------------
Classification
--------------

* Map input variables into discrete categories to predict results within a discrete output
* Example: Breast cancer or Test grade (A, B, C, D, F)

.. figure:: img/intro/classification_ex1.png
    :align: center
    :scale: 40%

.. figure:: img/intro/classification_ex2.png
    :align: center
    :scale: 40%

Unsupervised learning
**********************

**Point**

* Allow us to approach problems with little or no idea what our results should look like
* Derive the structure from data where we don't necessarily know the effect of the variables
* No feedback based on the prediction results

**Types**

* Clustering
* Non-clustering

-----------
Clustering
-----------

* Find groups with patterns being close to each other
* Example: Google news clustering

.. figure:: img/intro/clustering_ex.png
    :align: center
    :scale: 40%

---------------
Non-clustering
---------------

* Find the structure in a chaotic environment
* Example: Cocktail party problem

.. figure:: img/intro/non-clustering_ex.png
    :align: center
    :scale: 40%


Reinforcement learning
***********************

Reinforcement learning (RL) is an area of machine learning concerned with how software agents ought to take actions in an environment so as to maximize some notion of cumulative reward (Ref.: `Wikipedia <https://en.wikipedia.org/wiki/Reinforcement_learning>`_).

.. figure:: img/intro/reinforcement_learning.png
    :align: center
    :scale: 40%


요약
====

* 머신러닝은 머신러닝 기법이 스스로 데이터를 분석해 모델을 찾아내는 기법을 의미함

* 머신러닝의 문제점

    * 머신러닝이 학습 데이터로 모델을 학습시키고, 이 모델을 실제 데이터에 적용시킬 때 작동하지 않을 수 있음 (학습 데이터와 실제 데이터 차이 ↑)
    * 따라서 학습된 모델이 실제 데이터에도 잘 동작할 수 있게 일반화하는 것이 중요함

* 과적합

    * 학습된 모델이 주어진 학습 데이터에 과도하게 적합되어 있는 상태를 의미함
    * 정칙화나 검증을 통해 해결 가능

* 머신러닝 종류

    * 지도 학습

        * 학습 데이터에 대한 정답이 주어진 경우
        * 회귀와 분류가 있음

    * 비지도 학습

        * 학습 데이터에 대한 정답이 없는 경우
        * 클러스터링이 있음

    * 강화 학습
        
        * 모델이 특정 동작 시 그 보상이 최대가 되는 방향으로 학습하는 방법


:h2:`출처`

* `One page summary <https://docs.google.com/document/d/1xXpvTas6hPVzixJcUIlihBr3DQet8KhHcFrkZ2SX9yE/edit?usp=sharing>`_
* `Coursera, Machine Learning <https://www.coursera.org/learn/machine-learning>`_
* `모두를 위한 머신러닝/딥러닝 강의 <http://hunkim.github.io/ml/>`_
