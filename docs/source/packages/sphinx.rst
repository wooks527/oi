=======
Sphinx
=======

Sphinx는 Python으로 만든 Software project를 Documentation 할 때 사용하는 도구이고, 마크업 언어 (Markup language) 중 하나인 reStructuredText를 사용하여 Documenation 할 수 있다.

설치
=====

설치하기 전에 Anaconda가 설치되어 있어야 한다.

* `다운로드 페이지 <https://www.anaconda.com/distribution/#download-section>`_

Sphinx 설치는 conda나 pip를 이용해서 할 수 있다.

::

    conda install sphinx
    
::

    pip install -U sphinx

Sphinx 설치 후 추가로 설치한 Theme이나 패키지들을 설치한다.

::

    pip install sphinx_rtd_theme

보통 본인이 추가한 라이브러리는 requirements.txt 파일에 저장되어 있다.

::

    pip install sphinxcontrib-contentui
    pip install nbsphinx
    pip install sphinxemoji

여기까지 설치하면 Sphinx로 만든 문서를 Build 할 수 있다. Build는 docs 폴더 안에서 할 수 있다.

:h3:`설치 관련 이슈`

Windows에 Sphinx를 설치하는 경우 sphinxemoji에서 encoding 에러가 발생한다. 그래서 로컬의 sphinxemoji.py에서 json파일을 로드할 때 인코딩을 바꿔줘야 한다. Python이 설치되어 있는 경로에 따라 그 위치가 다르다. 본인은 Anaconda에 설치하여 그 위치가 

.. rst-class:: centered

    C:\\Users\\wooks\\Anaconda3\\lib\\site-packages\\sphinxemoji\\sphinxemoji.py

이다. 그러면 에러가 나지 않고 Build 할 수 있을 것이다.


Configuration 설정
===================

Read the Docs supports configuring your documentation builds with a YAML file. The Read the Docs file must be in the root directory of your project.

Below is an example YAML file which may require some changes for your project’s configuration:

.. code-block::

    # .readthedocs.yml
    # Read the Docs configuration file
    # See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

    # Required
    version: 2

    # Build documentation in the docs/ directory with Sphinx
    sphinx:
    configuration: docs/conf.py

    # Build documentation with MkDocs
    #mkdocs:
    #  configuration: mkdocs.yml

    # Optionally build your docs in additional formats such as PDF and ePub
    formats: all

    # Optionally set the version of Python and requirements required to build your docs
    python:
    version: 3.7
    install:
        - requirements: docs/requirements.txt


:h2:`출처`

* `Sphinx documentation <https://www.sphinx-doc.org/>`_
* `ReadtheDocs documentation, Configuration File <https://docs.readthedocs.io/en/stable/config-file/v2.html>`_
