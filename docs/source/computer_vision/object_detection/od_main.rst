================
Object detction
================

위키피디아에 따르면 Object detction은 비디오나 사진에서 Object를 감지하는 작업이다. 그렇다면 어떻게 Object를 감지할 수 있을까? 감지하는 과정은 크게 2가지로 나눌 수 있다.

먼저, 비디오나 사진에서 어떤 물체가 있는지 분류 (Classification)한다. 그리고 분류된 Object가 어디에 있는지 파악하는 과정 (Localization)을 통해 Object를 감지할 수 있다. 방금 언급한 내용이 아래 그림의 2번째 그림이다.

.. figure:: ../img/od/object_detction.png
    :align: center
    :scale: 100%

.. rst-class:: centered

    출처: `제이스핀, Object Detection <https://nuggy875.tistory.com/20?category=860935>`_

하지만 실제 비디오나 사진에는 여러 가지 Object가 있을 수 있기 때문에 결과적으로 세 번째 그림과 같이 여러 개의 Object를 분류하고 (Multi-labeled classification), Object들의 위치를 파악하는 것 (Localization)이 Object detection이라고 할 수 있다.

Classification과 관련된 내용은 :doc:`../cnn/cnn` 부분에서 많이 다뤘기 때문에, 여기서는 Object localization부터 하나씩 다루려고 한다.

.. toctree::
    :caption: 목차
    :maxdepth: 1

    find_an_object_loc
    object_detection
    od_eval
    yolo
    yolov4
    r-cnn
    sppnet
    fast_r-cnn
    faster_r-cnn

* :doc:`sift`
* R-CNN (Regions with CNN features)
* SPPNet (Spatial Pyramid Pooling in Deep Convolutional Networks for Visual Recognition)
* Fast-RCNN
* Faster-RCNN


:h2:`Reference`

* 라온피플 (Laon People) - `ZFNet [2] <https://laonple.blog.me/220676812642>`_, `GoogLeNet [6] <https://laonple.blog.me/220731472214>`_, `ResNet [4] <https://laonple.blog.me/220776743537>`_, `ResNet [5] <https://laonple.blog.me/220782324594>`_, `ResNet [6] <https://laonple.blog.me/220788549910>`_