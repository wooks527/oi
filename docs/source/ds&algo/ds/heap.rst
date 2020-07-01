=====
Heap
=====

힙 (Heap)은 최대/최소 원소를 빠르게 찾을 수 있게 만들어진 자료구조이다. 힙은 Max heap과 Min heap이 있다. 그리고 크게 힙 구성 (Heapify), 삽입 (Insert), 삭제 (Remove) 3개의 연산으로 구성되어 있고, 각각의 복잡도는 :math:`O(nlogn),` :math:`O(logn),` :math:`O(logn)` 이다.

힙은 완전 이진 트리 (Complete binary tree)이고, 배열을 이용하여 구현 가능하다. 힙은 정렬 (Heap sort)나 우선 순위 큐 (Priority queue) 등에 응용될 수 있다.

Python은 heapq 모듈과 Queue 모듈의 PriorityQueue 클래스을 통해 heapq를 제공한다. 둘 모두 minheap으로 구현되어 있어, 가장 앞에 있는 원소가 가장 작은 원소다. 하지만 PriortyQueue는 클래스이고, heapq는 모듈이다. 예를 들어, 힙에 데이터를 넣으려면, PriorityQueue에선 객체를 생성하고 메소드를 불러야 하지만 heapq는 객체를 생성하지 않으며, heapify(리스트 객체)처럼 함수를 호출해 리스트를 힙 형태로 소팅한다.

그렇다면 어떤 것을 사용해야 할 지 고민된다. heapq와 PriorityQueue 중에서는 heapq가 더 빠르며, 데이터 삽입 시 속도 차이가 약 10배 정도 난다.

Heap은 힙은 데이터가 지속적으로 정렬돼야 하며, 데이터의 삽입/삭제가 빈번하게 일어날 때 사용한다. 그리고 다음이 heapq와 PriorityQueue의 Time complexity이다.

=========== ============================
Operation   Time Complexity (Worst case)
=========== ============================
Get Item    O(1)
Insert Item O(logn)
Delete Item O(logn)
Search Item O(n)
=========== ============================


heapq
======

heapify
********

heapify는 리스트를 힙정렬하는 함수이고, Time complexity는 :math:`O(n)` 이다.

.. code-block:: python

    import heapq

    my_list = [13, 2, 1, 5, 10]
    heapq.heapify(my_list)

    # 가장 작은 원소인 1이 가장 앞으로 왔습니다.
    my_list


heappop
********

heappop은 가장 작은 원소를 빼내고 나머지 원소가 힙을 유지하도록 정리한다. heappop을 사용하기 전에 리스트가 힙 정렬되어 있는지 확인해야 올바른 결과가 나온다.

.. code-block:: python

    import heapq
    my_list = [13, 2, 1, 5, 10]
    heapq.heapify(my_list)

    # 가장 작은 원소인 1이 리턴됩니다. my_list의 길이가 하나 줄어듭니다.
    ret_val = heapq.heappop(my_list)

    print("리턴된 값:", ret_val)
    print("남은 원소:", my_list)

참고로, 리스트를 변형하지 않으면서 가장 작은 값을 알고 싶은 경우에는 인덱스를 이용하여 리스트에 접근하면 된다.

# 가장 작은 원소에 접근 예시

.. code-block:: python

    import heapq
    my_list = [13, 2, 1, 5, 10]
    heapq.heapify(my_list)

    # heappop을 하지만, 맨 앞 원소가 최솟값임은 변하지 않음
    while my_list:
        print("리스트의 맨 앞 원소:", my_list[0])
        heapq.heappop(my_list)


heappush
*********

heappush 함수는 힙 정렬된 리스트의 힙 상태를 유지하면서 데이터를 삽입한다. 역시나 사용 전에 리스트가 힙 정렬되어 있는지 확인해야 한다.

* 현재의 min 값보다 작은 값 삽입

.. code-block:: python

    import heapq
    my_list = [13, 2, 1, 5, 10]
    heapq.heapify(my_list)

    # -1 삽입
    heapq.heappush(my_list, -1)

    # 가장 작은 원소인 -1이 가장 앞에 위치
    print("남은 원소:", my_list)

* 현재의 min 값보다 큰 값 삽입

.. code-block:: python

    import heapq
    my_list = [13, 2, 1, 5, 10]
    heapq.heapify(my_list)

    # 100 삽입
    heapq.heappush(my_list, 7)

    # 기존에 가장 작았던 원소가 계속 앞에 위치
    print("남은 원소:", my_list)


