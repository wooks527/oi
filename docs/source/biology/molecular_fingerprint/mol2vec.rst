Mol2vec
========

======================
Introduction
======================

Mol2vec represents a novel way of embedding compound substructures as information rich vectors inspired by Natural Language Processing (NLP) techniques.
New compounds can be described by summing the substructure vectors retrieved from a pretrained Mol2vec model.


======================
Generation of Mol2vec
======================

.. figure:: ../img/molecular_fingerprint/generation_of_mol2vec.png
    :scale: 30%


**Compound encoding.**
Molecules were considered as sentences and substructures as words.
To obtain words for each molecule, the Morgan algorithm was used to generate all atom identifiers.
Identifiers have same order of canonical SMILES.
All rare words that occurred less than three times in the corpus were replaced with a string "UNSEEN".
The distribution of "UNSEEN" in the corpus is random, and hence, a vector close to zero is usually learned.

They used Skip-gram because it captures spatial relationships better as a result of the weighting of words in the context.
Higher dimensionality of embeddings also had a beneficial effect on the performances, while varying the window size had almost no effect.
The window size is 10 and 20 and second one is for radius 1, because at radius 1 each atom is represented twice via Morgan identifiers.
Finally, 300-dimensional embeddings were generated for all combinations.


=======================
Application of Mol2vec
=======================

.. figure:: ../img/molecular_fingerprint/application_of_mol2vec.png
    :scale: 30%

The vector for a molecule is finally obtained by summing all of the vectors of the Morgan substructures of the molecule.
If an unknown identifier occurs during featurization of the new data, the “UNSEEN” vector is employed.


==================================
Prediction of the ESOL solubility
==================================

.. figure:: ../img/molecular_fingerprint/prediction_of_esol_solubility.png
    :scale: 50%


**Reference**
    * Jaeger, S., et al. Mol2vec: Unsupervised Machine Learning Approach with Chemical Intuition. Journal of Chemical Information and Modeling. 2017.12.
