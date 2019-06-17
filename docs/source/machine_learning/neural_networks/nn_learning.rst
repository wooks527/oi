Neural networks: Learning
==========================

==============
Cost function
==============

.. figure:: ../img/neural_networks/nn_learning/neural_networks.png
  :align: center
  :scale: 80%

  **Neural network (Classification)**

Let's first define a few variables that we will need to use:

* :math:`L` = total number of layers in the network
* :math:`s_l` = number of units (not counting bias unit) in layer :math:`l`
* :math:`K` = number of output units/classes

Recall that in neural networks, we may have many output nodes. We denote :math:`h_\theta (x)_k` as being a hypothesis that results in the :math:`k^{th}` output. Our cost function for neural networks is going to be a generalization of the one we used for logistic regression. Recall that the cost function for regularized logistic regression was:

.. rst-class:: centered
  
  :math:`J(\theta) = - \frac{1}{m} \sum_{i=1}^m [ y^{(i)}\ \log (h_\theta (x^{(i)})) + (1 - y^{(i)})\ \log (1 - h_\theta(x^{(i)}))] + \frac{\lambda}{2m}\sum_{j=1}^n \theta_j^2`
​	 
For neural networks, it is going to be slightly more complicated:

.. rst-class:: centered
  
  :math:`J(\theta) = −\frac{1}{m} \sum_{i=1}^m \sum_{k=1}^{K} \big[ y(i)k \log((h_\theta (x^(i))_k) + (1 − y_k^{(i)}) \log(1 − (h_\theta (x^{(i)}))_k) \big] + \frac{\lambda}{2m} \sum_{l=1}^{L−1} \sum_{i=1}^{s_l} \sum_{j=1}^{s_l+1} (\theta_{j,i}^{(l)})^2`

We have added a few nested summations to account for our multiple output nodes. In the first part of the equation, before the square brackets, we have an additional nested summation that loops through the number of output nodes.

In the regularization part, after the square brackets, we must account for multiple theta matrices. The number of columns in our current theta matrix is equal to the number of nodes in our current layer (including the bias unit). The number of rows in our current theta matrix is equal to the number of nodes in the next layer (excluding the bias unit). As before with logistic regression, we square every term.

Additionally, suppose we want to try to minimize :math:`J(\theta)` as a function of :math:`\theta` , using one of the advanced optimization methods (fminunc, conjugate gradient, BFGS, L-BFGS, etc.). What do we need to supply code to compute (as a function of :math:`\theta` )? We need to add :math:`J(\theta)` and the (partial) derivative terms :math:`\frac{\partial}{\partial \theta_{ij}^{(l)}}` for every :math:`i, j, l` .

Note:

* The double sum simply adds up the logistic regression costs calculated for each cell in the output layer
* The triple sum simply adds up the squares of all the individual :math:`\theta s` in the entire network
* The i in the triple sum does not refer to training example :math:`i`


===========
Reference
===========

* https://www.coursera.org/learn/machine-learning