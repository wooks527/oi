Environment
===========

Installation
*************

Python3.5
---------

::

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install python3.5 libpython3.5-dev


**Version management**

update-alternatives --install /usr/bin/python python /usr/bin/python3.5 0


pip
----

**Installation:**

::

    wget https://bootstrap.pypa.io/get-pip.py
    sudo python2 get-pip.py
    sudo pip2 install -U setuptools
    sudo pip2 -m pip install pip --upgrade


**기존에 설치된 패키지를 강제로 재설치 하는 방법:**

::

    pip install --ignore-installed ${PACKAGE_NAME}


Virtual environment
********************

Conda
------

::

    conda create -n python2.7-venv python=2.7 anaconda

    
Reference
*********

* https://songgane.github.io/tips/2016/02/11/ubuntu-update-alternative/
* https://financedata.github.io/posts/faq_pip_packge_fail.html
* http://jkstory-textcube.blogspot.com/2016/02/conda-virtual-environments.html