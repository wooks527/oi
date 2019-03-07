Queue
======

Queue (큐)는 나중에 들어온 데이터가 먼저 나가는 구조 (FIFO: First-In First-Out)를 가지는 자료구조


============
Terminology
============

* Rear, Front


=========================
Abstract Data Type (ADT)
=========================

* Object: n 개의 element형의 요소들의 순서있는 컬렉션
* 연산:
    * create() ::= 큐 생성
    * init(q) ::= 큐 초기화
    * is_empty(q) ::= 큐가 비어있는지 검사
    * is_full(q) ::= 큐가 가득 찼는지 검사
    * enqueue(q, e) ::= 큐의 뒤에 요소 추가
    * dequeue(q) ::= 큐의 앞에 있는 요소를 반환한 다음 삭제
    * peek(q) ::= 큐에서 삭제하지 않고 앞에 있는 요소를 반환


=======
Types
=======

* Linear queue
* Circular queue
* Linked queue
* Deque (Double-ended queue)
* `Priority queue <https://oi.readthedocs.io/en/latest/algorithms/data_structure/queue/priority_queue.html>`_


===========
Utilization
===========

**Buffer**

**Simulation**


**References**
    * C언어로 쉽게 풀어쓴 자료 구조, 천인국 저