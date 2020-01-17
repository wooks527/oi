========================
Curse of dimensionality
========================

위키피디아에서 차원의 저주 (Curse of dimensionality)는 "The curse of dimensionality refers to various phenomena that arise when analyzing and organizing data in high-dimensional spaces (often with hundreds or thousands of dimensions) that do not occur in low-dimensional settings such as the three-dimensional physical space of everyday experience."라고 언급했다.

즉, 고차원 공간에 있는 데이터를 분석할 때 발생하는 여러 가지 현상을 차원의 저주라고 한다. 가장 대표적인 현상은 차원이 증가하면, 하나의 데이터를 나타내는 공간 역시 증가해서 하나의 데이터를 표현하는데 더 많은 변수가 필요하게 된다.

여기서 이해를 돕기 위해 차원과 변수의 정의를 먼저 언급하려고 한다.

* 차원 (Dimension)

    * 수학에서 공간 내에 있는 점 등의 위치를 나타내기 위해 필요한 축의 개수 (= 변수의 수)

* 변수 (Variable)

    * 데이터를 표현하기 위해 필요한 요소 (= 특징)

따라서 차원이 커지면 데이터를 나타내는데 필요한 변수의 양이 많아지기 때문에 이를 설명할 수 있을만큼의 데이터가 필요하게 된다. 예를 들어 하나의 변수를 설명하는데 필요한 최소한의 데이터 수가 30개라고 하자. 27차원 데이터인 경우 27 x 30 = 810개의 데이터가 필요하고, 1,000차원 데이터의 경우 1,000 x 30 = 30,000개의 데이터가 필요하게 된다.

정리하면, "**차원 ↑** → **데이터 표현에 필요한 변수의 수 ↑** → **각 변수를 설명하는데 필요한 최소한의 데이터 수 ↑** → **필요한 데이터 수 ↑↑↑**" 라고 할 수 있고, 이러한 현상을 차원의 저주라고 한다.


Reference
==========

* `Wikipedia, Curse of dimensionality <https://en.wikipedia.org/wiki/Curse_of_dimensionality#Optimization>`_
* `Time Traveler, 7. Curse of Dimension, Reduction of input dimension (차원의 저주) <https://89douner.tistory.com/31?category=868069>`_
* `꼬깔콘, Dimension / 차원 / 차원의 저주 / 차원 축소 <https://kkokkilkon.tistory.com/127>`_