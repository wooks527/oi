=====================
Image classification
=====================

LeNet
======

Convolution에서 Parameter가 가장 좋은 경우를 찾은 방법이다.


ILSVRC
=======

ILSVRC (ImageNet Large Scale Visual Recognition Challenge)

* Image classification
* Single object localization
* Object detection


AlexNet
*******

LeNet의 구조를 변경했고 그 내용은 다음과 같다.

* GPU 병렬연산
* ReLU 함수 사용
* Dropout 사용
* Max pooling
* Data augmentation
* Local Response Normalization (LRN)


ZFNet
******

Unpooling 개념을 사용했다.


NIN (Network In Network)
************************

Receptive field에 Dot product가 아닌 MLP를 사용했다.


VGGNet
*******

3x3 블록으로 Layer를 많이 쌓은 방법이다.



GoogleNet / Inception
**********************

여러 개의 Convolution을 병렬로 사용 후 Concatenate 했다.


ResNet
*******

Residual learning이라는 방법을 도입했고, 이는 Activation 함수를 사용하기 전에 Layer 정보를 활용하는 것이다. 이를 통해 Layer가 많이 늘어나도 학습이 가능하게 만들었다. VGGNet을 개선한 것으로 보인다.


MobileNet
**********

Standard convolution을 Depthwise convolution과 Pointwise convolution 단계로 나누어 계산한다. 이를 통해 연산량을 획기적으로 줄였다.


DenseNet
*********

ResNet의 Bottleneck 부분에서 이전 layer를 add 하는 것에서 concatenate 하는 것으로 변경했다.


Reference
==========

* `Fast campus, 딥러닝/인공지능 올인원 패키지 Online <https://www.fastcampus.co.kr/data_online_deep/>`_
* `Deep Residual Learning for Image Recognition, 2015 <https://arxiv.org/pdf/1512.03385.pdf>`_
* `Densely Connected Convolutional Networks, 2018 <https://arxiv.org/pdf/1608.06993.pdf>`_
