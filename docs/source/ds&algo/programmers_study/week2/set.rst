====
Set
====

Python은 set이라는 형태로 집합 자료구조를 한다. 집합은 다음과 같은 경우에 사용한다.

* 데이터 중복이 필요 X

    * 집합의 원소는 Unique함 (예: 집합에 5를 2번 넣어도 하나만 가짐)

* 정수가 아닌 데이터의 삽입/삭제/서치가 빈번한 경우

    * 리스트처럼 인덱스를 사용할 수 없는 문자열 등의 index를 활용하여 탐색하는 경우 (예: "abc" 원소 탐색 -> 리스트: O(N), 집합: O(1))

* (수학적으로) 교집합, 합집합, 차집합을 계산하는 경우

다음은 집합의 Operation의 Time complexity이다.

=========  ================  ==============================
Operation  예시               Time Complexity - Average Case
=========  ================  ==============================
탐색        "abc" in my_set   O(1)
제거        my_set.remove     O(1)
합집합       set1 | set2       O(len(set1) + len(set2))
교집합       set1 & set2       O(min(len(set1), len(set2)))
차집합       set1 - set2       O(len(set1))
대칭차*      set1 ^ set2       O(len(set1))
=========  ================  ==============================

* 대칭차 = 합집합 - 교집합

참고로 집합에는 hashable 타입만 삽입할 수 있다.

* hashable 타입: int, float, decimal, bool, string, tuple, frozenset 등
* non-hashable 타입: list, dict, set, 유저가 직접 만든클래스 등


Init
=====

.. code-block:: python

    empty_set = set() # 빈 집합
    my_set = set([1, 2, 3, 1, 2, 3]) # 원소를 가지는 집합


Add
====

.. code-block:: python

    >> my_set = set()
    >> my_set.add(3)
    >> my_set.add('hi')
    >> my_set
    {3, 'hi'}

    >> my_list = [1,2,3,4]
    >> my_set.add(my_list) # 리스트를 set에 넣으면 에러
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-12-e53b1add151a> in <module>()
        2 my_set = set()
        3 my_list = [1,2,3,4]
    ----> 4 my_set.add(my_list) # 리스트를 set에 넣으면 에러

    TypeError: unhashable type: 'list'


Delete
======

.. code-block:: python

    my_set = set([1,2,3,4,5])
    my_set.remove(1)


합/차/교집합
==========

.. code-block:: python

    >> set1 = set([1,2,3,4,5])
    >> set2 = set([4,5,6,7,8])

    >> print(set1 | set2) # 합집합
    {1, 2, 3, 4, 5, 6, 7, 8}

    >> print(set1 - set2) # 차집합
    {1, 2, 3}

    >> print(set1 & set2) # 교집합
    {4, 5}


Reference
==========

* `Wikipedia, Python <https://wiki.python.org/moin/TimeComplexity>`_
