Python
=======

=============
Installation
=============

**Python3.5**

::

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install python3.5 libpython3.5-dev


**PIP**

::

    wget https://bootstrap.pypa.io/get-pip.py
    sudo python2 get-pip.py
    sudo pip2 install -U setuptools
    sudo pip2 -m pip install pip --upgrade

====
pip
====

**기존에 설치된 패키지를 강제로 재설치 하는 방법**

::

    pip install --ignore-installed ${PACKAGE_NAME}


===================
Version management
===================

update-alternatives --install /usr/bin/python python /usr/bin/python3.5 0


======
Conda
=======

**가상환경**

::

    conda create -n python2.7-venv python=2.7 anaconda


================
Time complexity
================

Built-in methods
****************

**String**

=================  ==============================  =============  =====================================================
Operation          Example                         Big-O          Notes
=================  ==============================  =============  =====================================================
split              split()                         O(n)             
=================  ==============================  =============  =====================================================

**List**

=================  ==============================  =============  =====================================================
Operation          Example                         Big-O          Notes
=================  ==============================  =============  =====================================================
slice              list[a:b]                       O(b-a) = O(n)    
sum                sum([1, 2, 3, 4, 5])            O(n)
=================  ==============================  =============  =====================================================

**Numpy**

=================  ==============================  =============  =====================================================
Operation          Example                         Big-O          Notes
=================  ==============================  =============  =====================================================
sum                <array>.sum([1, 2, 3, 4, 5])    O(n)           Faster than built-in sum function (`sum vs. np.sum`_)
=================  ==============================  =============  =====================================================

.. _sum vs. np.sum: https://stackoverflow.com/questions/10922231/pythons-sum-vs-numpys-numpy-sum/10922478

**Counter**

=================  ==============================  =============  =====================================================
Operation          Example                         Big-O          Notes
=================  ==============================  =============  =====================================================
Counter            Counter([1, 2, 3])              O(n)             
most_common        c.most_common(2)                O(nlogn)
=================  ==============================  =============  =====================================================


input vs. sys.stdin.readline
*****************************

If you handle big data, it is faster to use sys.stdin.readline but I don't know why sys.stdin.readline is fater than input.


===========
Reference
===========

* https://songgane.github.io/tips/2016/02/11/ubuntu-update-alternative/
* https://financedata.github.io/posts/faq_pip_packge_fail.html
* http://jkstory-textcube.blogspot.com/2016/02/conda-virtual-environments.html
* `Python Wiki's timeComplexity <https://wiki.python.org/moin/TimeComplexity>`_