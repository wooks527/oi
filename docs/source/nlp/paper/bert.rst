=====
BERT
=====

BERT (Bidirectional Encoder Representations from Transformer)의 아키텍처는 "Attention is all you need"에서 소개된 Transformer를 사용하지만, pre-training과 fine-tuning 시의 아키텍처를 조금 다르게하여 Transfer learning을 용이하게 만드는 것이 핵심입니다. 여기서 Transfer learning이란 이미 잘 훈련된 모델을 이용하여 목적에 맞게 모델을 약간 변경하여 사용하는 방법이다.


Pre-training
=============

MLM
****

MLM (Masked Language Model)은 input에서 무작위하게 몇개의 token을 mask 시킵니다. 그리고 이를 Transformer 구조에 넣어서 주변 단어의 context만을 보고 mask된 단어를 예측하는 모델입니다. 

.. figure:: ../img/paper/bert/mlm.png
    :align: center
    :scale: 70%


Next sentence prediction
*************************

BERT에서는 corpus에서 두 문장을 이어 붙여 이것이 원래의 corpus에서 바로 이어 붙여져 있던 문장인지를 맞추는 Binarized next sentence prediction task를 수행한다. 이러한 작업을 하는 이유는 NLP task중에 Question Answering (QA)나 Natural Language Inference (NLI)와 같이 두 문장 사이의 관계를 이해하는 것이 중요한 것들이기 때문이다.


Fine-tuning
============

.. figure:: ../img/paper/bert/fine-tuning.png
    :align: center
    :scale: 50%



Reference
==========

* `Minho-Park7, BERT 논문정리 <https://mino-park7.github.io/nlp/2018/12/12/bert-%EB%85%BC%EB%AC%B8%EC%A0%95%EB%A6%AC/?fbclid=IwAR3S-8iLWEVG6FGUVxoYdwQyA-zG0GpOUzVEsFBd0ARFg4eFXqCyGLznu7w>`_
