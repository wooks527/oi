====================
선형 탐색과 이진 탐색
====================

선형 탐색 (Linear search)
=========================

.. figure:: ../img/search/linear_search.png
    :align: center
    :scale: 40%

선형 탐색의 경우 리스트의 길이에 비례하는 시간이 소요되며 시간 복잡도는 :math:`O(n)` 이다. 최악의 경우에는 모든 원소를 다 비교해 봐야한다.

.. code-block:: python

    def linear_search(L, x):
        i = 0
        while i < len(L) and L[i] != x:
            i += 1
        if i < len(L):
            return i
        return -1

    >> S = [3, 8, 2, 7, 6, 10, 9]
    >> linear_search(S, 6)
    4
    >> linear_search(S, 1)
    -1
    >> S.index(6)
    4
    >> S.index(1)
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-7-58b6e9d2e949> in <module>()
    ----> 1 S.index(1)

    ValueError: 1 is not in list


이진 탐색 (Binary search)
=========================

이진 탐색은 크기 순으로 정렬되어 있다는 성질을 이용하는 방법이고, 탐색하려는 리스트가 이미 정렬되어 있는 경우에만 적용 가능하다.

.. figure:: ../img/search/binary_search_01.png
    :align: center
    :scale: 40%

.. figure:: ../img/search/binary_search_02.png
    :align: center
    :scale: 40%

.. figure:: ../img/search/binary_search_03.png
    :align: center
    :scale: 40%

이진 탐색은 한 번 비교가 일어날 때마다 탐색 영역을 반씩 줄인다 (Divide and conquer). 따라서 시간복잡도는 :math:`O(logn)` 이다.

Code
*****

* 코드 설명

.. code-block:: text

    리스트 L 과, 그 안에서 찾으려 하는 원소 x 가 인자로 주어질 때, x 와 같은 값을 가지는 원소의 인덱스를 리턴하는 함수 solution() 을 완성하세요. 만약 리스트 L 안에 x 와 같은 값을 가지는 원소가 존재하지 않는 경우에는 -1 을 리턴합니다. 리스트 L 은 자연수 원소들로 이루어져 있으며, 크기 순으로 정렬되어 있다고 가정합니다. 또한, 동일한 원소는 두 번 이상 나타나지 않습니다.

    예를 들어,
    L = [2, 3, 5, 6, 9, 11, 15]
    x = 6
    의 인자들이 주어지면, L[3] == 6 이므로 3 을 리턴해야 합니다.

    또 다른 예로,
    L = [2, 5, 7, 9, 11]
    x = 4
    로 주어지면, 리스트 L 내에 4 의 원소가 존재하지 않으므로 -1 을 리턴해야 합니다.

* 코드

    * Recursive version
        
    .. code-block:: python

        def b_search(L, x, low, high):
            if low == high: return -1
            
            mid = (low+high) // 2
            if L[mid] == x:
                return mid
            elif L[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
                
            return b_search(L, x, low, high)

        def solution(L, x):
            low = 0
            high = len(L) - 1
            answer = b_search(L, x, low, high)
            return answer

    * Iterative version
        
    .. code-block:: python

        def solution(L, x):
            low = 0
            high = len(L) - 1
            while low <= high:
                mid = (low+high) // 2
                if L[mid] == x:
                    return mid
                elif L[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1


성능 비교
=========

선형 탐색과 이진 탐색의 성능을 비교했을 때 아래의 이미지와 같다.

.. figure:: ../img/search/performances.png
    :align: center
    :scale: 40%

그렇다고 해서 항상 이진 탐색이 좋은 것은 아니다. 왜냐하면 이진 탐색은 리스트가 정렬되어 있는 것을 전제로 하기 때문이다.


BFS와 DFS
==========


:h2:`참조`

* https://programmers.co.kr/learn/courses/57
