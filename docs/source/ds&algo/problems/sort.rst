=====
Sort
=====

가장 큰 수
=========

* 문제

    * https://programmers.co.kr/learn/courses/30/lessons/42746

* 해결법

    * 방법 1
    
        * 빈 문자열로 수를 초기화한다.
        * 가장 크게 만들 수 있는 수를 고른다.
        * 그 수를 현재 수에 이어 붙인다.
        * 모든 수를 다 사용할 때까지 반복한다.

    * 방법 2
    
        * 빈 문자열로 수를 초기화한다.
        
        * 수의 목록을 (크게 만드는 것 우선으로) 정렬한다.

            * 크게 만드는 수의 기준

                * 34 vs. 343

                    * 수의 목록이 잘 정렬되어 있다면,

                        * 34 뒤에 올 수 있는 수들 중 가장 큰 조합은 34343434...
                        * 343 뒤에 올 수 있는 수들 중 가장 큰 조합은 343343343...

                .. figure:: ../img/problems/sort/basis_of_bigger_numberz.png
                    :align: center
                    :scale: 40%

        * 목록에서 하나씩 꺼내어 현재 수에 이어 붙인다.
        
        * 모든 수를 다 사용할 때까지 반복한다.

* 구현 (방법 2)

    * 대소 관계 비교를 위한 기준을 마련
    * 이것을 이용하여 주어진 배열을 정렬
    * 정렬된 배열을 이용하여 문자열 표현을 완성

* 코드

    * `가장 큰 수 <https://github.com/hwkim89/programmers/blob/master/sort/the_biggest_number.ipynb>`_

