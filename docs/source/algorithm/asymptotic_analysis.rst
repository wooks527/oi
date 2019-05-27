Asymptotic analysis
===================

==========
Motivation
==========

* "Sweet spot" for high-level reasoning about algorithms.
* Coarse enough to suppress architecture/language/compiler-dependent details.
* Sharp enough to make useful comparisons between different algorithms, especially on large inputs (e.g. sorting or integer multiplication).


===================
Asymptotic analysis
===================

**High-level idea**

* Suppress constant factors and lower-order terms
* Constant factors are too system-dependent
* Lower-order terms are irrelevant for large inputs

**Example**

* Equate 6nlogn + 6 with just nlogn
* Running time is O(nlogn), where n = input size

**Time complexity**

* Asymptotic analysis의 다른 표현으로 보임
* 시간복잡도 분석은 입력크기를 기준으로 단위연산을 몇 번 실행하는지 구하는 것이다.
* T(n) = 입력크기 n에 대해서 알고리즘이 단위연산을 실행하는 횟수, 일정 시간복잡도 (= Every-case time complexity)

=========
Examples
=========

**Two loops**
* One loops: O(n)
* Two loops: O(n^2)
* Two nested loops: O(n^2)

**배열의 원소 모두 더하기**
T(n) = n

**교환정렬**
T(n) = (n - 1) + (n - 2) + ... + 1 = (n - 1)n / 2

**행렬곱셈**
T(n) = n x n x n = n^3


====================
big-O, big-Ω, big-Θ
====================

**O (big-O)**

    * 학계에서 시간의 상한을 의미
    * 학계에서는 Θ의 의미와 가까움
    * 업계의 추세


**Ω (big-Ω)**

    * 학계에서 시간의 하한을 의미


**Θ (big-Θ)**

    * 학계에서 Ω와 O 둘 다를 의미
    * 알고리즘의 수행시간이 Ω(N)이면서 O(N)이라면, Θ(N)이라고 할 수 있음

**o (little-o)**

    * Definition: T(n) = o(f(n)) if and only if for all constants c > 0, there exists a constant n0 such that T(n) <= cf(n), ∀n >= n0


===================
Examples of claims
===================

**Example #1**

* Claim: 2^(n+10) = O(2^n)
* Proof:

**Example #2**

* Claim: 2^(10n) ≠ O(2^n)
* Proof:

**Example #3**

* Claim: for every pair of (positive) functions f(n), g(n), max{f, g} = Θ(f(n) + g(n))
* Proof:


=================================================================
최선 (Best-case), 최악 (Worst-case), 평균 (Average-case) 시간복잡도
=================================================================

**최선 시간복잡도**

    * ?(n) = 입력크기 n에 대해 알고리즘이 실행할 단위연산의 최대 횟수


**최악 시간복잡도**

    * W(n) = 입력크기 n에 대해 알고리즘이 실행할 단위연산의 최대 횟수


**평균 시간복잡도**

    * A(n) = 입력크기 n에 대해 알고리즘이 실행할 단위연산의 평균 횟수 (기대치)


======
Tips
======

**상수항은 무시하라**

    * O(N)이 O(2N)보다 더 좋은 표기법


**지배적이지 않은 항은 무시하라**

.. figure:: img/bigo_performances.jpeg
    :align: center
    :scale: 40%


    * O(N^2+N) → O(N^2)
    * O(N+logN) → O(N)
    * O(5*2^N + 1000N^100) → O(2^N)


**여러 부분으로 이루어진 알고리즘: 덧셈 vs. 곱셈**

    * 알고리즘이 A 일을 모두 끝마친 후에 B 일을 수행하는 경우 → O(A+B)
    * 알고리즘이 A 일을 할 때마다 B 일을 수행하는 경우 → O(A*B)


**상환 시간**

    * P.67

 
**logN 수행 시간**

    * 이진 탐색, 이진 탐색 트리의 탐색
    * P.68, P.806 (로그의 밑)


**재귀적으로 수행 시간 구하기**

    * 아래 예제는 O(2^N)
    * 2^0 + 2^1 + ... + 2^N = 2^(N+1) - 1

Example::

    int f(int n) {
        if (n <= 1) return 1;
        return f(n-1) + f(n-1)
    }


===========
References
===========

* https://www.coursera.org/learn/algorithms-divide-conquer
* 알고리즘 기초 Foruth Edition (Foundations of algorithms), Richard Neapolitan, Kumarss Naimipour, 도경구 역
* 코딩 인터뷰 완전 분석, 게일 라크만 맥도웰 지음, 이창현 옮김