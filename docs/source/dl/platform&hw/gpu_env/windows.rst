=======================
GPU 환경 구축 - Windows
=======================

Windows에 GPU 환경 구축하는 과정을 정리한 페이지이다. 사용한 GPU는 RTX 2070 super이고 지금부터 하나씩 설명하려고 한다.


GPU 설치
=========

우선 GPU를 구매한 후 이를 Main board의 PCI slot에 설치해야 한다. 특히 Power와 연결하는 부분은 GPU마다 다르므로 요구하는 핀 수에 맞게 연결해주면 된다. Driver는 NIVDIA 홈페이지에서 다운 받아서 설치할 수 있다. 추가로 내장 Graphic을 사용하고 싶을 때는 BIOS에서 Primary Display를 OnBoard 또는 IFGX로 해야 하고, IGPU Multi-Monitor 모드를 Enabled 해주어야 한다.

.. figure:: ../img/gpu_env/bios_mult-monitor_setting.png
    :align: center
    :scale: 50%

.. rst-class:: centered

    출처: `erde, 내장 + 외장 그래픽 동시에 사용하기 (멀티모니터) <https://blog.erde.kr/17>`_

추가로 Driver 설치 후 cmd 창에서 GPU 상태를 nvidia-smi로 확인하기 위해서는 nvidia-smi 위치를 Path에 등록해야 한다. 보통 다음 경로가 nvidia-smi 경로다.

* C:\\Program Files\\NVIDIA Corporation\\NVSMI

CUDA and cuDNN
===============

GPU를 사용하기 위해서는 CUDA와 cuDNN을 설치해야 한다. 이 때 2개의 버전을 맞추는 것이 중요한데, 여기서는 CUDA 10.1 (Feb 2019)과 cuDNN v7.6.5 (November 5th, 2019)를 설치했다.

CUDA
*****

Cuda는 공식 홈페이지 (`Link <https://developer.nvidia.com/cuda-toolkit-archive>`_)에서 다운받을 수 있고, CUDA 10.1 설치 시에는 먼저 Visual studio를 설치하라는 메시지가 나와 이를 먼저 설치했다. Visual studio도 공식 홈페이지에서 다운받아서 설치하면 되고, 설치항목은 C++만 선택하면 될 것 같다 (참고: `Visual Studio 2019 설치하기 <http://blog.naver.com/PostView.nhn?blogId=tipsware&logNo=221505528605>`_).

Visual studio를 설치한 후에는 CUDA 설치 프로그램에서 설정되는 기본 설정으로 설치하면 된다. 설치를 완료한 경우 아래의 경로를 Path에 추가해야 한다.

* C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.1\\bin
* C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.1\\extras\\CUPTI\\libx64
* C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v10.1\\include

----------------
Troubleshooting
----------------

* 설치할 수 없다는 메시지를 받는 경우

    * network 버전으로 설치한 경우, 다운로드가 안되어 멈추는 경우가 있으므로 local 버전으로 다운받아서 설치하면 해결됨

cuDNN
******

cuDNN은 공식 홈페이지 (`Link <https://developer.nvidia.com/cudnn>`_)에서 다운받아 CUDA가 설치되어 있는 폴더에 가서 복사 후 붙여넣으면 된다. 다운로드 받을 때, CUDA와 호환되는 cuDNN을 다운받는 것이 중요하다.


Conda
======

GPU 설치를 끝내면 GPU를 사용할 수 있게 환경을 구축해야 한다. 원래는 Docker에서 제공하는 nvidia-docker라는 이미지가 있는데, Windows는 지원하지 않으므로 여기서는 일단 패스한다. 그렇다면 대체방안은 Conda를 이용한 가상 환경 구축이다.

Anaconda는 홈페이지에서 다운받아 설치하면 된다. 혹시 conda나 python이 실행되지 않는 경우 아래의 위치 정보를 Path에 추가하면 된다. 참고로 [사용자명]에는 개인 PC에서 본인이 로그인 할 때 사용한 사용자명을 입력해야 한다.

