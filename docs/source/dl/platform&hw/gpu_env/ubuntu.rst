======================
GPU 환경 구축 - Ubuntu
======================

Nvidia driver 및 Docker 설치
=============================

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

* nvidia-docker 설치 (`Link 1 <https://github.com/NVIDIA/nvidia-docker>`_, `Link 2 <https://jybaek.tistory.com/791>`_, `Link 3 <https://hub.docker.com/r/nvidia/cuda/>`_)

    * 설치
    ::

        # Add the package repositories
        distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
        curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
        curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

        sudo apt-get update & sudo apt-get install -y nvidia-container-toolkit
        sudo systemctl restart docker

    * 설치 확인 (확인 할 때 Image가 다운로드 됨)

    ::

        sudo docker run --rm --gpus all nvidia/cuda:10.1-devel nvidia-smi
        sudo docker images

    * sudo 권한 부여 (재시작 필요)

    ::

        sudo usermod -aG docker $USER

* Container 생성

    * 명령어

    ::

        docker run -itd --name nvidia-docker -v [호스트 경로]:/root/share -p 8081:8081 --gpus all --restart=always nvidia/cuda:10.1-devel /bin/bash

    * 부가 설명

        * -v 옵션은 호스트와 컨테이너 사이의 공유 폴더를 설정하는 옵션임 ￫ -v 호스트 경로:컨테이너 경로

            * 호스트 경로는 원하는 경로로 설정하면 됨
            * 예: -v /home/wooks/share:/root/share

        * -p 옵션은 호스트와 컨테이너 상이에 연결할 포트 번호 (예: 호스트 포트:컨테이너 포트)

설치되지 않은 패키지 설치
************************

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

* Tensorflow에서 GPU 사용을 위한 추가 패키지 설치 (PyTorch만 사용하는 경우 설치할 필요 X)

    * libcudnn7 설치 (`Link <https://www.tensorflow.org/install/gpu#ubuntu_1804_cuda_10>`_)

        * 명령어

        ::

            apt-get install --no-install-recommends \
                    libcudnn7=7.6.4.38-1+cuda10.1  \
                    libcudnn7-dev=7.6.4.38-1+cuda10.1

        * 주의사항

            * 호스트 Driver와 호환되지 않는 경우 에러 발생 (예: Failed to initialize NVML: Driver/library version mismatch)

    * libnvinfer6 설치 (`Link <https://www.tensorflow.org/install/gpu#ubuntu_1804_cuda_101>`_)

    ::

        apt-get install -y --no-install-recommends libnvinfer6=6.0.1-1+cuda10.1 \
                libnvinfer-dev=6.0.1-1+cuda10.1 \
                libnvinfer-plugin6=6.0.1-1+cuda10.1




Tensorflow와 PyTorch 설치
=========================

* 가상환경 만들고 활성화 하기

::

    conda create -n gpu-env python=3.7
    conda activate gpu-env

* Tensorflow 설치 (`Link <https://www.tensorflow.org/install/pip>`_)

    * 설치

    ::

        pip install --upgrade tensorflow

    * 테스트

        * 방법 1
    
        ::

            import tensorflow as tf
            device_name = tf.test.gpu_device_name()
            if device_name != '/device:GPU:0':
                raise SystemError('GPU device not found')
            
            print('Found GPU at: {}'.format(device_name))

        * 방법 2

        ::

            tf.test.is_gpu_available()

* PyTorch 설치 (`Link <https://pytorch.org/get-started>`_)

    * PyTorch는 conda를 이용해 설치할 수 있다.

    .. code::

        conda install pytorch torchvision cudatoolkit=10.1 -c pytorch

    * 설치 결과는 Python에서 다음 코드를 실행해 보면 알 수 있다.

        * PyTorch 동작 여부 확인

            * 코드
            
            .. code:: python

                import torch
                x = torch.rand(5, 3)
                print(x)

            * 결과

            ::

                tensor([[0.1847, 0.1291, 0.2709],
                    [0.5160, 0.7583, 0.5821],
                    [0.2033, 0.6579, 0.4393],
                    [0.5903, 0.8483, 0.0634],
                    [0.6718, 0.5395, 0.1732]])

        * GPU 사용 가능 여부 확인

        ::

            import torch
            torch.cuda.is_available()


기타 사항
=========

* GPU에서 Xorg 실행시키고 싶지 않을 때 Prime GPU를 OnBoard의 GPU로 변경하면 된다.

::

    lspci | grep VGA

    prime-switch intel
    prime-select intel


Troubleshooting
================

* shm-size 변경하고 싶을 때

    * 해당 Container의 hostconfig.json 파일의 내용 중 ShmSize의 값을 바꾸면 됨
    * 그리고 이것도 안되면 Host의 ShmSize도 변경해보기 

        * 방법

            * /etc/fstab 파일의 가장 하단에 아래 내용을 한 줄 추가하기

            ::

                tmpfs /dev/shm tmpfs defaults,size=8g 0 0

            * /dev/shm 마운트 다시하기

            ::

                mount -o remount /dev/shm

        * 참조

            * `SysTutorials, How to configure /dev/shm size of Linux? <https://www.systutorials.com/how-to-configure-dev-shm-size-of-linux/>`_
