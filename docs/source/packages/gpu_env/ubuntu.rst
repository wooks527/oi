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

        docker run -itd --name nvidia-docker -v /home/wooks/share:/root/share -p 8081:8081 --gpus all nvidia/cuda:10.1-devel /bin/bash

    * 부가 설명

        * -v 옵션은 호스트와 컨테이너 사이의 공유 폴더를 설정하는 옵션임 (예: 호스트 경로:컨테이너 경로)
        * -p 옵션은 호스트와 컨테이너 상이에 연결할 포트 번호 (예: 호스트 포트:컨테이너 포트)

설치되지 않은 패키지 설치
************************

* Container에 접속하여 기본 패키지 설치

::

    docker exec -it nvidia-docker bash

    sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list
    apt-get update 
    apt-get dist-upgrade -y

    apt-get install -y wget vim git gcc  build-essential

* libcudnn7 설치 (`Link <https://www.tensorflow.org/install/gpu#ubuntu_1804_cuda_10>`_)

    * 명령어

    ::

        apt-get install --no-install-recommends \
                libcudnn7=7.6.4.38-1+cuda10.1  \
                libcudnn7-dev=7.6.4.38-1+cuda10.1

    * 주의사항

        * cuda는 제외하고 설치
        * 호스트 Driver와 호환되지 않는 경우 에러 발생 (예: Failed to initialize NVML: Driver/library version mismatch)

* libnvinfer6 설치 (`Link <https://www.tensorflow.org/install/gpu#ubuntu_1804_cuda_101>`_)

::

    apt-get install -y --no-install-recommends libnvinfer6=6.0.1-1+cuda10.1 \
            libnvinfer-dev=6.0.1-1+cuda10.1 \
            libnvinfer-plugin6=6.0.1-1+cuda10.1

* Anaconda 설치 (`Link <https://docs.anaconda.com/anaconda/install/linux/>`_)

::

    mkdir downloads
    cd downloads
    wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
    bash Anaconda3-2019.10-Linux-x86_64.sh

    source ~/.bashrc
    conda update -n base conda


Tensorflow와 PyTorch 설치
=========================

* 가상환경 만들고 활성화 하기

::

    conda create -n gpu-env python=3.7
    conda activate gpu-env

* Tensorflow 설치

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

* PyTorch 설치

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