PriorityQueue
==============

put_nowait
***********

.. code-block:: python

    # 데이터 삽입 예시
    from queue import PriorityQueue

    my_list = [13, 2, 1, 5, 10]
    pq = PriorityQueue()

    # 데이터 삽입
    for val in my_list:
        pq.put_nowait(val)
        
    # queue 멤버 변수를 통해 현재 어떤 값이 들어있는지 확인 가능
    print(pq.queue)


get_nowait
***********

데이터를 가져올 때 get_nowait 메소드 이외에 get 메소드가 있다. 하지만 get_nowait를 사용하는 이유는 OOO이다.

.. code-block:: python

    # 데이터 접근 예시
    from queue import PriorityQueue

    my_list = [13, 2, 1, 5, 10]
    pq = PriorityQueue()
    for val in my_list:
        pq.put_nowait(val)

    # 가작 작은 값 가져오기
    print(pq.get_nowait())


qsize
******

.. code-block:: python

    from queue import PriorityQueue

    my_list = [13, 2, 1, 5, 10]
    pq = PriorityQueue()

    for val in my_list:
        pq.put_nowait(val)
        print('큐 크기:', pq.qsize())

        
empty
******

.. code-block:: python

    from queue import PriorityQueue

    pq = PriorityQueue()

    print("큐가 비었나?:", pq.empty())

    my_list = [13, 2, 1, 5, 10]
    for val in my_list:
        pq.put_nowait(val)

    print("큐가 비었나?:", pq.empty())


heapq vs. PriorityQueue
========================

heapq 모듈에 비해서 PriorityQueue 클래스의 속도는 조금 떨어진다. 실제로 힙에 데이터를 100,000번 넣었을 때,

.. code-block:: python

    import heapq
    from queue import PriorityQueue
    import timeit
    import random

    random.seed(0)

    dataset = list(range(0,100000))
    random.shuffle(dataset)

* heapq 모듈의 heappush: 약 40ms

.. code-block:: python

    def heapq_perform(dataset):
    lst = []
    for data in dataset:
        heapq.heappush(lst, data)

    # heapq
    print("heapq를 사용했을 때:")
    %timeit heapq_perform(dataset)

* PriorityQueue 클래스의 put_nowait: 300ms

.. code-block:: python

    def pqclass_perform(dataset):
        pq = PriorityQueue()
        for data in dataset:
            pq.put_nowait(data)

    print("PriorityQueue를 사용했을 때:")
    %timeit -n 10 pqclass_perform(dataset)


heap vs. list
**************

앞서 언급한 것처럼 heapq는

* 데이터가 지속적으로 정렬돼야 함
* 데이터의 삽입/삭제가 빈번하게 일어남

과 같은 상황에서 사용한다. 추가로 이 때, 리스트보다 heapq가 좋은 이유는 다음 예제를 통해 알 수 있다.

-----------------------------
예시: 반복적 가장 작은 값 추출
-----------------------------

"PUSH X" 명령이 들어오면 자료구조에 데이터를 넣고, "POP None" 명령이 들어오면 데이터 중 가장 작은 값을 뺀다.

.. code-block:: python

    random.seed(0)

    def build_comands(n=100000):
        '''PUSH, POP 명령을 담은 리스트를 만드는 함수'''
        commands = []
        num_inserted = 0
    
        for _ in range(n):
            operation = 'PUSH' if num_inserted == 0 else random.choice(['PUSH', 'POP'])
            if operation == 'PUSH':
                num_inserted += 1
                number = random.randint(0,1000000) 
            else:
                num_inserted -= 1
                number = None
            commands.append((operation, number))
    
        commands.extend([('POP', None)] * (num_inserted - 1))
        return commands

    commands = build_comands()
    print("commands[:5] => ", commands[:5])

* heapq: 32ms

.. code-block:: python

    def heapq_perform(commands):
        hq = []
        for [operation, value] in commands:
            if operation == 'PUSH':
                heapq.heappush(hq, value)
            else:
                heapq.heappop(hq)

    %timeit -n 10 heapq_perform(commands)

* PriorityQueue 클래스의 put_nowait: 약 233ms

.. code-block:: python

    def list_perform(commands):
        lst = []
        for [operation, value] in commands:
            if operation == 'PUSH':
                lst.append(value)
            else:
                lst.sort(reverse=True)
                lst.pop()
        
    %timeit -n 10 list_perform(commands)

여기서 n이 커질수록 두 모듈의 성능 차이는 급격하게 늘어날 수 있다.
