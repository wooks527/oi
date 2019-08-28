=====
Heap
=====

힙 (Heap)은 최대/최소 원소를 빠르게 찾을 수 있게 만들어진 자료구조이다. 힙은 Max heap과 Min heap이 있다. 그리고 크게 힙 구성 (Heapify), 삽입 (Insert), 삭제 (Remove) 3개의 연산으로 구성되어 있고, 각각의 복잡도는 :math:`O(nlogn),` :math:`O(logn),` :math:`O(logn)` 이다.

힙은 완전 이진 트리 (Complete binary tree)이고, 배열을 이용하여 구현 가능하다. 힙은 정렬 (Heap sort)나 우선 순위 큐 (Priority queue) 등에 응용될 수 있다.

Python에는 Min heap이 구현되어 있고 heapq 패키지를 통해 사용할 수 있다.

.. code-block:: python

    import heapq
    heapq.heapify(L) #  리스트 L로부터 min heap 구성
    m = heapq.heappop(L) # min heap L에 최소값 삭제 (+ 반환)
    heapq.heappush(L, x) # min head L에 원소 x 삽입


더 맵게
======

* 문제

    * `Programmers > 코딩테스트 연습 > 힙 (Heap) > 더 맵게 <https://programmers.co.kr/learn/courses/30/lessons/42626>`_

* 해결법

    * 오름차순으로 정렬 후 앞에서부터 하나씩 해결할 수 있다.

        * 복잡도

            * 최악의 경우

                * 수가 하나 남을 때까지 섞어야 하는 경우 (:math:`n-1` 회)

            * 각 단계 (섞는 일)에서 요구되는 계산량

                * 정렬된 리스트에 순서 맞추어 원소 삽입
                * :math:`O(n)`

            * 전체 복잡도

                * :math:`O(n^2)`

    * 힙을 이용하면 최대/최소 원소를 더 빠르게 꺼낼 수 있다.

        * 힙 (Heap)은 크게 Max heap, 

* 코드

    * `Github <https://github.com/hwkim89/programmers/blob/master/heap/more_spicy.ipynb>`_
