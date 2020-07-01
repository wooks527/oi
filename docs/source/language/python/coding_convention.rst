==================
Coding convention
==================

Coding convention에는 여러가지 방법이 있다. 여기에서는 대표적인 Guide인 Python Developer's Guide와 Google Python Style Guide를 살펴보려고 한다.


Python Developer's Guide
=========================

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

* `PEP8 <https://www.python.org/dev/peps/pep-0008/#id47>`_ 기준으로 시퀀스가 비어있는지 여부를 판단할 경우, 리스트명만 사용하기를 권장한다.

* 2차원 행렬에서 행과 열을 가져올 때, 단순히 i와 j를 사용하는 것보다 r과 c를 활용하는 것이 더 가독성이 좋다.


Google Python Style Guide
==========================

* Comments and Docstrings

    * `GitHub, Google Python Style Guide <https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings>`_
    * `Google Python Style Guide <http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings>`_


Others
=======

* `Real Python, Documenting Python Code: A Complete Guide <https://realpython.com/documenting-python-code/>`_
* 
