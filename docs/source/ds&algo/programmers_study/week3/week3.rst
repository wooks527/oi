===========
3주차: 탐색
===========

3주차에는 탐색과 관련된 문제를 풀이한 내용을 정리하려고 한다.

보통 탐색 문제에서 많이 사용하는 방법은 DFS와 BFS이다. DFS는 깊이 우선 탐색이고 BFS는 너비 우선 탐색이다.

각 탐색 방법의 코드는 어느 정도 정형화 되어 있고 그 내용은 아래와 같다.

* DFS

.. code:: python

    def dfs(graph, start_node):
        stack, visited = [], set()
        stack.append(start_node)
        while stack:
            cur_node = stack.pop()
            visited.add(cur_node)
            for next_node in graph[cur_node]:
                if next_node not in visited:
                    stack.append(next_node)
                    visited.add(next_node)
        return visited

* BFS

.. code:: python

    def bfs(graph, start_node):
        queue, visited = deque(), set()
        queue.append(start_node)
        while queue:
            cur_node = queue.popleft()
            visited.add(cur_node)
            for next_node in graph[cur_node]:
                if next_node not in visited:
                    queue.append(next_node)
                    visited.add(next_node)
        return visited

