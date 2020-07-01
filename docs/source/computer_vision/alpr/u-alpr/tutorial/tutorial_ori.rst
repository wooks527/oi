============================
Tutorial for original codes
============================

Nvidia driver + Docker 설치
============================

* Nvidia driver 설치 (`Link <https://codechacha.com/ko/install-nvidia-driver-ubuntu/>`_)

::

    sudo add-apt-repository ppa:graphics-drivers/ppa
    sudo apt update
    sudo ubuntu-drivers autoinstall
    sudo reboot

* Docker 설치 (`Link <https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-engine---community>`_)

    * Set up the repository

    ::

        sudo apt-get update

        sudo apt-get install \
             apt-transport-https \
             ca-certificates \
             curl \
             gnupg-agent \
             software-properties-common

        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

        sudo apt-key fingerprint 0EBFCD88

        sudo add-apt-repository \
             "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
             $(lsb_release -cs) \
             stable"

    * Install docker engine - community

    ::

        sudo apt-get update
        sudo apt-get install docker-ce docker-ce-cli containerd.io

nvidia-docker 설치 후 Container 생성
====================================

nvidia-docker 설치
*******************

* 설치

::

    # Add the package repositories
    distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
    curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
    curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

    sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
    sudo systemctl restart docker

* 설치 확인 (확인 할 때 Image가 다운로드 됨)

::

    sudo docker run --rm --gpus all nvidia/cuda:10.0-devel nvidia-smi
    sudo docker images

* 참고 링크: `Link 1 <https://github.com/NVIDIA/nvidia-docker>`_, `Link 2 <https://jybaek.tistory.com/791>`_, `Link 3 <https://hub.docker.com/r/nvidia/cuda/>`_

Container 생성 후 각종 패키지 설치
**********************************

* Container 생성

    * 명령어

    ::

        docker run -itd --name nvidia-docker -v [호스트 경로]:/root/share -p 8081:8081 --gpus all --restart=always nvidia/cuda:10.0-devel /bin/bash

    * 부가 설명

        * -v 옵션은 호스트와 컨테이너 사이의 공유 폴더를 설정하는 옵션임 ￫ -v 호스트 경로:컨테이너 경로

            * 호스트 경로는 원하는 경로로 설정하면 됨
            * 예: -v /home/wooks/share:/root/share

        * -p 옵션은 호스트와 컨테이너 상이에 연결할 포트 번호 (예: 호스트 포트:컨테이너 포트)

* Container에 접속하여 기본 패키지 설치

    * 명령어

    ::

        docker exec -it nvidia-docker bash

        sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list
        apt-get update 
        apt-get dist-upgrade -y

        apt-get install -y wget vim git gcc  build-essential

    * 추가 정보

        * apt-get update를 위해 등록되는 sources.list의 내용은 아래와 같음

        ::

            # See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to
            # newer versions of the distribution.
            deb http://ftp.daumkakao.com/ubuntu/ bionic main restricted
            # deb-src http://ftp.daumkakao.com/ubuntu/ bionic main restricted

            ## Major bug fix updates produced after the final release of the
            ## distribution.
            deb http://ftp.daumkakao.com/ubuntu/ bionic-updates main restricted
            # deb-src http://ftp.daumkakao.com/ubuntu/ bionic-updates main restricted

            ## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
            ## team. Also, please note that software in universe WILL NOT receive any
            ## review or updates from the Ubuntu security team.
            deb http://ftp.daumkakao.com/ubuntu/ bionic universe
            # deb-src http://ftp.daumkakao.com/ubuntu/ bionic universe
            deb http://ftp.daumkakao.com/ubuntu/ bionic-updates universe
            # deb-src http://ftp.daumkakao.com/ubuntu/ bionic-updates universe

            ## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
            ## team, and may not be under a free licence. Please satisfy yourself as to
            ## your rights to use the software. Also, please note that software in
            ## multiverse WILL NOT receive any review or updates from the Ubuntu
            ## security team.
            deb http://ftp.daumkakao.com/ubuntu/ bionic multiverse
            # deb-src http://ftp.daumkakao.com/ubuntu/ bionic multiverse
            deb http://ftp.daumkakao.com/ubuntu/ bionic-updates multiverse
            # deb-src http://ftp.daumkakao.com/ubuntu/ bionic-updates multiverse

            ## N.B. software from this repository may not have been tested as
            ## extensively as that contained in the main release, although it includes
            ## newer versions of some applications which may provide useful features.
            ## Also, please note that software in backports WILL NOT receive any review
            ## or updates from the Ubuntu security team.
            deb http://ftp.daumkakao.com/ubuntu/ bionic-backports main restricted universe multiverse
            # deb-src http://ftp.daumkakao.com/ubuntu/ bionic-backports main restricted universe multiverse

            ## Uncomment the following two lines to add software from Canonical's
            ## 'partner' repository.
            ## This software is not part of Ubuntu, but is offered by Canonical and the
            ## respective vendors as a service to Ubuntu users.
            # deb http://archive.canonical.com/ubuntu bionic partner
            # deb-src http://archive.canonical.com/ubuntu bionic partner

            deb http://security.ubuntu.com/ubuntu/ bionic-security main restricted
            # deb-src http://security.ubuntu.com/ubuntu/ bionic-security main restricted
            deb http://security.ubuntu.com/ubuntu/ bionic-security universe
            # deb-src http://security.ubuntu.com/ubuntu/ bionic-security universe
            deb http://security.ubuntu.com/ubuntu/ bionic-security multiverse
            # deb-src http://security.ubuntu.com/ubuntu/ bionic-security multiverse

