=======
Docker
=======

서버 관리 시 문제점
===================

서버 구성 시 하나의 서버에 Web server, Web application server, DB server를 동시에 구축하게 되면 여러 Program을 하나의 서버에 설치하게 된다.
기술 개발 속도가 빨라짐에 따라 업데이트 시 여러 Program 간의 충돌이 생길 수 있다.
결론적으로 여러 개의 서버에 각 서버를 따로 구축해야 되는 상황이 발생한다.
하지만 이는 자원 낭비가 될 수 있고 이에 대한 대안으로 하나의 컴퓨터에 여러 개 서버를 구성하는 가상환경이 활용된다.
대표적인 예가 VM ware와 같은 프로그램이고, 이는 OS를 가상화하기 때문에 무겁고 느린 단점이 있다.
이러한 단점을 해결하기 위해 등장한 것이 Docker이고 Docker는 프로세스를 격리시켜 독립된 서버로 구성할 수 있다.
상세한 내용은 아래 관련 링크를 통해 이해할 수 있다.

.. figure:: img/vm_vs_docker.png
    :scale: 40%

하나의 서버에 여러 개의 컨테이너를 실행하면 서로 영향을 미치지 않고 독립적으로 실행되어 마치 가벼운 Virtual Machine을 사용하는 느낌을 준다.
이러한 컨테이너는 이미지 형태로 저장될 수 있다.
이미지는 컨테이너 실행에 필요한 파일과 설정값등을 포함하고 있는 것으로 상태값을 가지지 않고 변하지 않는다.

.. figure:: img/docker_image.png
    :scale: 40%

**관련 링크**

* https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html


WSGI
=======

.. figure:: img/wsgi.png
    :scale: 80%

웹 서버 게이트웨이 인터페이스(WSGI, Web Server Gateway Interface)는 웹서버와 웹 애플리케이션의 인터페이스를 위한 파이선 프레임워크다.
uWSGI는 웹 클라이언트가 웹 서버에게 요청한 HTTP 프로토콜 요청을 Python Call로 변환하기 위한 매핑관계를 WSGI 표준으로 구현한 것이다.

Port 관련 처리
===============

Docker 포트 추가 및 변경
************************

**Step 1:** Stop the docker container

**Step 2:** Edit config.v2.json

