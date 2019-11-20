====================
Dialog Manager (DM)
====================

Examples
=========

Conditional language modeling: seq2seq model
*********************************************

The "right" (and also the most ambitious) way to implement a conversational chat-bot would be to build a seq2seq model. Generally, you will use encoder-decoder-attention architecture, but you need to decide on specific details of the architecture and tune hyperparameters. This `TF tutorial on NMT <https://www.tensorflow.org/tutorials/seq2seq>`_ is a good way to check how things should be better implemented.


Selective model: embeddings-based ranking
*******************************************

One more way to tackle the problem is to build a ranking system that scores predefined replicas (e.g. from Twitter) given the question. Roughly, this is how `Chatterbot <https://chatterbot.readthedocs.io/en/stable/>`_ works. Specifically, you can learn unsupervised sentence embeddings (e.g. sent2vec) on dialogue corpus or use question-answer pairs to train supervised embeddings (e.g. StarSpace). Anyways, will then score all possible answers and reply with the most similar one.


Reference
==========

* `Coursera, Natural Language Processing (NLP) <https://www.coursera.org/learn/language-processing>`_
