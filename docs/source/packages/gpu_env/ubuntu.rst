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

    * Install docker engine - community

    ::

        sudo apt-get update
        sudo apt-get install docker-ce docker-ce-cli containerd.io

nvidia-docker 설치 후 Container 생성
====================================

* nvidia-docker 설치 (`Link 1 <https://github.com/NVIDIA/nvidia-docker>`_, `Link 2 <https://jybaek.tistory.com/791>`_)

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

        docker run --runtime=nvidia --rm nvidia/cuda:10.0-devel nvidia-smi

* Container 생성

::

    docker run -itd --name nvidia-docker -v /home/wooks/share:/root/share -p 8081:8081 --gpus all nvidia/cuda:10.0-devel /bin/bash

* Container에 접속하여 기본 패키지 설치

::

    docker exec -it <CONTAINER_NAME> bash

    sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list
    apt-get update 
    apt-get dist-upgrade -y

    apt-get install -y wget vim git gcc  build-essential

* Anaconda 설치 (`Link <https://docs.anaconda.com/anaconda/install/linux/>`_)

::

    mkdir downloads & cd downloads
    wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
    bash Anaconda3-2019.10-Linux-x86_64.sh

    source ~/.bashrc
    conda update -n base conda

* libcudnn 설치

::

    apt-get install libcudnn7=7.6.5.32-1+cuda10.0


Tensorflow와 PyTorch 설치
=========================

* 가상환경 만들기

::

    conda create -n u-alpr python=3.7

* Tensorflow 설치

    * 설치

    ::

        pip install --upgrade tensorflow

    * 테스트

    ::

        import tensorflow as tf
        device_name = tf.test.gpu_device_name()
        if device_name != '/device:GPU:0':
            raise SystemError('GPU device not found')
        
        print 'Found GPU at: {}'.format(device_name)

* PyTorch 설치

    * PyTorch는 conda를 이용해 설치할 수 있다.

    .. code::

        conda install pytorch torchvision cudatoolkit=10.1 -c pytorch

    * 설치 결과는 Python에서 다음 코드를 실행해 보면 알 수 있다.

    .. code:: python

        >>> import torch
        >>> x = torch.rand(5, 3)
        >>> print(x)
        tensor([[0.1847, 0.1291, 0.2709],
            [0.5160, 0.7583, 0.5821],
            [0.2033, 0.6579, 0.4393],
            [0.5903, 0.8483, 0.0634],
            [0.6718, 0.5395, 0.1732]])
