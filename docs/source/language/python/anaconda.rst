=========
Anaconda
=========

설치
=====

Ubuntu
********

Anaconda 공식 홈페이지 (`Link <https://www.anaconda.com/distribution/>`_)에서 설치파일을 다운로드 받아 :code:`bash Anaconda3-2019.10-Linux-x86_64.sh` 로 실행하면 설치할 수 있다.


Windows
*********

설치파일을 다운로드 받아 설치하면 된다.


가상 환경
==========

* 가상 환경 만들기

    * ``conda create -n [가상환경명] python=[버전]``

* 가상 환경 시작/종료

    * ``conda activate [가상환경명]``
    * ``conda deactivate``

* 가상 환경 리스트 출력

    * ``conda env list``

* 가상 환경 제거하기

    * ``conda env remove -n [가상환경명]``


:h2:`참조`

* `reStructuredText & Sphinx » reST & Sphinx Reference » Inline Code & Textroles <https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/WritingReST/InlineCode.html>`_
