===========
정렬 (Sort)
===========

.. figure:: img/sort&search/sort.png
    :align: center
    :scale: 40%

* sorted()

    * 내장함수
    * 정렬된 새로운 리스트를 얻어냄

* sort()

    * 리스트의 메서드
    * 해당 리스트를 정렬함

.. code-block:: python

    >> L = [3, 8, 2, 7, 6, 10, 9]
    >> L2 = sorted(L)
    >> L2
    [2, 3, 6, 7, 8, 9, 10]
    >> L
    [3, 8, 2, 7, 6, 10, 9]
    >> L.sort()
    >> L
    [2, 3, 6, 7, 8, 9, 10]

추가로, 정렬의 순서를 반대로 하려면 reverse=True를 사용하면 된다.

* L2 = sorted(L, reverse=True)
* L.sort(reverse=True)

문자열로 이루어진 리스트의 경우, 정렬 순서는 사전 순서 (알파벳 순서)를 따른다. 문자열의 길이순으로 정렬하기 위해서는 정렬에 이용하는 key를 지정하면 된다.

.. code-block:: python

    >> L = ['abcd', 'xyz', 'spam']
    >> sorted(L, key=lambda x: len(x))
    ['xyz', 'abcd', 'spam']
    >> L = ['spam', 'xyz', 'abcd']
    >> sorted(L, key=lambda x: len(x))
    ['xyz', 'spam', 'abcd']

리스트 내에 딕셔너리를 원소로 가진 경우에도 키를 이용하여 정렬할 수 있다.

* L = [{'name': 'John', 'score': 83}, {'name': 'Paul', 'score': 92}]
* L.sort(key=lambda x: x['name']) → 레코드를 이름 순서대로 결정
* L.sort(key=lambda x: x['score'], reverse=True) → 레코드를 점수 높은 순서대로 결정

그 외에도 다양한 정렬 알고리즘이 있다.

* :doc:`Quick sort <sort/quick_sort>`
