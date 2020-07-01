==============
알고리즘의 복잡도
==============

알고리즘의 복잡도는 크게 2가지로 나누어서 확인할 수 있다.

* 시간 복잡도 (Time complexity)

    * 문제의 크기와 이를 해결하는 데 걸리는 시간 사이의 관계

* 공간 복잡도 (Space complexity)

    * 문제의 크기와 이를 해결하는 데 필요한 메모리 공간 사이의 관계

여기에서는 시간 복잡도를 위주로 설명할 계획이다.


시간 복잡도
===========

시간 복잡도는 크게 2가지로 나누어 생각할 수 있다.

* 평균 시간 복잡도 (Average time complexity)

    * 임의의 입력 패턴을 가정했을 때 소요되는 시간의 평균

* 최악 시간 복잡도 (Worst-case time complexity)

    * 가장 긴 시간을 소요하게 만드는 입력에 따라 소요되는 시간


Big-O notation
***************

점근 표기법 (Asymptotic notation)의 하나로, 어떤 함수의 증가 양상을 다른 함수와의 관계로 표현하는 방법이다. 알고리즘의 복잡도를 표현할 때 쓰이며 :math:`O(logn),\ O(n),\ O(n^2),\ O(2^n)` 등으로 표기할 수 있다.

좀 더 상세히 설명하자면 입력의 크기가 n 일 때,

* :math:`O(logn):` 입력 크기의 로그에 비례하는 시간 소요
* :math:`O(n):` 입력 크기에 비례하는 시간 소요

여기서 계수는 크게 중요하지 않다.


다양한 알고리즘
============

선형 시간 알고리즘 :math:`O(n)`
******************************

예를 들어, :math:`n` 개의 무작위로 나열된 수에서 최댓값을 찾기 위해 선형 알고리즘을 적용했다고 하자.

.. figure:: img/complexity/o(n)_ex.png
    :align: center
    :scale: 40%

로그 시간 알고리즘 :math:`O(logn)`
*********************************

예를 들어, :math:`n` 개의 크기 순으로 정렬된 수에서 특정 값을 찾기 위해 이진 탐색 알고리즘을 적용했다고 하자.

.. figure:: img/complexity/o(logn)_ex.png
    :align: center
    :scale: 40%

이차 시간 알고리즘 :math:`O(n^2)`
********************************

예를 들어, :math:`n` 개의 무작위로 나열된 수에서 최댓값을 찾기 위해 삽입 정렬 알고리즘을 적용했다고 하자.

.. figure:: img/complexity/o(n^2)_ex.png
    :align: center
    :scale: 40%

* Best case: :math:`O(n)`
* Worst case: :math:`O(n^2)`

:math:`nlogn` 시간 알고리즘 :math:`O(nlogn)`
********************************************

삽입 정렬 알고리즘보다 더 낮은 시간 복잡도로 정렬하기 위해, :math:`n` 개의 무작위로 나열된 수에서 최댓값을 찾기 위해 병합 정렬 알고리즘을 적용했다고 하자. 참고로 입력 패턴에 따라 정렬 속도에 차이가 있지만, 정렬 문제에 대해 :math:`O(nlogn)` 보다 낮은 복잡도를 갖는 알고리즘은 존재할 수 없음이 증명되어 있다.

병합 정렬의 개념은 정렬할 데이터를 반씩 나누어 각각을 정렬시키는 것이다. 그래서 크게 2가지 단계로 구분할 수 있다.

* 분할

.. figure:: img/complexity/O(nlogn)_ex_01.png
    :align: center
    :scale: 40%

이 작업을 하는데 드는 시간 복잡도는 :math:`O(logn)` 이다.

* 정렬

.. figure:: img/complexity/O(nlogn)_ex_02.png
    :align: center
    :scale: 40%

이 작업을 하는데 드는 시간 복잡도는 :math:`O(n)` 이다.

최종적으로 병합 정렬의 전체 과정은 다음과 같고, 시간 복잡도는 :math:`O(nlogn)` 이다.

.. figure:: img/complexity/O(nlogn)_ex_03.png
    :align: center
    :scale: 40%

복잡한 문제: 배낭 문제 (Knapsack problem)
*************************************

배낭 문제는 주어진 배낭에 배낭의 한계를 넘지 않으면서 각 물건의 무게와 가치를 고려하여 최적의 물건을 담을 수 있는 경우를 결정하는 문제이다. 기존의 문제들보다 더 복잡한 문제이지만 추후에 다룰 Dynamic programming을 통해 해결할 수 있다.

