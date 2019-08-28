=====
Hash
=====

완주하지 못한 선수
===============

* 문제

    * `Programmers > 코딩테스트 연습 > 해시 (Hash) > 완주하지 못한 선수 <https://programmers.co.kr/learn/courses/30/lessons/42576>`_

* 자료구조와 알고리즘의 선택

    * 만약 이름 대신 번호가 주어졌다면, 최대 크기 10만에 해당하는 선형 배열을 이용할 수 있다.
    * 하지만 영어 이름이 주어졌기 때문에 배열을 사용하면 :math:`26^{26}` 크기의 배열을 사용해야 하므로 불가능하다.
    * 이처럼 인덱스 대신 문자열을 이용하여 원소를 찾으려고 하는 경우 해시가 유용하다.
    * 참고로 사전의 원소들은 해시를 이용해 :math:`O(1)` 시간에 접근 가능하다.

    .. figure:: ../img/problems/hash/hash_ex.png
        :align: center
        :scale: 40%

* 코드

    * `Github <https://github.com/hwkim89/programmers/blob/master/hash/incomplete_player.ipynb>`_
