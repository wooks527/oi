윌콕슨 부호순위 검정 (Wilcoxon signed rank test)
================================================

F. Wilcoxon에 의해 제안된 비모수 통계검정 방법이다.
자료의 순서를 사용하여 자료의 중위수(median)가 0 인지를 검정한다.
Wilcoxon signed-rank test는 "+","-"의 부호를 무시하고 절대값으로 순위를 구한 후, 그 다음 절차는 순위에 "+"와 "-"를 부여한다.
각 자료의 쌍은 부호화된 순위 (signed rank)를 갖게 된다.
이런 의미에서 Wilcoxon 검정은 Wilcoxon 부호 순위검정 (Wilcoxon signed rank teset)이라고 불리기도 한다.


========
예제
========

Data.csv : 30명을 대상으로 약 복용 전후의 체중 변화를 측정하여 약이 체중 감소에 영향이 있는지를 조사한 데이터이다.

=====  =====  =====
rank   pre    post
=====  =====  =====
1      80.5   82.3
2      84.8   85.5
...    ...    ...
30     87.5   86.8
=====  =====  =====

::

    DATA = read.csv(“Data.csv”)
    with(DATA,shapiro.test(post-pre))
    Data: post – pre
    W=0.876, p-value=0.00784

::

    귀무가설 H0: 약 복용 전후 몸무게 차이가 정규분포를 따른다
    대립가설 H1: 약 복용 전후 몸무게 차이가 정규분포를 따르지 않는다.
    검정통계량: W=0.876
    P-value: 0.00784 < 0.05
    결정: 약 복용 전후 몸무게 차이가 정규분포를 따르지 않는다.
      -> Wilcoxon Signed-Rank Test 수행

::

    with(DATA, wilcox.test(post-pre))
    data: post – pre
    V=303.4, p-value=0.064

::

    귀무가설 H0: 약 복용 전후 몸무게 차이의 median은 0이다.
    대립가설 H1: 약 복용 전후 몸무게 차이의 median은 0이 아니다.
    검정통계량: V=303.4
    P-value: 0.064 > 0.05
    결정: 약 복용 전후 몸무게 차이가 없다.


**Reference**
    * `人CoDOM <http://www.incodom.kr/R%ED%99%9C%EC%9A%A9/Wilcoxon_Signed-Rank_Test>`_
