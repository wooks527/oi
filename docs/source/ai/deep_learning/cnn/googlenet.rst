==========
GoogLeNet
==========

GoogLeNet은 2014년 ILSVRC에서 1위를 차지한 모델이고, 가장 큰 변화는 Network의 깊이다.

.. figure:: ../img/cnn/googlenet/revolution_of_depth.png
    :align: center
    :scale: 70%

.. rst-class:: centered

    출처: `라온피플 (Laon People) <https://laonple.blog.me/220686328027>`_

CNN의 성능을 향상시키는 가장 직접적인 방법은 Network 크기를 늘리는 방법이다. 2013년까지는 CNN network의 깊이가 10 미만이었지만, 2014년 GoogLeNet과 VGGNet이 각각 22 layer, 19 layer로 2배 이상 커졌다. 물론 Top-5 에러율도 각각 6.7%, 7.3% 낮아졌다. 이후 2015년에 우승한 ResNet은 152개의 Layer를 가지고 Top-5 에러율도 3.57%로 더 낮아진다.

하지만 Network가 깊어지면 Trainable parameter 수가 증가하게 되고, 그 결과 Overfitting 문제가 발생하거나 연산량이 급격히 늘어날 수 있다. AlexNet만 보더라도 Trainable parameter 수가 6천만개이고, GPU (GTX580) 2개를 사용하여 일주일 이상 학습시켰다. 단순히 Network를 깊게 만들면 학습시간이 엄청나게 길어질 수 있다.

따라서, 이러한 문제를 해결하기 위해서는 Network의 구조적인 변화에 대한 고민이 필요했고, Google에서 Inception이라는 모듈로 구성된 GoogLeNet으로 이를 해결했다. 여기서 Inception 모듈은 싱가포르 국립대학의 Min Lin이 2013년에 발표한 "Network in Network"의 구조를 더 발전시킨 형태이다. Network in Network (NIN) 구조는 :doc:`여기 <nin>` 에서 확인할 수 있다.


Inception
==========

Google 연구팀은 NIN을 기반으로 Network를 깊게 만들면서도 연산량의 수가 급격히 늘지 않는 Inception이라는 모듈을 만들었다. 또한, Local receptive field에서 더 다양한 Feature를 추출하기 위해 여러 개의 Convolution을 병렬적으로 사용했다.

.. figure:: ../img/cnn/googlenet/inception_module.png
    :align: center
    :scale: 70%

.. rst-class:: centered

    출처: `라온피플 (Laon People) <https://laonple.blog.me/220686328027>`_

Inception에서는 같은 Layer에 다른 크기를 가지는 Filter를 적용하여 다른 Scale의 Feature를 추출할 수 있게 만들었다. 그러면서 1x1 convolution을 적절히 사용하여 차원을 줄여 연산량 문제를 해결했다.

원래 초기에는 아래 그림처럼 1x1/3x3/5x5 Convolution, 3x3 Max pooling을 나란히 놓는 구조를 만들었다. 하지만 3x3과 5x5 Convolution은 연산량이 많아 Network가 깊어지면 치명적인 문제가 될 수 있다. 이러한 문제를 해결하기 위해 1x1 Convolution으로 Feature map의 차원 수를 줄였다. 

.. figure:: ../img/cnn/googlenet/inception_module_naive_and_optimized.png
    :align: center
    :scale: 65%

.. rst-class:: centered

    출처: `라온피플 (Laon People) <https://laonple.blog.me/220692793375>`_

GoogLeNet의 Inception은 기존 CNN 구조에서 크게 벗어나지 않으면서 NIN의 특징을 반영했다 (반면 NIN은 MLP로 Non-linear feature를 얻었으나, 결국 Fully connected 형태이고 구조적으로도 익숙하지 않음).


Parameters
***********

더욱 놀라운 것은 GoogLeNet이 Network가 더 깊은데 Trainable parameter 수는 AlexNet의 1/12 수준이라는 것이다.

.. figure:: ../img/cnn/googlenet/params_alexnet_googlenet.png
    :align: center
    :scale: 70%

.. rst-class:: centered

    출처: `라온피플 (Laon People) <https://laonple.blog.me/220686328027>`_

Google 연구팀은 Network를 더 깊게 하여 성능을 높이면서 연산량을 증가시키지 않는 연구를 진행했다. 그 결과 초기 CNN 구조의 문제점을 알았고, Inception 모듈로 구성된 GoogLeNet을 만들었다.


Reference
==========

* 라온피플 - `GoogLeNet [1] <https://laonple.blog.me/220686328027>`_, `GoogLeNet [2] <https://laonple.blog.me/220692793375>`_, `GoogLeNet [3] <https://laonple.blog.me/220704822964>`_
* `YouTube, 최희정 - CNN Localization (ZFNet & Deep Taylor Decomposition) <https://www.youtube.com/watch?v=46TlWpZgKRE>`_
