=======
YOLOv4
=======

YOLOv4가 2020년 4월 23일 arXiv에 공개되었고 논문 제목은 “YOLOv4：Optimal Speed and Accuracy of Object Detection” 이다.

여기에서는 YOLOv4에 대한 내용과 실제 사용법에 대해 정리해보려고 한다.

아직 내용 정리는 ...


실제 사용법
===========

Training
*********

학습은 아래와 같은 명령어를 이용하여 진행할 수 있다.

.. code::

    ./darknet detector train data/obj.data cfg/yolo-obj.cfg yolov4.conv.137 -dont_show -mjpeg_port 8090 -map

여기서 obj.data는 Training과 Test 정보를 나타내는 파일이고, yolo-obj.cfg는 YOLOv4의 구조에 대한 정보를 나타내는 파일이다. 그 내용을 살펴보면 다음과 같다.

* obj.data

    .. code::

        classes = 1
        train = data/train.txt
        valid = data/valid.txt
        names = data/obj.names
        backup/backup

    * classes: 학습할 모델이 구분해야 하는 Class 수
    * train: 학습할 이미지의 경로를 저장하고 있는 텍스트 파일
    * valid: 검증할 이미지의 경로를 저장하고 있는 텍스트 파일
    * names: 분류할 Object의 이름이 저장된 파일
    * backup: 학습된 모델을 저장할 위치


Test
*****

테스트는 아래와 같은 명령어를 이용하여 진행할 수 있다.

.. code::

    ./darknet detector map data/obj.data cfg/yolo-obj.cfg backup/yolo-obj_best.weights

여기서 backup에 저장된 yolo-obj_best.weights는 위에서 언급한 Training을 통해 학습된 YOLOv4 모델 중 가장 성능이 좋았던 경우의 Weight를 저장한 파일이다.


:h2:`참조`

* `HOYA012'S RESEARCH BLOG, YOLOv4：Optimal Speed and Accuracy of Object Detection Review <https://hoya012.github.io/blog/yolov4/>`_
* `GitHub, AlexeyAB/darknet <https://github.com/AlexeyAB/darknet>`_
* `YOLOv4: Optimal Speed and Accuracy of Object Detection <https://arxiv.org/abs/2004.10934>`_
