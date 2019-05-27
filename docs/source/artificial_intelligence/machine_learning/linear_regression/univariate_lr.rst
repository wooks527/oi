Univariate linear regression
=============================

=======================
Example: Housing prices
=======================

.. figure:: img/univariate_lr_ex.png
    :align: center
    :scale: 40%


=========
Process
=========

.. figure:: img/univariate_lr_process.png
    :align: center
    :scale: 40%


==============================
Notation of training set
==============================

.. figure:: img/notation_of_training_set.png
    :align: center
    :scale: 40%


| m = The number of training examples (samples)
| x's = Input variables (Features)
| y's = Output variables (Target variables)
| (x, y) = One training example
| (x\ :sub:`i`\, y\ :sub:`i`\) = ith training example


=======================
Hypothesis function
=======================

.. figure:: img/hypothesis_function.png
    :align: center
    :scale: 40%


====================
Cost function
====================

**Idea**

Choose 𝜽\ :sub:`0`\, 𝜽\ :sub:`1`\ so that ℎ\ :sub:`𝜃`\ (𝑥) is close to 𝑦 for training samples.

**Examples**

.. figure:: img/cost_function_ex.png
    :align: center
    :scale: 50%


**Method**

Minimize the squared error function.

.. figure:: img/cost_function_equation.png
    :align: center
    :scale: 40%


==================
Gradient descent
==================

**Idea**
    * Make arbitrary function  𝑱(𝜽\ :sub:`0`\, 𝜽\ :sub:`𝟏`\)
    * Find (𝐦𝐢𝐧)┬(𝜽\ :sub:`0`\, 𝜽\ :sub:`1`\)⁡𝑱(𝜽\ :sub:`𝟎`\, 𝜽\ :sub:`𝟏`\)

**Process**
    * Start with some 𝜽\ :sub:`0`\, 𝜽\ :sub:`𝟏`\
    * Keep changing 𝜽\ :sub:`0`\, 𝜽\ :sub:`𝟏`\ to reduce 𝐉(𝜽\ :sub:`0`\, 𝜽\ :sub:`𝟏`\) until we hopefully end up at a minimum

**Types**
    * Batch gradient descent
        * Each step of gradient descent uses all the training set.
    * Stochastic gradient descent (SGD)
        * Each step of gradient descent uses partial of the training set called mini-batch.

**Algorithm**

.. figure:: img/gradient_descent_algorithm.png
    :align: center
    :scale: 20%


.. figure:: img/gradient_descent_condition.png
    :align: center
    :scale: 40%


Should be updated simultaneously!!

**Linear equation movement**

.. figure:: img/gradient_descent_move.png
    :align: center
    :scale: 40%


**Learning rate 𝜶**

.. figure:: img/gradient_descent_learning_rate.png
    :align: center
    :scale: 40%


**Fixed learning rate 𝜶**

.. figure:: img/gradient_descent_fixed_learning_rate.png
    :align: center
    :scale: 40%


**Local minimum problem**

.. figure:: img/local_minimum_problem.png
    :align: center
    :scale: 40%


**Final algorithm for the linear regression**

.. figure:: img/gradient_descent_algorithm_for_linear_regression.png
    :align: center
    :scale: 50%


이 부분은 추후에 보충 필요 (과정)



**Reference**
    * https://www.coursera.org/learn/machine-learning
