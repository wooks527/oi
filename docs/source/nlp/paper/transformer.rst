============
Transformer
============

Transformer는 "Attention Is All You Need"라는 논문에서 제안한 모델이고, 이 모델은 기존 Translation 문제를 RNN, CNN을 활용하지 않고 Attention만 이용하여 해결했다.

Previous model: Seq2seq + Attention
====================================

이전 Translation 문제를 해결하는데 사용한 대표적인 모델은 Seq2seq 이다. 그 내용은 :doc:`링크 <../encoder-decoder-attention_architecture>` 에서 확인할 수 있다.

위 링크를 통해 알 수 있듯이 Seq2seq 모델은 RNN을 활용했고, 추후에 Attention 개념을 도입하더라도 그 연산량이 많다. 그래서 Transformer 모델에서는 RNN, CNN을 활용하지 않았고, 가벼우면서도 성능이 좋은 모델임을 여러가지 실험으로 밝혔다.


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


Input and output embedding
***************************

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

Feed forward 결과와 Feed forward 이전을 더하고 Normalization 한다. 이 때 Layer normalization을 이용한다 (추후 정리 예정).


Linear and softmax
********************

Linear를 통해 출력 단어 종류로 맞추고, Softmax를 이용하여 단어를 분류한다.



Reference
==========

* `Attention Is All You Need <https://arxiv.org/abs/1706.03762>`_