::

    sudo vi /mnt/sdb/docker/containers/fba2e6ecdf13fc83f7002fe3d066f64b2798cc59f5c9e842508b53ac75d96934/config.v2.json
    ...
    {
    "Config": {
    ....
    "ExposedPorts": {
    "80/tcp": {},
    "8888/tcp": {}
    },
    ....

**Step 3:** Edit hostconfig.json

::

    sudo vi /mnt/sdb/docker/containers/fba2e6ecdf13fc83f7002fe3d066f64b2798cc59f5c9e842508b53ac75d96934/hostconfig.json
    ....
     "PortBindings": {
     "80/tcp": [
     {
     "HostIp": "",
     "HostPort": "80"
     }
     ],
     "8888/tcp": [
     {
     "HostIp": "",
     "HostPort": "8888"
     }
     ]
     },
    .....

Multiple ports
***************

::

    docker run -p <host_port1>:<container_port1> -p <host_port2>:<container_port2>


::

    docker run -p <host_port1>-<host_port2>:<container_port1>-container_port2>

:h4:`참조`

* `IntelliPoat <https://intellipaat.com/community/240/how-do-i-expose-multiple-port-with-docker>`_
* `Stack Overflow <https://stackoverflow.com/a/32806333>`_

실행중인 Container에 Port 또는 Volume 추가
******************************************

::

    docker stop [현재 컨테이너명]
    docker commit [현재 컨테이너명] [현재 컨테이너로 만들 이미지명]
    docker run -v [호스트 경로]:[컨테이너 경로] -p [호스트 포트]:[컨테이너 포트] -d [위에서 만든 이미지명] --name [새로운 컨테이너명]


Commands
=========

* 복사

    * Host -> Container

    ::

        docker cp [container name]:[container 내부 경로] [host 파일경로]

    * Container -> Host

    ::

        docker cp [host 파일경로] [container name]:[container 내부 경로]

* Container 이름 변경

::

    docker rename [원래 컨테이너명]:[새로운 컨테이너명]


Commit and push
================

* Commit

::

    docker commit -a "[작성자명] <[이메일주소]>" -m "Commit 메시지" [컨테이너명] [이미지명:태그]

(작성 예정)

* `Cloudkul, Docker Images and Containers: Points to Remember <https://cloudkul.com/blog/understanding-docker-images-and-containers/>`_
* `pyrasis.com, Docker 기본 사용법 <http://pyrasis.com/Docker/Docker-HOWTO>`_
* `SCALYR, HOW TO CREATE A DOCKER IMAGE FROM A CONTAINER <https://www.scalyr.com/blog/create-docker-image/>`_


Jupyter notebook 사용하기
=========================

* Container 내부에서 아래 명령어를 실행하면 됨

    * 명령어

    ::

        jupyter notebook --ip 0.0.0.0 --port 8082 --no-browser --allow-root

    * 주의 사항

        * 포트 번호는 Container 생성 시 연결한 포트 중 하나를 선택하면 됨

:h3:`참조`

* `Eungbean Lee, 랩탑에서 딥러닝 서버에 접속하여 DOCKER/JUPYTER 사용하기 <https://eungbean.github.io/2019/03/22/jupyter-ssh/>`_


Docker에 X window 설정
=======================

* 호스트에서 아래 명령어 실행

::

    xhost local:root

* Container 생성 시 아래 옵션 추가 (옵션은 정리가 필요함, `Link 1 <http://wiki.ros.org/docker/Tutorials/GUI>`_, `Link 2 <https://conservative-vector.tistory.com/entry/docker%EC%97%90%EC%84%9C-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88-gui-%EC%8B%A4%ED%96%89%ED%95%98%EA%B8%B0>`_, )

::

    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e DISPLAY=unix$DISPLAY \

:h3:`참조`

* `EUNGBEAN, [EOD]CANNOT CONNECT TO X SERVER :0.0 <https://eungbean.github.io/2018/12/04/EOD-cannot-connect-to-X-server-0.0/>`_


nvidia-docker
==============

GPU 선택 방법
*************

::

    #### Test nvidia-smi with the latest official CUDA image
    docker run --gpus all nvidia/cuda:10.0-base nvidia-smi

    # Start a GPU enabled container on two GPUs
    docker run --gpus 2 nvidia/cuda:10.0-base nvidia-smi

    # Starting a GPU enabled container on specific GPUs
    docker run --gpus '"device=1,2"' nvidia/cuda:10.0-base nvidia-smi
    docker run --gpus '"device=UUID-ABCDEF,1"' nvidia/cuda:10.0-base nvidia-smi

    # Specifying a capability (graphics, compute, ...) for my container
    # Note this is rarely if ever used this way
    docker run --gpus all,capabilities=utility nvidia/cuda:10.0-base nvidia-smi

위 코드에서 볼 수 있듯이 ``--gpus`` 옵션 뒤에 어떤 값을 입력하느냐에 따라 어떤 GPU를 사용할 것인지 결정할 수 있다.

:h4:`참조`

* `GitHub, NVIDIA/nvidia-docker <https://github.com/NVIDIA/nvidia-docker>`_
* `GitHub, NVIDIA/nvidia-docker, Wiki <https://github.com/NVIDIA/nvidia-docker/wiki>`_


Q&A
====

* 여러 개의 Image들로 하나의 Container를 만들 수 없는지 여부

    * (조사 필요)


:h2:`출처`

* https://mybrainimage.wordpress.com/2017/02/05/docker-change-port-mapping-for-an-existing-container/
* http://www.leafcats.com/163
* `위키피디아 <https://ko.wikipedia.org/wiki/%EC%9B%B9_%EC%84%9C%EB%B2%84_%EA%B2%8C%EC%9D%B4%ED%8A%B8%EC%9B%A8%EC%9D%B4_%EC%9D%B8%ED%84%B0%ED%8E%98%EC%9D%B4%EC%8A%A4`_
* https://blog.appdynamics.com/engineering/an-introduction-to-python-wsgi-servers-part-1/