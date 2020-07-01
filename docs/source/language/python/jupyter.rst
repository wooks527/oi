Jupyter
========

============
Multi kernel
============

**Python3.5 Kernel 추가**

    * /usr/local/share/jupyter/kernels에서 python3.5 폴더 생성
    * kernel.json 파일 생성 후 아래 내용 추가
    * 만약 실행이 안된다면 pip로 notebook을 설치하기 (python3.5 -m pip install notebook)

::

    {
        "language": "python",
        "display_name": "Python 3.5",
        "argv": [
            "/usr/bin/python3.5",
            "-m",
            "IPython.kernel",
            "-f",
            "{connection_file}"
        ]
    }



:h2:`출처`

* https://blog.nacyot.com/articles/2015-05-08-jupyter-multiple-pythons/
