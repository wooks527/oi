=============================
Large scale machine learning
=============================

Learning with large datasets
=============================

One of the best ways to get a **high performance** machine learning system, is if you take a low-bias learning algorithm, and train that on **a lot of data**. So, we want to use a lot of dataset.

Example: classification between confusable words
*************************************************

.. rst-class:: centered

  For breakfast I ate _____ eggs.

We can choose one of {to, two, too} for above sentence and below figure describe how some algorithms performed through the dataset size. In conclusion, "It's not who has the best algorithm that wins. It's who has the most data".

.. figure:: img/large_scale_ml/dataset_importance.png
  :align: center
  :scale: 80%


Large dataset
*************

**Problem:**

When :math:`M` is a hundred million, you need to carry out a summation over a hundred million terms, in order to compute these derivatives terms and to perform a single step of decent. There are many methods to compute this derivative such as Stochastic Gradient Descent (SGD).

.. rst-class:: centered

  :math:`\theta_j := \theta_j - \alpha \frac{1}{m} \sum_{i=1}^{m} (h_\theta (x^{(i)}) - y^{(i)}) x_j^{(i)}`

----------------------------
Why a lot of data is better?
----------------------------

How can you tell if using all of the data is likely to perform much better than using a small subset of the data? The answer is to plot a learning curve for a range of values of m and verify that the algorithm has high variance when m is small.

Like below left figure, when m is big, the algorithm has high variance. But when m is small, the algorithm has high bias like below right figure (:doc:`Bias vs. Variance <advice_for_applying_ml>`). So, we will be more confident that adding extra training examples would improve performance.

.. figure:: img/large_scale_ml/why_a_lot_of_data_is_better.png
  :align: center
  :scale: 80%


Stochastic Gradient Descent (SGD)
=================================

Gradient Descent로 Loss Function을 계산할 때 전체 Train set을 사용하는 것을 **Batch Gradient Descent** 라고 한다. 그러나 이렇게 계산을 할 경우 한번 step을 내딛을 때 전체 데이터에 대해 Loss Function을 계산해야 하므로 너무 많은 계산량이 필요하다. 이를 방지하기 위해 보통은 Stochastic Gradient Descent (SGD) 라는 방법을 사용한다.

이 방법에서는 Loss function을 계산할 때 전체 데이터 (Batch) 대신 일부 조그마한 데이터의 모음 (Mini-batch)에 대해서만 Loss function을 계산한다. 이 방법은 Batch gradient descent 보다 다소 부정확할 수는 있지만, 훨씬 계산 속도가 빠르기 때문에 같은 시간에 더 많은 Step을 갈 수 있으며 여러 번 반복할 경우 보통 Batch의 결과와 유사한 결과로 수렴한다. 또한, SGD를 사용할 경우 Batch Gradient Descent에서 빠질 Local minima에 빠지지 않고 더 좋은 방향으로 수렴할 가능성도 있다.


Stochastic gradient descent convergence
========================================


Other optimizations
===================

There are various optimization methods to improve performances of SGD such as AdaGrad, Adam and so on (:doc:`Optimization <optimization>`)


Advanced topics
================

**Online learning**


**Map reduce and data parallelism**



Reference
===========

* https://www.coursera.org/learn/machine-learning
* http://shuuki4.github.io/deep%20learning/2016/05/20/Gradient-Descent-Algorithm-Overview.html


