Neural graph fingerprint
========================

=============
Introduction
=============

In most drug discovery by virtual screening, drugs need to be encoded as a fixed size vector, called a molecular fingeprint.
One of the popular molecular fingerprint is extended connectivity fingerprint (ECFP).
In this paper, they replace the bottom layer of this stack - the function that computes molecular fingerprint vecotrs - with a differentiable neural network whose input is a graph representing the original molecule.

These neural graph fingerprints offer several advantages over fixed fingerprints:

    * **Predictive performance.** Machine optimized fingerprints can provide substantially better predictive performance than fixed fingerprints.
    * **Parsimony.** Differentiable fingerprints can be optimized to encode only relevant features, reducing downstream computation and regularization requirements.
    * **Interpretability.** Each feature of a neural graph fingerprint can be activated by similar but distinct molecular fragments, making the feature representation more meaningful.


=====================================
Creating a differentiable fingerprint
=====================================

This section describes the replacement of each discrete operation in ECFP with a differentiable analog.

.. f igure:: img/neural_graph_fingerprint_algorithm.PNG
    :scale: 70%

    Pseudocode of circular fingerprints (left) and neural graph fingerprints (right).

**Hashing.** They replace the hash operation with a single layer of a neural network.
Using a smooth function allows the activations to be similar when the local molecular structure varies in unimportant ways.

**Indexing.** We use the softmax operation as a differentiable analog of indexing.
In essence, each atom is asked to classify itself as belonging to a single category.
The sum of all these classification label vectors produces the final fingerprint.
This operation is analogous to the pooling operation in standard convolutional neural networks.

**Canonicalization.** An alternative to canonicalization is to apply a permutation-invariant function, such as summation.
In the interests of simplicity and scalability, we chose summation.


=====================================
Code
=====================================


========
Install
========

::

    git clone https://github.com/HIPS/neural-fingerprint.git
    cd neural-fingerprint
    sudo python setup.py install


=========
Overview
=========

특정 Molecular property를 잘 예측하는 Weight 계산
    * Hidden layer 2개 사용 (Dimension 100)
해당 Weight를 이용하여 fingerprint 생성


**Reference**
    * Duvenaud, D., et al. Convolutional Networks on Graphs for Learning Molecular Fingerprints. The 28th International Conference on Neural Information Processing Systems. 2018.12
