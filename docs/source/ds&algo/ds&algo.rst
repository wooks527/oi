===============
자료구조와 알고리즘
===============

자료구조
======

자료구조는 데이터를 나타내는 방법이다. 기본적으로 제공하는 데이터 타입에는 문자열 (str), 리스트 (list), 사전 (dict), 순서쌍 (tuple), 집합 (set) 등이 있다.

* 문자열: 'This is a string.'
* 리스트: [1, 2, 3, 4]
* 사전: {'a': 6, 'b': 'text'}

기본 데이터 타입이 존재함에도 자료구조를 사용해야 하는 이유는 무엇일까?

기본적으로 제공하는 데이터 타입으로 표현하여 해결할 수 없는 문제의 경우, 자료구조를 사용하면 해결할 수 있다. 예를 들어 최대값을 구하는 함수 max는 리스트를 활용하여 최대값을 찾는다. 하지만 그 자료 수가 많아지면 굉장히 오래 걸리기 때문에 다른 방법이 필요하다

문제 해결을 위한 다양한 자료구조들이 있으며, 그 목록은 다음과 같다.

.. toctree::
    :maxdepth: 1

    linear_array
    queue
    heap


알고리즘
======

알고리즘은 다음과 같이 정의할 수 있다.

* 사전적 정의: 어떤 문제를 해결하기 위한 절차, 방법, 명령어들의 집합
* 프로그래밍: 주어진 문제의 해결을 위한 자료구조와 연산 방법에 대한 선택

문제마다 사용할 수 있는 알고리즘이 다르며, 그 목록은 다음과 같다.

.. toctree::
    :maxdepth: 1

    sort&search
    recursive_algo
    complexity


프로그래밍 문제
============

자료구조와 알고리즘에 대한 이해를 기반으로 다양한 문제를 실제로 적용해 봄으로써 다양한 문제 상황에서 어떤 자료구조와 알고리즘을 사용해야 하는지에 대한 이해를 높이고자 한다. 프로그래밍 문제를 풀 수 있는 사이트는 다양하다. 여기서는 프로그래머스라는 사이트에서 제공하는 문제와 그에 대한 해결책을 보이고자 한다.

아래의 목록은 다양한 알고리즘으로 해결할 수 있는 문제들과 그에 대한 해법을 나타낸 것이다.

.. toctree::
    :maxdepth: 1

    problems/queue
    problems/heap
    problems/stack
    problems/hash
    problems/greedy
    problems/sort
    problems/dynamic_pr
    problems/bfs_dfs
    problems/others


문제를 풀 때 유의사항
*****************

* 제한사항에 유의하기
* 문제를 이해하고 한 번에 푸는 것이 아니라 문제 해결에 필요한 하나하나의 단계로 해법을 표현해야 한다.


참조
====

* https://programmers.co.kr/learn/courses/57
* `Programmers <https://programmers.co.kr/learn/challenges>`_
