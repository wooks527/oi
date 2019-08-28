====================
Dynamic programming
====================

동적계획법 (Dynamic programming)은 주어진 최적화 문제를 재귀적인 방식으로 보다 작은 부분 문제로 나누어 부분 문제를 풀어, 이 해를 조합하여 전체 문제의 해답에 이르는 방식이다. 알고리즘의 진행에 따라 탐색해야 할 범위를 동적으로 결정함으로써 탐색 범위를 한정할 수 있다.

동적계획법을 활용하는 대표적인 예는 피보나치 수열이다. 이를 재귀함수로 구현하게 되면, 지수 함수의 복잡도를 가져 n 값이 조금만 커져도 동작이 멈추는 현상이 발생한다.

.. figure:: ../img/problems/dynamic_pr/recursive_fibonacci.png
    :align: center
    :scale: 40%

하지만 동적계획법을 적용한다면 선형함수의 복잡도를 가진다.

.. figure:: ../img/problems/dynamic_pr/dynamic_fibonacci.png
    :align: center
    :scale: 40%

동적계획법을 활용할 수 있는 대표적인 예는 배낭 문제 (Knapsack problem)이다. 배낭 문제는 가장 높은 값을 가지도록 물건들을 골라 배낭에 담는 문제이다.

.. figure:: ../img/problems/dynamic_pr/knapsack_pr.png
    :align: center
    :scale: 40%


N으로 표현
=========

* 문제

    * `Programmers > 코딩테스트 연습 > 동적계획법 (Dynamic programming) > N으로 표현 <https://programmers.co.kr/learn/courses/30/lessons/42895>`_

* 해결법

    * N을 한 번 사용해서 만들 수 있는 수들, N을 두 번 사용해서 만들 수 있는 수들, ...
    
    * 이전에 계산된 결과값을 다음 단계에서 활용할 수 있다.
    
    * 일반화: N = x
        
        .. figure:: ../img/problems/dynamic_pr/n_representation.png
            :align: center
            :scale: 40%


* 문제의 복잡도

    * (발생할 수 없는) 최악의 경우

        .. figure:: ../img/problems/dynamic_pr/n_representation_complexity_01.png
            :align: center
            :scale: 40%

    * 실제로 만들어지는 결과의 개수

        .. figure:: ../img/problems/dynamic_pr/n_representation_complexity_02.png
            :align: center
            :scale: 40%
            
    * 문제의 성질에 따라, 동적계획법으로 풀어냄으로써 탐색해야 하는 범위를 효과적으로 줄일 수 있음

* 코드

    * `Github <https://github.com/hwkim89/programmers/blob/master/dynamic_programming/n_representation.ipynb>`_