* C:\\Users\\[사용자명]\\Anaconda3
* C:\\Users\\[사용자명]\\Anaconda3\\Scripts
* C:\\Users\\[사용자명]\\Anaconda3\\lib\\site-packages
* C:\\Users\\[사용자명]\\Anaconda3\\Library\\bin

설치가 잘 되었는지는 cmd에서 conda -V 와 python --V 를 입력해서 확인할 수 있다.

가상 환경
*********

Conda를 설치한 후에는 GPU 환경을 위한 가상 환경을 만들면 된다. 가상 환경을 사용하는 이유는 여러 가지 패키지를 설치했을 때 충돌이 날 수 있고 최악의 경우 OS를 다시 설치해야 할 수도 있다. 이러한 문제를 최소화하고자 가상 환경을 만들고 해당 가상 환경에서 여러 가지 패키지를 설치하여 여러 가지 패키지 설치 시 충돌을 최소화 할 수 있다.

Conda에서는 Anaconda navigator를 사용하거나 cmd 창에서 직접 명령어를 작성하여 가상 환경을 만들 수 있다. 여기서는 명령어를 통해 가상 환경을 만들어보려고 한다.

.. code::

    conda create -n gpu_env python=3.7

위 명령어를 통해 gpu_env라는 가상 환경을 만들 수 있다. 이 때, 가상 환경명 뒤에는 설치하고 싶은 패키지를 입력하면 되고, 추가로 더 설치할 것이 없는 경우에는 기본적으로 python 하나는 입력해주는 것이 좋다. 만약에 패키지를 하나도 입력하지 않으면 비어있는 가상 환경을 만들게 되고, 빈 가상 환경을 이용해 Python을 사용하는 경우 기본 설치된 Python을 이용하게 된다.

가상 환경을 만들고 나서는 해당 가상 환경을 활성화 해야 하고 그 후에 그 가상 환경에서 GPU 환경을 만들어주면 된다.

.. code::

    conda actiavte gpu_env

참고로 가상 환경을 삭제하는 방법은 아래와 같다.

.. code::

    conda remove --name gpu_env --all

-----------------
Troubleshooting
-----------------

* conda activate gpu_env가 실행되지 않는 경우

    * conda init으로 초기화 시킨 후 cmd를 재시작하고 다시 실행해보기

Tensorflow and PyTorch 설치
============================

이제 Tensorflow나 PyTorch와 같은 GPU Library를 설치하면 된다. 관련 내용은 각각의 공식 홈페이지 (`Tensorflow <https://www.tensorflow.org/install/pip>`_, `PyTorch <https://pytorch.org/get-started/locally/>`_)에 자세히 나와 있으며, 실제 사용되는 명령어는 다음과 같다.

Tensorflow
***********

Tensorflow는 pip를 통해 설치할 수 있다.

.. code::

    pip install --upgrade tensorflow

설치 결과는 Python에서 다음 명령어로 확인할 수 있다.

.. code:: python

    C:\> python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
    tf.Tensor(1298.9895, shape=(), dtype=float32)

PyTorch
********

PyTorch는 conda를 이용해 설치할 수 있다.

.. code::

    conda install pytorch torchvision cudatoolkit=10.1 -c pytorch

설치 결과는 Python에서 다음 코드를 실행해 보면 알 수 있다.

.. code:: python

    >>> import torch
    >>> x = torch.rand(5, 3)
    >>> print(x)
    tensor([[0.1847, 0.1291, 0.2709],
        [0.5160, 0.7583, 0.5821],
        [0.2033, 0.6579, 0.4393],
        [0.5903, 0.8483, 0.0634],
        [0.6718, 0.5395, 0.1732]])


:h2:`참조`

* `erde, 내장 + 외장 그래픽 동시에 사용하기 (멀티모니터) <https://blog.erde.kr/17>`_
* `이제는, 딥러닝 개발환경도 Docker로 올려보자!! <http://moducon.kr/2018/wp-content/uploads/sites/2/2018/12/leesangsoo_slide.pdf>`_
* `Tensorflow 공식 홈페이지 <https://www.tensorflow.org/install/pip>`_
* `PyTorch 공식 홈페이지 <https://pytorch.org/get-started/locally/>`_
