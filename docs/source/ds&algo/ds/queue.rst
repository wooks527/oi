======
Queue
======

Queue는 자료의 선입선출, FIFO(First-In-First-Out)을 보장하는 자료구조이다. Python에서는 collections 모듈의 deque 또는 queue 모듈의 Queue 클래스를 통해 큐 자료구조를 제공한다.


deque
======

deque은 스택과 큐를 합친 자료구조이고, 다음과 같은 메소드를 제공한다.

=========================== ============================================================
메소드                       설명
=========================== ============================================================
deque([iterable[, maxlen]]) 초기화 함수이고, iterable(리스트 등)을 인자로 건네면 이를 deque화 해줌
append(x)                   x를 덱의 오른쪽에 삽입합니다.
popleft()                   덱의 가장 왼쪽에 있는 원소를 덱에서 제거하며, 그 값을리턴합니다.
clear()                     모든 원소를 지웁니다.
=========================== ============================================================

* 참고: 스택과 달리 큐를 list로 이용하지 않는 이유

    * 스택에서 list.append와 list.pop()을 이용했던 것 처럼 list.append와 list.pop(0)을 이용하면 리스트를 큐처럼 사용할 수 있다.
    * 허나 pop()의 time complexity는 O(1)인 반명 pop(0)의 time complexity는 O(N)이기 때문에 시간이 오래걸린다.
    * 따라서 시간복잡도를 고려해 리스트는 큐로 사용하지 않는다.


Init
*****

.. code-block:: python

    from collections import deque

    # 빈 큐 만들기
    deque1 = deque()

    # 원소가 있는 큐 만들기
    deque2 = deque([1, 2, 3])

    # 큐 최대 길이 명시하기(원소를 이보다 많이 넣으면 maxlen이 자동 갱신됨)
    deque3 = deque(maxlen=5)


append
*******

.. code-block:: python

    my_deque = deque()
    my_deque.append(3)

    print(my_deque)


popleft
*******

.. code-block:: python

    my_deque = deque([1,2,3])

    while my_deque:
        print("{}을/를 pop했습니다".format(my_deque.popleft()))


clear
******

.. code-block:: python

    my_deque = deque([1,2,3])

    print("전:", my_deque)
    my_deque.clear()
    print("후:", my_deque)


원소 수
******

.. code-block:: python

    my_deque = deque([1,2,3], maxlen=5)
    print(len(my_deque))


Queue
======

Queue 모듈의 큐는 multi-consumer queue를 제공하고, 따라서 threaded programming을 자주 쓰며 이로 인해 deque에 비해 속도가 느리다. 다음은 Queue 클래스가 제공하는 메소드와 멤버 변수이다.

================= ============= ==================================
구분               이름           하는 일
================= ============= ==================================
메소드              qsize()       들어있는 데이터의 길이를 리턴
메소드              empty()       큐가 비었는지 검사
메소드              put(item)     item을 큐에 삽입
메소드              get()         큐에서 원소를 제거하고 제거한 원소를 리턴
멤버 변수           queue         현재 큐에 들어 있는 데이터
================= ============= ==================================



Init
*****

.. code-block:: python

    # 빈 큐 생성하기
    from queue import Queue

    empty_queue = Queue()
    empty_queue


put
****

Queue에는 원소 N개를 한 번에 넣는 방법은 없고, 데이터 수만큼 삽입 연산을 호출해야 한다.

.. code-block:: python

    # 큐에 데이터 넣기
    from queue import Queue

    my_queue = Queue()
    my_queue.put(3)

    my_queue.queue


get
****

.. code-block:: python

    # 큐에서 데이터 제거하기
    from queue import Queue

    my_queue = Queue()
    my_queue.put(3)

    front = my_queue.get_nowait()

    print(front)
    my_queue.queue


qsize
******

.. code-block:: python

    # 큐에 들은 원소 수 알아내기
    from queue import Queue
    my_queue = Queue()

    for val in range(5):
        my_queue.put(val)
        print('큐 크기:', my_queue.qsize())