* Anaconda 설치 (`Link <https://docs.anaconda.com/anaconda/install/linux/>`_)

::

    mkdir downloads
    cd downloads
    wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
    bash Anaconda3-2019.10-Linux-x86_64.sh

    source ~/.bashrc
    conda update -n base conda

* Tensorflow에서 GPU 사용을 위한 추가 패키지 설치

    * libcudnn 설치 (시간이 조금 걸림)

    ::

        apt-get install libcudnn7=7.6.5.32-1+cuda10.0


alpr-unconstrained 실행을 위한 환경 설정
========================================

* 가상환경 만들고 활성화 하기

::

    conda create -n u-alpr python=2.7
    conda activate u-alpr

* tensorflow 설치

    * 설치

    ::

        pip install --upgrade tensorflow==1.15.0

    * 테스트

        * 방법 1
    
        ::

            import tensorflow as tf
            device_name = tf.test.gpu_device_name()
            if device_name != '/device:GPU:0':
                raise SystemError('GPU device not found')
            
            print 'Found GPU at: {}'.format(device_name)

        * 방법 2

        ::

            tf.test.is_gpu_available()

* keras 설치

::
    
    pip install keras==2.2.4

* OpenCV 설치 (`Link <https://pypi.org/project/opencv-python/>`_)

    * 설치

    ::

        pip install opencv-python
        pip install opencv-contrib-python

    * 버전

        * opencv-python-4.2.0.32
        * opencv-contrib-python-4.2.0.32

    * 테스트

        ::

            python -c "import cv2"
            
        * 아무런 결과가 나오지 않아야 제대로 설치된 것임

    * Trobule shooting

        * ImportError: libgthread-2.0.so.0: cannot open shared object file: No such file or directory (`Link <https://www.kaggle.com/c/inclusive-images-challenge/discussion/70226>`_)

        ::

            apt-get install libgtk2.0-dev


alpr-unconstrained 테스트
==========================

* alpr-unconstrained 코드 복제

::

    git clone https://github.com/sergiomsilva/alpr-unconstrained.git

* darknet build

::

    cd darkenet
    make

* 기존 모델 다운로드 후 간단한 테스트

    * 코드

    ::

        bash get-networks.sh

        bash run.sh -i samples/test -o tmp/output -c tmp/output/results.csv

    * Troubleshooting

        * Could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR (`Link 1 <https://lsjsj92.tistory.com/363>`_, `Link 2 <https://github.com/tensorflow/tensorflow/issues/24496#issuecomment-464891884>`_)

            * 추가할 코드

            ::

                import tensorflow as tf
                config = tf.ConfigProto()
                config.gpu_options.allow_growth = True
                session = tf.Session(config=config)

            * 대상 파일: license-plate-detection.py, train-detector.py

* Training LP detector

    * 코드

    ::

        mkdir models

        python create-model.py eccv models/eccv-model-scracth
        python train-detector.py --model models/eccv-model-scracth --name my-trained-model --train-dir samples/train-detector --output-dir models/my-trained-model/ -op Adam -lr .001 -its 300000 -bs 64

    * Troubleshooting

        * Could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR (`Link 1 <https://lsjsj92.tistory.com/363>`_, `Link 2 <https://github.com/tensorflow/tensorflow/issues/24496#issuecomment-464891884>`_)

        ::

            import tensorflow as tf
            config = tf.ConfigProto()
            config.gpu_options.allow_growth = True
            session = tf.Session(config=config)
