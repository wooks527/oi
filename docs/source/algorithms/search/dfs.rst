DFS (Depth First Search)
========================

========
Example
========

.. figure:: img/dfs.png
    :align: center
    :scale: 30%


======
Codes
======

https://github.com/hwkim89/algorithms/blob/master/search/dfs.ipynb


===============
Time complexity
===============

**인접리스트로 표현된 그래프**
    * O(N + E)

**인접행렬로 표현된 그래프**
    * O(N^2)


=========
Features
=========

그래프 내에 적은 숫자의 간선만을 가지는 희소 그래프(Sparse Graph) 의 경우 인접 행렬보다 인접 리스트를 사용하는 것이 유리


**Reference**
    * https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html