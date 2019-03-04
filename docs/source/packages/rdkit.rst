RDKit
======


========================
Install from the source
========================

**Boost 설치**

::

    mkdir boost-install
    cd boost-install
    wget https://jaist.dl.sourceforge.net/project/boost/boost/1.58.0/boost_1_58_0.tar.gz
    tar xzvf boost_1_58_0.tar.gz
    cd boost_1_58_0
    sudo ./bootstrap.sh --with-libraries=python,serialization --prefix=/home/hwkim/boost --with-python=/usr/bin/python3.5 --with-python-version=3.5 --with-python-root=/usr/lib/python3.5
    ./b2 install

    vi ~/.bashrc
        export RDBASE=/home/hwkim/rdkit-Release_2018_03_1
        export BOOST_LIBRARY_PATH=/home/hwkim/boost/lib
        export LD_LIBRARY_PATH=$RDBASE:$BOOST_LIBRARY_PATH:/home/hwkim/rdkit-Release_2018_03_1/lib
        export PYTHONPATH=$PYTHONPATH:$RDBASE


**RDKit 설치**

::

    sudo apt-get install build-essential cmake
    mkdir rdkit-install
    cd rdkit-install
    wget https://github.com/rdkit/rdkit/archive/Release_2018_03_1.tar.gz
    tar xzvf Release_2018_03_1.tar.gz -C ~/

    vi ~/.bashrc
        export LD_LIBRARY_PATH=$RDBASE:$BOOST_LIBRARY_PATH:/home/hwkim/rdkit-Release_2018_03_1/lib

    cd $RDBASE
    mkdir build
    cd build
    sudo cmake .. -DPYTHON_LIBRARY=/usr/lib/python3.5/config-3.5m-x86_64-linux-gnu/libpython3.5.so -DPYTHON_INCLUDE_DIR=/usr/include/python3.5 -DPYTHON_EXECUTABLE=/usr/bin/python3.5 -DBOOST_ROOT=/home/hwkim/boost/ -DBoost_NO_SYSTEM_PATHS=TRUE -DBOOST_LIBRARYDIR=/home/hwkim/boost/lib
    sudo make
    sudo make install


=====
Tips
=====

**특정 RDKit 경로 임시 추가**

import sys
sys.path.append('/home/share/hwkim/rdkit-Release_2018_03_1')


**Reference**