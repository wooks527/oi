=====
용어
=====

* 대비 표준화 (Contrast normalization)

    * 다양한 이미지로 학습하는 경우 이미지마다 밝기가 다르고 찍은 환경이 다를 수 있습니다.
    
    * 이것을 어느 정도 통일해 주는 것이 대비 표준화 (Contrast normalization) 과정입니다.

    * 표준화 과정은 평균을 빼고 표준편차로 나눠주는 :math:`\hat X = \frac{X - E(X)}{\sigma(X)}` 과정입니다. 전체 픽셀들의 분포가 평균이 0이고 분산이 1인 정규분포로 바뀌게 됩니다.

    * 종류

        * 전체 대비 표준화 (Global Contrast Normalization, GCN)
        
            * 전체 이미지에 대해서 하는 경우 
            * feature-wise 라고도 함
            * 모든 훈련 이미지의 픽셀들에 대해 평균과 표준편차를 구하고 이 평균과 표준편차로 모든 이미지의 픽셀들을 표준화함

        * 개별 대비 표준화 (Local Contrast Normalization, LCN)
        
            * 각각의 이미지에 대해서 하는 경우
            * sample-wise 라고도 함
            * 각각의 이미지의 픽셀들에 대해 평균과 표준편차를 구하고 해당 이미지의 픽셀들을 표준화함

        * GCN과 LCN 모두 데이터에 대해 한 번만 하면 됨

    * 출처: `Deepest documentation <https://deepestdocs.readthedocs.io/en/latest/003_image_processing/0030/>`_

* 측면 억제 (Lateral inhibition)

    * 측면 억제는 발생과정 중 같은 분화능을 갖는 다수의 세포에서 소수의 세포가 선택되어 특정 세포로 분화하는 과정을 설명하기 위하여 제시된 개념이다.
    * 측면 억제 과정에서는 외부의 신호에 의하여 세포가 특화 또는 분화되는 일반적인 발생학의 모델과는 다르게 세포 간의 상호작용으로 인하여 분화되는 세포가 확률적(stochastic)으로 결정된다.
    * 따라서 같은 분화능을 갖는 세포들이 특정 세포로 분화될 확률을 같다.
    * 측면 억제 과정에서 가장 중요한 인자로는 Notch 수용체와 그 리간드인 Delta가 있다.
    * 출처: `[네이버 지식백과] 측면 억제 [lateral inhibition] (동물학백과) <https://terms.naver.com/entry.nhn?docId=5669842&cid=63057&categoryId=63057>`_

* Label-preserving transformation

    * In general we want the augmented images to be fairly dissimilar to the originals.
    However, we need to be careful that the augmented images still visually represent the same concept (and thus label).
    * If a pipeline only produces output images that have this property we call this pipeline label-preserving.
    * 출처: `Augmentor.jl <https://augmentorjl.readthedocs.io/en/latest/introduction/background.html>`_