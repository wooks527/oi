Graph
======

Graph는 연결되어 있는 객체 간의 관계를 표현할 수 있는 자료구조이다.


========
History
========

**Euler tour**

그래프에 존재하는 모든 간선을 한번만 통과하면서 처음 정점으로 되돌아오는 경로


===========
Terminology
===========

* Vertex/Node, Edge/Link
* Adjacent vertex
* Degree, In-degree, Out-degree
* Simple path, Cycle
* Connected component (연결 성분)
    * 연결 성분이란 최대로 연결된 부분 그래프를 의미


=======
Types
=======

* Undirected graph (무방향 그래프)
* Directed graph (방향 그래프)
* Weighted graph (가중치 그래프) / Network (네트워크)
* Subgraph (부분 그래프)
* Complete graph (완전 그래프)
* Dense graph (밀집 그래프) / Sparse graph (희소 그래프)
* `Spanning tree (신장 트리) <https://oi.readthedocs.io/en/latest/algorithms/data_structure/tree/spanning_tree.html>`_


==================
Expression methods
==================

* Adjacency matrix (인접 행렬)
* Adjacency list (인접 리스트)


============
Graph search
============

* `DFS (Depth first search) <https://oi.readthedocs.io/en/latest/algorithms/search/dfs.html>`_
* `BFS (Breath first search) <https://oi.readthedocs.io/en/latest/algorithms/search/bfs.html>`_


============================================================================================================================
`Shortest path (최단 경로) <https://oi.readthedocs.io/en/latest/algorithms/data_structure/graph/shortest_path.html>`_
============================================================================================================================


===========
Graph sort
===========

* `Topological sort (위상 정렬) <https://oi.readthedocs.io/en/latest/algorithms/sort/topological_sort.html>`_


**References**
    * C언어로 쉽게 풀어쓴 자료 구조, 천인국 저