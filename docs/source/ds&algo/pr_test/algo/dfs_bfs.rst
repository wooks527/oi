============
DFS and BFS
============

* :doc:`DFS and BFS </ds&algo/algo/dfs_bfs>`


Problems
========

여행 경로
********

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


구슬 탈출
********

* 문제

    * `구슬 탈출 4 <https://www.acmicpc.net/problem/15653>`_
    * 보드를 가중치가 1인 그래프로 표현할 수 있고, 이를 통해 최소 방향 전환 횟수를 구할 수 있음
    * 총 가능한 상태의 개수: (NM)^2

* 코드

    * 

