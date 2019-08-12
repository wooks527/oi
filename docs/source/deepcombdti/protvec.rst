========
Protvec
========

ProtVec is a representation of proteins through protein sequences. First, we need a large corpus to train distributed representation of biological sequences. Then, to break the sequences into sub sequences and we can generate 3 lists of shifted non-overlapping words.

.. figure:: img/protvec/split_prot_seqs.png
    :align: center
    :scale: 70%

Finally, we train the embedding based on 1,640,370 (546,790 × 3) sequences of 3-grams through a Skip-gram model.

.. figure:: img/protvec/skip_gram.png
    :align: center
    :scale: 70%

Utilization
===========

ProtVec can be utilized to various situations such as protein family classification.

* Each sequence is represented as the summation of the vector representation of overlapping 3-grams
* For each family type, the same number of instances from Swiss-Prot are selected randomly for negative examples

Reference
==========

* https://arxiv.org/pdf/1503.05140
