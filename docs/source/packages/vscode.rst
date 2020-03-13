========
VS Code
========

사용법
=======

VSCode로 Docker container 코드 수정하기
***************************************

* Extension 설치

    * Remote Development를 검색하여 설치

* VSCode와 Container 연결

    * ``F1`` 키 또는 ``Ctrl`` + ``Shift`` + p 를 이용하여 커맨드 라인을 입력할 수 있게 만들기
    * Remote-Containers: Attach to Running Container... 를 선택하면 해당 Container로 연결됨

* 개발하기 위한 폴더를 선택하면 해당 소스코드를 VSCode에서 볼 수 있음

:h3:`참조`

* `tech_curioso, VSCode로 Docker Container에 Remote로 연결하기 <https://curioso365.tistory.com/100>`_

원격에서 VSCode로 다른 코드 수정하기
***********************************

* `생각의 자취, 원격서버 vscode로 연결해서 작업하기 <https://evols-atirev.tistory.com/28>`_


Troubleshooting
================

* Docker container 코드 실행 시 Locale 문제

    * 코드

    ::

        apt-get install locales
        vi /etc/default/locale

    ::

        # 아래 내용 추가하기
        LANG=en_US.UTF-8
        LC_ALL=en_US.UTF-8

    ::

        # 위 작업으로 안되면 아래 명령어 실행 (158 ￫ 3)
        sudo dpkg-reconfigure locales

    * 참조

        * `I.K.Picture & IT Info., pip를 통한 설치 시 unsupported locale setting 에러 <http://blog.engintruder.com/176>`_
        * `StackExchange, Can't install locales [closed] <https://unix.stackexchange.com/questions/223533/cant-install-locales>`_

* 원하는 Python interpreter로 컴파일되지 않을 때

    * ``Ctrl`` + ``Shift`` + ``P`` 로 Python: Select Interpreter를 선택한 후 원하는 Python을 선택할 수 있음
    * 참조: `Visual Studio Code > Docs, Using Python environments in VS Code <https://code.visualstudio.com/docs/python/environments>`_
