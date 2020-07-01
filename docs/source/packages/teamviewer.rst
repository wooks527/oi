===========
Teamviewer
===========

Troubleshooting
================

* 패키지 의존 문제로 설치가 되지 않을 때

    * apt로 --fix-broken 옵션을 추가하여 설치해서 해결함

    ::

        sudo apt install ./teamviewer_15.5.3_amd64\ .deb --fix-broken

    * 참조

        * `How to Install TeamViewer on Ubuntu 18.04 <https://linuxize.com/post/how-to-install-teamviewer-on-ubuntu-18-04/>`_
        * `Dependency is not satisfiable: libqt5gui5 (<=5.5) Error <https://community.teamviewer.com/t5/Linux/Dependency-is-not-satisfiable-libqt5gui5-lt-5-5-Error/td-p/24811>`_
