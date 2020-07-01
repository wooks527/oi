======
Python
======

Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

.. toctree::
    :maxdepth: 1

    pros_and_cons
    coding_convention
    time_complexity
    parallel_processing
    pandas/pandas
    numpy/numpy
    special_tips
    peps/peps
    jupyter
    anaconda


Others
=======

Numbers
********

* round

::

>>> round(44.4512347, 2)
14.45


File I/O
*********

* readline()

    * 코드

    ::

        f = open("C:/doit/새파일.txt", 'r')
        line = f.readline()
        print(line)
        f.close()

    * 참조

        * `WikiDocs, 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법 <https://wikidocs.net/26>`_

* readlines()

    * 기본적인 방법

        * 코드

        ::

            f = open("C:/doit/새파일.txt", 'r')
            lines = f.readlines()
            for line in lines:
                print(line)
            f.close()

        * 참조

            * `WikiDocs, 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법 <https://wikidocs.net/26>`_

    * Remove '\n' from readlines

        * 코드

        ::

            >>> filelist = open("file.txt").readlines()
            ['a\n', 'b\n', 'c\n', 'd\n']

            >>> open("file.txt").read().splitlines()
            ['a', 'b', 'c', 'd']

        * 참조

            * `Sany's Linux and Open Source Blog, Python – remove newline from readlines <https://viewsby.wordpress.com/2014/08/28/python-remove-newline-from-readlines/>`_

* listdir()

    * 코드

    ::

        from os import listdir
        from os.path import isfile, join
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    * 참조

        * `StackOverflow, <https://stackoverflow.com/a/3207973>`_


:h2:`Reference`

* `Wikipedia <https://en.wikipedia.org/wiki/Python_(programming_language)>`_
