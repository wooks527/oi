============
DFS and BFS
============

DFS와 BFS는 그래프를 탐색하는 대표적인 방법이다. 이를 위해서는 우선 그래프를 이해해야 한다. 그래프 (Graph)는 정점 (Vertex)과 간선 (Edge or Link)으로 구성되고, 크게 유향 (Directed) 그래프와 무향 (Undirected) 그래프가 있다.

이러한 그래프를 탐색하기 위해서는 DFS는 스택 (Stack), BFS는 큐 (Queue)라는 자료구조가 활용되고, 다음은 DFS와 BFS에 대한 개념이다.

* 깊이 우선 탐색 (DFS, Depth-First Search)

    * 한 정점에서 인접한 모든 (아직 방문하지 않은) 정점을 방문하되, 각 인접 정점을 기준으로 깊이 우선 탐색을 끝낸 후 다음 정점으로 진행
    * 스택을 이용하여 어느 정점에서 DFS를 하고 있는지 기억하고 되돌아감

* 너비 우선 탐색 (BFS, Breadth-First Search)

    * 한 정점에서 인접한 모든 (아직 방문하지 않은) 정점을 방문하고, 방문한 각 인접 정점을 기준으로 (방문한 순서에 따라) 또다시 너비 우선 탐색을 행함
    * 큐를 이용하여 어느 정점에서 BFS를 해야 하는지를 기록하고 진행함


여행 경로
========

* 문제

    * `Programmers > 코딩테스트 연습 > 깊이/너비 우선 탐색 (DFS/BFS) > 여행 경로 <https://programmers.co.kr/learn/courses/30/lessons/43164>`_

* 그래프의 표현

    .. figure:: ../img/problems/bfs_dfs/graph.png
        :align: center
        :scale: 40%

    *

* 해결법

    * 스택을 이용하여 재귀적인 "한 붓 그리기" 문제 → 재귀적인 성질을  가진 DFS 응용

    * 시작 정점은 "ICN"

    * 모든 정점 방문이 아니라 모든 간선 방문
        
        * 한 정점에서 택할 간선이 두 개 이상인 경우?
        * 공항 이름의 알파벳 순서를 따름

* 코드

    * `Github <https://github.com/hwkim89/programmers/blob/master/bfs_dfs/travel_route.ipynb>`_

