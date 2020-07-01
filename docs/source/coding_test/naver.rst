======
Naver
======

구글에서 네이버 코딩 테스트 후기로 검색하여 여러 글을 봤지만, 코딩 테스트에 대한 자세한 내용은 없었다. 그래서 각 블로그에서 정리한 내용으로 어떻게 준비해야 할 지 정리해 보려고 한다.

2019년 네이버 코딩 테스트에서는 프로그래머스 플랫폼에서 3문제가 나왔고, 제한 시간은 2시간이었다고 한다. 여기까지는 평범한듯 하다. 하지만 문제는 다른 테스트와 다르게 테스트 케이스 통과 여부를 알 수 없다고 한다... 우선, 나온 문제를 요약하면 아래와 같다.

* 1번 문제

    * 문자열 큐
    * 임시 메일 보관함을 구현하는 문제로, 메일 송수신 및 사용자의 명령 레코드가 인풋으로 주어졌고 이 레코드대로 진행된 결과를 출력해야 한다. RECEIVE 레코드는 임시 보관함에 수신된 메일들을 저장하고, SAVE는 현재 임시보관함에 있는 메일 전부를 일반메일함에 옮겨 저장한다. REMOVE는 임시 보관함에 가장 최근 수신된 메일을 삭제한다.

* 2번 문제

    * 수열 문제
    * 연속된 2개 이상의 숫자들을 더하여 나올 수 있는 모든 숫자를 오름차순으로 정리한 수열이 주어졌다. 이 수열에서 N번째 수를 출력한다.

* 3번 문제

    * 위상 정렬 문제
    * 로이네 집에서 송편을 만드는 문제

기본적인 문자열 다루는 문제나 수학 관련 문제 및 정렬 문제가 나오는 것으로 보인다.

다른 블로그에서 어떤 유형에 문제가 나오는지 추측한 내용이 있는데, 아래 3가지 유형이라고 한다.

* 주사위의 현 상태 배열을 최소한의 이동을 통해 같은 면으로 통일하는 문제
* 이진 트리와 set을 활용해 중복되지 않은 노드들로 이루어진 최대 height을 구하는 문제
* 겨울과 여름의 경계선을 구하는 전형적인 DP 문제

하지만 정보가 많이 없기 때문에 기초적인 문제들인 스택, 큐, 해시, 문자열, 이분탐색, 완전탐색 등에 집중하는 것이 좋다고 언급했다. 결국 최소한 프로그래머스에 코딩테스트 연습 문제들 중 코딩테스트 고득점 Kit에 해당하는 문제들은 꼭 풀어봐야겠다 (`코딩테스트 고득점 Kit <https://programmers.co.kr/learn/challenges>`_).

그리고 여러 블로그들을 보다보면 네이버 코딩테스트가 다른 기업에 비해서는 조금 쉬운편이라고 한다. 절대 마음의 위로가 되지 않는 이야기지만...


관련 문제 풀이
==============

* 문자열 문제

    * `사전순 부분문자열 <https://github.com/hwkim89/programming/blob/master/programmers/ds/stack/alphabetical_part_string.ipynb>`_
    * `괄호 변환 <https://github.com/hwkim89/programming/blob/master/programmers/coding_test/kakao_blind_recruitment/2020/change_parenthesis.ipynb>`_
    * `불량 사용자 <https://github.com/hwkim89/programming/blob/master/programmers/coding_test/kakao_intern_test/2019/bad_user.ipynb>`_
    * `단어 변환 <https://github.com/hwkim89/programming/blob/master/programmers/algo/bfs_dfs/word_change.ipynb>`_

* 수학 문제

    * `다음 큰 숫자 <https://github.com/hwkim89/programming/blob/master/programmers/number/next_bigger_number.ipynb>`_
    * `숫자의 표현 <https://github.com/hwkim89/programming/blob/master/programmers/number/representation_of_number.ipynb>`_
    * `최댓값과 최솟값 <https://github.com/hwkim89/programming/blob/master/programmers/number/max_and_min.ipynb>`_
    * `최솟값 만들기 <https://github.com/hwkim89/programming/blob/master/programmers/number/make_min_num.ipynb>`_
    * `피보나치 수열 <https://github.com/hwkim89/programming/blob/master/programmers/number/fibonacci_number.ipynb>`_

* 위상 정렬 문제

    * `줄 세우기 <https://github.com/hwkim89/programming/blob/master/baekjoon/sort/2252_line_up.ipynb>`_


참조
====

위 내용은 아래 링크에서 작성한 내용을 기반으로 작성했으므로, 조금 더 자세한 내용이 필요한 경우 아래 링크에서 다시 확인하자.

* `나만의 일기장 <https://blog.naver.com/PostView.nhn?blogId=san9407&logNo=221655897462>`_
* `Chick's blog <https://yoonjinxd.github.io/etc/2019/10/02/2019-Naver-%EC%98%A8%EB%9D%BC%EC%9D%B8-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%A6%AC%EB%B7%B0.html>`_
* `DEVLOG <https://deepwelloper.tistory.com/116>`_
