=============
Special tips
=============

* bool은 int의 Sub class이다.

.. code-block:: python

    print(issubclass(bool, int))

* Python에서 무한값을 가져오는 방법들

.. code-block:: python

    # Way 1
    from math import inf as INF

    # Way 2
    INF = float('inf') # Type: <class 'float'>

    # Way 3
    from numpy import inf as INF

* is와 == 연산자의 차이점

    * is는 주소값을 비교하는 연산자이고, ==는 값자체를 비교하는 연산자이다.
    
    * `전지적 송윤섭시점 블로그 <https://tech.songyunseop.com/post/2017/09/python-comparing/>`_
    
    * 참고로 1과 같이 자주 쓰이는 상수는 메모리에 상주되어 있는 것 같다.
        
        * 다음이 이를 설명하는 예시이다.

        .. code-block:: python
        
            >> print(0 + 1 is 1)
            True

            >> print(0 + 10000 is 10000)
            False
