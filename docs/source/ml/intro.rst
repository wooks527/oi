=============
Introduction
=============

Definition
============

There are several definition of Machile learnings:

* Arthur Samuel (1959)

    * The field of study that gives computers the ability to learn without being explicitly programmed.

* Tom Mitchel (1998)

    * A computer program is said to learn from experience E with respect to some class of task T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E


Types of ML
============

In ML, there are three algorithms:

.. figure:: img/intro/ml_algorithms.png
    :align: center
    :scale: 40%

Supervised learning
********************

**Point**

* "Right answers" are given

**Types**

* Regression (:doc:`Link <linear_regression>`)
* Classification.

-----------
Regression
-----------

* Map input variables to some continuous functions to predict results within a continuous output
* Example: Housing price prediction

.. figure:: img/intro/regression_ex.png
    :align: center
    :scale: 40%

--------------
Classification
--------------

* Map input variables into discrete categories to predict results within a discrete output
* Example: Breast cancer or Test grade (A, B, C, D, F)

.. figure:: img/intro/classification_ex1.png
    :align: center
    :scale: 40%

.. figure:: img/intro/classification_ex2.png
    :align: center
    :scale: 40%

Unsupervised learning
**********************

**Point**

* Allow us to approach problems with little or no idea what our results should look like
* Derive the structure from data where we don't necessarily know the effect of the variables
* No feedback based on the prediction results

**Types**

* Clustering
* Non-clustering

-----------
Clustering
-----------

* Find groups with patterns being close to each other
* Example: Google news clustering

.. figure:: img/intro/clustering_ex.png
    :align: center
    :scale: 40%

---------------
Non-clustering
---------------

* Find the structure in a chaotic environment
* Example: Cocktail party problem

.. figure:: img/intro/non-clustering_ex.png
    :align: center
    :scale: 40%


Reinforcement learning
***********************

Reinforcement learning (RL) is an area of machine learning concerned with how software agents ought to take actions in an environment so as to maximize some notion of cumulative reward (Ref.: `Wikipedia <https://en.wikipedia.org/wiki/Reinforcement_learning>`_).

.. figure:: img/intro/reinforcement_learning.png
    :align: center
    :scale: 40%


:h2:`출처`

* `One page summary <https://docs.google.com/document/d/1xXpvTas6hPVzixJcUIlihBr3DQet8KhHcFrkZ2SX9yE/edit?usp=sharing>`_
* `Coursera, Machine Learning <https://www.coursera.org/learn/machine-learning>`_
