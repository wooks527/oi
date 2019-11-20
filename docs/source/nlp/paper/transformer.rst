============
Transformer
============

Transformer는 "Attention Is All You Need"라는 논문에서 제안한 모델이고, 이 모델은 기존 Translation 문제를 Attention만 이용하여 해결했다.


Model architecture
===================

.. figure:: ../img/paper/transformer/architecture.png
    :align: center
    :scale: 25%

위 그림에서 좌측이 Encoder, 우측이 Decoder 부분이라고 생각하면 된다. 그리고 Transformer의 특징은 다음과 같다.

* Scaled dot-product attention과 Multi-head attention 사용
* 병렬 계산에 용이함
* 단어의 위치를 표현하기 위해 Positional encoding 사용

지금부터는 각 구조를 하나씩 살펴보려고 한다.


Inputs and outputs
*******************

Input과 Output은 모두 각 Sequence를 Word 기반으로 One-hot encoding한 Vector이다.


Embedding
**********

One-hot encoding vector들을 Embedding vector로 변경한다 (차원 축소).


Positional encoding
********************

전체 Sequence의 길이 중 상대적 위치에 따라 고유 벡터를 생성하여 Embedding vector에 더해 주는 부분이고, 관련 수식은 아래와 같다.

.. rst-class:: centered

    :math:`PE_{(pos,2i)} = sin(pos/10000^{2i/d_{model}})`

    :math:`PE_{(pos,2i+1}) = cos(pos/10000^{2i/d_{model}})`


Multi-head attention
*********************

.. figure:: ../img/paper/transformer/mha.png
    :align: center
    :scale: 25%


Scaled dot-product attention
*****************************

.. figure:: ../img/paper/transformer/sdpa.png
    :align: center
    :scale: 25%


Masked multi-head attention
****************************

.. figure:: ../img/paper/transformer/mha.png
    :align: center
    :scale: 25%



Position-wise feed forward
***************************

왜 하는지 아직 이해 못함...


Add & Norm
***********

Feed forward 결과와 Feed forward 이전을 더하고 Normalization 한다.


Linear and softmax
********************

Linear를 통해 출력 단어 종류로 맞추고, Softmax를 이용하여 단어를 분류한다.



Reference
==========

* `Attention Is All You Need <https://arxiv.org/abs/1706.03762>`_
