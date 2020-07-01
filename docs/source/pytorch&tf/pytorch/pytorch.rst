========
PyTorch
========

파이토치 (PyTorch)는 2017년 공개된 딥러닝 프레임워크로 페이스북의 인공지능 연구팀에서 관리한다.

사실, 파이토치 이외에도 텐서플로우와 같은 딥러닝 프레임워크가 있는데 왜 파이토치를 사용해야 할까? 파이토치를 텐서플로우와 비교했을 때 차이점은 다음과 같다.

* 프로세스 차이

    * 텐서플로우는 'Define and Run' 방식이라 그래프를 먼저 만들고, 실제 연산 시 값을 전달함
    * 그래서 전체적으로 코드가 길어지고, 그래프와 연산을 분리해서 생각해야 함
    * 하지만 파이토치는 'Define by Run' 방식으로 그래프 정의와 값 초기화가 동시에 일어남
    * 따라서 그래프와 연산을 분리해서 생각할 필요가 없고, 코드가 더 간결함

* 연산 속도

    * 실제로 깃허브에서 테스트한 실험에 따르면 파이토치가 텐서플로우 보다 2.5배 빠르다고 함

그래서 PyTorch를 잘 사용하는 것은 딥러닝을 활용할 때 중요하다.

지금부터 PyTorch에 대해 알아보려고 하고, 여기에서는 Coursera의 Deep Neural Networks With PyTorch라는 강의를 기준으로 정리했고 그 링크는 다음과 같다.

.. toctree::
    :caption: Table of contents
    :maxdepth: 1

    deep-neural-networks-with-pytorch/deep-neural-networks-with-pytorch




아래 내용은 과거에 정리해 둔 내용인데 추후에 처리할 예정이다.

* `텐서 (Tensor) <https://github.com/hwkim89/dl_framework/blob/master/pytorch/tensor.ipynb>`_
* `경사하강법 (Gradient descent) <https://github.com/hwkim89/dl_framework/blob/master/pytorch/gradient_descent.ipynb>`_


:h2:`참조`

* 파이토치 첫걸음, 최건호 지음, 한빛미디어, 2019
