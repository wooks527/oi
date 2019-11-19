======
Stack
======

Stack은 가장 나중에 들어온 자료가 가장 먼저 처리되는 LIFO(Last-In-First-Out) 자료구조이다.

다음은 Python list로 구현한 스택이다.

.. code-block:: python

    class Stack(list):
        push = list.append
        
        def is_empty(self):
            if not self:
                return True
            else:
                return False

        def peek(self):
            return self[-1]


Python에서는 list를 Stack과 유사하게 사용할 수 있고, 다음과 같은 Operation을 사용할 수 있다.

==========  ===============  ===============================
Operation   구현              Time Complexity - Average Case
==========  ===============  ===============================
Pop item     my_list.pop     O(1)
Push item    my_list.append  O(1)
==========  ===============  ===============================


Init
=====

.. code-block:: python

    stack = []


push
=====

append는 리스트 (스택)의 가장 마지막에 원소를 추가해준다.

.. code-block:: python

    stack = [1, 2, 3]
    stack.append(4)


pop
====

pop은 리스트 (스택)의 가장 마지막 원소를 제거하고 그 결과를 반환한다.

.. code-block:: python

    stack = [1, 2, 3]
    top = stack.pop()


top
====

리스트 (스택)의 가장 위 원소를 확인하는 경우, [-1] 인덱스를 활용할 수 있다.

.. code-block:: python

    stack = [1, 2, 3]
    top = stack[-1]

