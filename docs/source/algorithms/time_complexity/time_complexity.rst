Time complexity
================

시간복잡도 분석은 입력크기를 기준으로 단위연산을 몇 번 실행하는지 구하는 것이다.

T(n) = 입력크기 n에 대해서 알고리즘이 단위연산을 실행하는 횟수, 일정 시간복잡도 (= Every-case time complexity)

=========
Example
=========

**배열의 원소 모두 더하기**
T(n) = n

**교환정렬**
T(n) = (n - 1) + (n - 2) + ... + 1 = (n - 1)n / 2

**행렬곱셈**
T(n) = n x n x n = n^3


===========================================
최악 시간복잡도 (Worst-case time complexity)
===========================================

W(n) = 입력크기 n에 대해 알고리즘이 실행할 단위연산의 최대 횟수


=============================================
평균 시간복잡도 (Average-case time complexity)
=============================================

A(n) = 입력크기 n에 대해 알고리즘이 실행할 단위연산의 평균 횟수 (기대치)


**Reference**
    * 알고리즘 기초 Foruth Edition (Foundations of algorithms), Richard Neapolitan, Kumarss Naimipour, 도경구 역