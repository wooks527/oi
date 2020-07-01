====================
Korean ALPR dataset
====================

여기에서는 한국의 차량 번호판과 관련된 데이터 셋을 정리하려고 한다. 먼저, 대한민국의 차량 번호판에 대해 이해해보자.


대한민국의 차량 번호판
======================

위키피디아에 따르면 (`위키피디아 <https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%B0%A8%EB%9F%89_%EB%B2%88%ED%98%B8%ED%8C%90>`_), 대한민국의 차량 번호판은 대한민국에서 등록되는 모든 자동차의 전·후면에 부착되는 직사각형 모양의 금속판으로서, 정식 명칭은 자동차등록번호판이다. 자동차등록번호판은 한글과 아라비아 숫자의 조합으로 이루어진 일련번호, 즉 자동차등록번호, 일명 차량번호를 포함하는데, 그 조합 방식은 등록 자동차 수의 급격한 증가와 더불어 바뀌어 왔다.

1973년, 1996년, 2004년 세 번에 걸쳐서 조합 방식과, 색상 등 형태상으로 큰 변화가 있었는데, 1973년 4월 15일부터 계속 유지되고 있는 큰 틀은 <해당 자동차의 사용 목적 구별 - 자가용/사업용>, <한글 한 글자 사용>, <마지막 네 자리 일련번호> 이렇게 세 가지이다. 번호판의 한글기호는 군용을 제외한 나머지는 받침이 없다.

건설기계(굴삭기, 덤프트럭 등)나 모터사이클(이륜자동차), 관용 차량(외교관 차량), 군용 차량, 주한 미군 차량 등에도 등록 번호가 부여되나, 일반 자동차와는 다른 방식으로 부여되며, 규격·색상도 상이하다. 자전거, 경운기 등은 번호판 부착 대상이 아니다.

조금 더 자세한 내용은 :doc:`kr_lp_def` 에 따로 정리했으니 더 자세히 이해하고 싶을 때 참고하면 된다.


Dataset
========

KarPlate dataset
*****************

* `KarPlate Dataset <http://pr.gachon.ac.kr/ALPR.html>`_

Korean vehicle dataset
***********************

* `Korean vehicle dataset <https://github.com/seokbongyoo/Dataset_for_LPR>`_

Others
*******

* 더 살펴봐야 할 논문들

    * Accurate License Plate Recognition and Super-Resolution Using a Generative Adversarial Networks on Traffic Surveillance Video, 2018

        * 총 1,000대의 차량에 대해 각각 4가지 이미지를 사용함
        * 공개 X

    * Real-Time License Plate Detection Based on Faster R-CNN, 2016

        * 두 대의 카메라로 서로 다른 시점에서 실제 도로를 주행중인 차들을 촬영한 이미지 사용
        * 총 약 8만장의 이미지로 실험함 (이런 데이터 셋은 어디서 구하는 건지 모르겠음)
        * 공개 X

    * 도로주행 영상에서의 차량 번호판 검출, 2014

        * 현대모비스에서 제공한 도로 주행 영상 데이터 사용
        * 총 약 724장의 이미지 사용

    * 왜곡 불변 차량 번호판 검출 및 인식 알고리즘, 2011

        * 구청과 대학에 설치된 상용 LPR 시스템 카메라로 촬영
        * 총 약 6200장의 차량 영상 데이터 사용

* 알 수 없음

    * A Novel License Plate Detection Approach for an Embedded System, 2020

    * Korean License Plate Recognition System Using Combined Neural Networks, 2020

    * Vehicle license plate detection using region-based convolutional neural networks, 2018

        * ResearchGate에 논문 요청함

    * Vehicle Plate Detection in Car Black Box Video, 2017

        * Dataset에 접근 권한 X

    * HSI color based vehicle license plate detection, 2008

    * An Approach to Korean License Plate Recognition Based on Vertical Edge Matching, 2000

    * LEARNING-BASED APPROACH FOR LICENSE PLATE RECOGNITION, 2000

* 정리 필요

    * Automatic license plate detection and recognition framework to enhance security applications, 2019
    * Automatic Number Plate Detection for Korean Vehicles, 2009

