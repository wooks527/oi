===========
Quick sort
===========

Quick sort는 Divide and conquer 개념을 이용한 방법으로 시간 복잡도는 :math:`O(NlogN)` 이다.


Example
========

.. figure:: ../img/sort/quick_sort.png
    :align: center
    :scale: 30%


Codes
======

* https://github.com/hwkim89/algorithms/blob/master/sort/quick_sort.ipynb


Time complexity
================

Best case
**********

* The number of comparisons

    * 순환 호출의 깊이 (k) = log₂n
    * 각 순환 호출 단계의 비교 연산 = 평균 n번
    * 순환 호출의 깊이 * 각 순환 호출 단계의 비교 연산 = nlog₂n

* The number of exchanges

    * 비교 횟수보다 작으므로 무시 가능

* Best T(n) = O(nlog₂n)


Worst case
***********

* The number of comparisons

    * 순환 호출의 깊이 * 각 순환 호출 단계의 비교 연산 = n^2

* The number of exchanges

    * 비교 횟수보다 작으므로 무시 가능

* Worst T(n) = O(n^2)


Average case
*************

* T(n) = O(nlog₂n)


Reference
==========

* `Heee's Development Blog <https://gmlwjd9405.github.io/2018/05/10/algorithm-quick-sort.html>`_
