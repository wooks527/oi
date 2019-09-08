==================
Coding convention
==================

다양한 Coding convetion이 존재하는데 한 번에 다 정리하기 어렵기 때문에 여기에 하나씩 정리하고자 한다.

* Public 하지 않은 메소드나 인스턴스 변수의 이름 앞에는 언더스코어를 하나 붙인다 (`PEP8 <https://www.python.org/dev/peps/pep-0008/#id47>`_).

* Function 내부에 Function을 만드는 경우,

    * 다양한 이름으로 불림, Closure / Inner function / Nested function
    * 클로저를 사용하면 함수 밖에서 호출된 변수에 접근 가능 (?)
    * 내부 함수를 사용하면서 Global scope에 대한 관리가 용이함
    * 검수, 데코레이터, 콜백 함수 구현 등에 사용될 수 있음

* Docstring conventions (`PEP257 <https://www.python.org/dev/peps/pep-0257/>`_)

    * Docstring을 사용하면 help 함수의 인자로 전달 시 기능 사용 설명서로 출력됨

    * 현재는 아래와 같은 Docstring convention을 사용하고 있음

    .. code-block:: python

        def function(a, b):
            ''' This is a function.
            Args:
                a (str): string
                b (int): number
            Returns:
                c (list): a list consists of a string and a number
            '''
            c = [a, b]
            return c

    * 추후에는 PEP257 문서를 읽고 정리해보고자 함