.. figure:: img/complexity/knapsack_problem.png
    :align: center
    :scale: 40%


문제
====

.. toggle-header::
    :header: **문제**

    |
    객관식 1.
    N 개의 원소로 이루어진 배열이 있습니다. 이 배열을 반씩 나누어 각각 정렬한 뒤 병합 (merge) 하는 방법을 통해서, 소위 divide-and-conquer 방법으로 정렬할 수 있습니다. 이러한 방법으로 데이터를 정렬하는 알고리즘을 병합 정렬 (merge sort) 알고리즘이라고 부릅니다. 병합 정렬 알고리즘의 복잡도를 big-O 점근 표기법으로 표기한 것으로 다음 중 알맞은 것을 고르세요.

    ① :math:`O(logN)`

    ② :math:`O(N)`

    ③ :math:`O(NlogN)`

    ④ :math:`O(N^2)`

    ⑤ :math:`O(N^3)`

    
    객관식 2.
    이미 크기 순으로 정렬되어 있는 N 개의 원소를 가지는 배열로부터, 입력으로 주어진 데이터가 배열 내에 존재하는지, 또한 존재한다면 몇 번째 원소인지를 탐색하는 방법으로서, 배열의 가운데 원소와 입력 데이터를 비교하고 그 데이터와 같은 원소가 존재할 수 없는 절반의 배열을 버리는 방식을 택할 수 있습니다. 이러한 탐색 방법을 이진 탐색 (binary search) 이라고 부릅니다. 이진 탐색 알고리즘의 복잡도를 big-O 점근 표기법으로 표기한 것 중 다음에서 알맞은 것을 고르세요.

    ① :math:`O(logN)`

    ② :math:`O(N)`

    ③ :math:`O(NlogN)`

    ④ :math:`O(N^2)`

    ⑤ :math:`O(N^3)`

    
    객관식 3.
    N 개의 원소가 무작위 순서로 늘어서 있는 배열 내에, 입력으로 주어진 데이터가 존재하는지, 그리고 존재한다면 몇 번째 위치에 존재하는지를 알아내기 위하여 배열을 처음부터 시작해서 원소를 하나씩 입력 데이터와 비교하는 방법을 적용할 수 있습니다. 이러한 탐색 방법을 선형 탐색 (linear search) 이라고 부릅니다. 선형 탐색 알고리즘의 복잡도를 big-O 점근 표기법으로 표기한 다음 중 알맞은 것을 선택하세요.

    ① :math:`O(logN)`

    ② :math:`O(N)`

    ③ :math:`O(NlogN)`

    ④ :math:`O(N^2)`

    ⑤ :math:`O(N^3)`

    
    객관식 4.
    N 개의 수가 입력으로 주어진다고 할 때, 모든 원소들 사이의 대소 관계를 비교하여 N X N 행렬로 나타내고자 합니다. 이 문제를 풀기 위하여 모든 원소의 쌍에 대하여 대소 관계를 비교하여 그것을 행렬에 채우는 방법을 택한다고 할 때, 이 알고리즘의 복잡도를 big-O 점근 표기법으로 표기한 다음 중 알맞은 것을 선택하세요.

    ① :math:`O(logN)`

    ② :math:`O(N)`

    ③ :math:`O(NlogN)`

    ④ :math:`O(N^2)`

    ⑤ :math:`O(N^3)`

    
    객관식 5.
    N 행 N 열의 정사각행렬 A 와 B 가 주어진다고 할 때, 이 두 행렬의 곱 (product) 인 N X N 행렬 C 를 계산하기 위하여 다음과 같은 방법을 쓸 수 있습니다.

    .. code-block:: python

        for i in range(N):
            for j in range(N):
                C[i][j] = 0
                for k in range(N):
                    C[i][j] += A[i][k] * B[k][j]

    이러한 알고리즘을 이용하여 행렬의 곱셈을 행할 때, 이 행렬 곱셈 (matrix multiplicaiton) 알고리즘의 복잡도를 big-O 점근 표기법으로 알맞게 표기한 것을 아래 보기에서 선택하세요.

    ① :math:`O(logN)`

    ② :math:`O(N)`

    ③ :math:`O(NlogN)`

    ④ :math:`O(N^2)`

    ⑤ :math:`O(N^3)`

|

참조
====

* https://programmers.co.kr/learn/courses/57
