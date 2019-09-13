===============
Regularization
===============

The problem of overfitting
==========================

Consider the problem of predicting :math:`y` from :math:`x \in R.` The leftmost figure below shows the result of fitting a :math:`y = θ_0 + θ_1 x` to a dataset. We see that the data doesn’t really lie on straight line, and so the fit is not very good.

Instead, if we had added an extra feature :math:`x^2,` and fit :math:`y = \theta_0 + \theta_1x + \theta_2x^2,` then we obtain a slightly better fit to the data (See middle figure). Naively, it might seem that the more features we add, the better.

However, there is also a danger in adding too many features: The rightmost figure is the result of fitting a :math:`5^{th}` order polynomial :math:`y = \sum_{j=0} ^5 \theta_j x^j.` We see that even though the fitted curve passes through the data perfectly, we would not expect this to be a very good predictor of, say, housing prices (:math:`y`) for different living areas (:math:`x`).

.. figure:: img/regularization/overfitting.png
  :align: center
  :scale: 100%

Without formally defining what these terms mean, we’ll say the figure on the left shows an instance of **underfitting**—in which the data clearly shows structure not captured by the model—and the figure on the right is an example of **overfitting**.


Underfitting
************

Underfitting, or high bias, is when the form of our hypothesis function :math:`h` maps poorly to the trend of the data. It is usually caused by a function that is **too simple** or uses **too few features**.


Overfitting
***********

At the other extreme, overfitting, or high variance, is caused by a hypothesis function that fits the available data but does not generalize well to predict new data. It is usually caused by a complicated function that creates a lot of unnecessary curves and angles unrelated to the data.

This terminology is applied to both linear and logistic regression. There are two main options to address the issue of overfitting:

1) Reduce the number of features:

* Manually select which features to keep
* Use a model selection algorithm

2) Regularization

* Keep all the features, but reduce the magnitude of parameters :math:`\theta_j`
* Regularization works well when we have a lot of slightly useful features


Cost Function
=============

If we have overfitting from our hypothesis function, we can reduce the weight that some of the terms in our function carry by increasing their cost. We wanted to make the following function more quadratic:

.. rst-class:: centered
    
    :math:`\theta_0 + \theta_1x + \theta_2x^2 + \theta_3x^3 + \theta_4x^4`

We'll want to eliminate the influence of :math:`\theta_3x^3.` Without actually getting rid of these features or changing the form of our hypothesis, we can instead modify our cost function:

.. rst-class:: centered

    :math:`min_\theta\ \dfrac{1}{2m}\sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})^2 + 1000\cdot\theta_3^2 + 1000\cdot\theta_4^2`

We've added two extra terms at the end to inflate the cost of :math:`\theta_3` and :math:`\theta_4.` Now, in order for the cost function to get close to zero, we will have to reduce the values of :math:`\theta_3` and :math:`\theta_4` to near zero. This will in turn greatly reduce the values of :math:`\theta_3x^3` and :math:`\theta_4x^4` in our hypothesis function.

As a result, we see that the new hypothesis (depicted by the pink curve) looks like a quadratic function but fits the data better due to the extra small terms :math:`\theta_3x^3` and :math:`\theta_4x^4.`

.. figure:: img/regularization/cost_function.png
  :align: center
  :scale: 100%

We could also regularize all of our theta parameters in a single summation as:

.. rst-class:: centered

    :math:`min_\theta\ \dfrac{1}{2m}\ \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})^2 + \lambda\ \sum_{j=1}^n \theta_j^2`

The :math:`\lambda,` or lambda, is the regularization parameter. It determines how much the costs of our theta parameters are inflated.

Using the above cost function with the extra summation, we can smooth the output of our hypothesis function to reduce overfitting. If lambda is chosen to be too large, it may smooth out the function too much and cause underfitting. Hence, what would happen if :math:`\lambda = 0` or is too small?


Regularized Linear Regression
==============================

We can apply regularization to both linear regression and logistic regression. We will approach linear regression first.

Gradient Descent
We will modify our gradient descent function to separate out :math:`\theta_0` from the rest of the parameters because we do not want to penalize :math:`\theta_0.`

Repeat {

    :math:`\theta_0 := \theta_0 - \alpha \frac{1}{m} \sum\limits_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)}) x_0^{(i)}`

    :math:`\theta_j := \theta_j - \alpha [(\frac{1}{m} \sum\limits_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)}) + \lambda_m \theta_j]\ where\ j \in \{1, 2, \cdots n\}`

}

The term :math:`\frac{\lambda}{m}\theta_j` performs our regularization. With some manipulation our update rule can also be represented as:

.. rst-class:: centered

    :math:`\theta_j := \theta_j(1 - \alpha\frac{\lambda}{m}) - \alpha\frac{1}{m}\sum_{i=1}^m(h_\theta(x^{(i)}) - y^{(i)})x_j^{(i)}`

The first term in the above equation, :math:`1 - \alpha\frac{\lambda}{m}` will always be less than 1. Intuitively you can see it as reducing the value of :math:`\theta_j` by some amount on every update. Notice that the second term is now exactly the same as it was before.

**Normal Equation**

Now let's approach regularization using the alternate method of the non-iterative normal equation.

To add in regularization, the equation is the same as our original, except that we add another term inside the parentheses:

.. rst-class:: centered

    :math:`\theta = (X^T X + \lambda \cdot L)^{-1} X^T y`
    
    :math:`where\ L = \begin{bmatrix} 0 &  &  &  &   \\ & 1 &  &  &  \\ &  & 1 &  &  \\ &  &  & \ddots &  \\ &  &  &  & 1 \end{bmatrix}`

:math:`L` is a matrix with 0 at the top left and 1's down the diagonal, with 0's everywhere else. It should have dimension :math:`(n+1)×(n+1).` Intuitively, this is the identity matrix (though we are not including :math:`x_0`), multiplied with a single real number :math:`\lambda.`

Recall that if :math:`m < n,` then :math:`X^TX` is non-invertible. However, when we add the term :math:`\lambda \cdot L,` then :math:`X^TX + \lambda \cdot L` becomes invertible.


Regularized Logistic Regression
===============================

We can regularize logistic regression in a similar way that we regularize linear regression. As a result, we can avoid overfitting. The following image shows how the regularized function, displayed by the pink line, is less likely to overfit than the non-regularized function represented by the blue line:

.. figure:: img/regularization/regularized_lr.png
    :align: center
    :scale: 100%


Cost Function
*************

Recall that our cost function for logistic regression was:

.. rst-class:: centered

    :math:`J(\theta) = - \frac{1}{m} \sum_{i=1}^m \large[ y^{(i)}\ \log (h_\theta (x^{(i)})) + (1 - y^{(i)})\ \log (1 - h_\theta(x^{(i)})) \large]`

We can regularize this equation by adding a term to the end:

.. rst-class:: centered

    :math:`J(\theta) = - \frac{1}{m} \sum_{i=1}^m \large[ y^{(i)}\ \log (h_\theta (x^{(i)})) + (1 - y^{(i)})\ \log (1 - h_\theta(x^{(i)}))\large] + \frac{\lambda}{2m}\sum_{j=1}^n \theta_j^2`

The second sum, :math:`\sum_{j=1}^n \theta_j^2` means to explicitly exclude the bias term, :math:`\theta_0.` I.e. the :math:`\theta` vector is indexed from 0 to n (holding :math:`n+1` values, :math:`\theta_0` through :math:`\theta_n`), and this sum explicitly skips :math:`\theta_0,` by running from 1 to n, skipping 0. Thus, when computing the equation, we should continuously update the two following equations:

Repeat {

    :math:`\theta_0 := \theta_0 - \alpha \frac{1}{m} \sum\limits_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)}) x_0^{(i)}`

    :math:`\theta_j := \theta_j - \alpha [(\frac{1}{m} \sum\limits_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)}) + \frac{\lambda}{m} \theta_j]\ where\ j \in \{1, 2, \cdots n\}`

}


Bias vs. Variance
==================

In this section we examine the relationship between the degree of the polynomial :math:`d` and the underfitting or overfitting of our hypothesis.

* We need to distinguish whether **bias** or **variance** is the problem contributing to bad predictions.
* :blue:`High bias` is :blue:`underfitting` and :red:`high variance` is :red:`overfitting`. Ideally, we need to find a **golden mean** between these two.

The training error will tend to decrease as we increase the degree :math:`d` of the polynomial.

At the same time, the cross validation error will tend to decrease as we increase :math:`d` up to a point, and then it will increase as :math:`d` is increased, forming a convex curve.

* High bias (underfitting)
    
    * Both :math:`J_{train}(\theta)` and :math:`J_{CV}(\theta)` will be high.
    * :math:`J_{CV}(\theta) \approx J_{train}(\theta).`

* High variance (overfitting)

    * :math:`J_{train}(\theta)` will be low.
    * :math:`J_{CV}(\theta)` will be much greater than :math:`J_{train}(\theta).`

The is summarized in the figure below:

.. figure:: img/regularization/bias_vs_variance.png
    :align: center
    :scale: 100%


Regularization and bias/variance
*********************************

In the below figure, we see that as :math:`\lambda` increases, our fit becomes more rigid. On the other hand, as :math:`\lambda` approaches 0, we tend to over overfit the data.

.. figure:: img/regularization/regularization_and_bias_variance.png
    :align: center
    :scale: 80%

So how do we choose our parameter :math:`\lambda` to get it 'just right'? In order to choose the model and the regularization term :math:`\lambda`, we need to:

* Initialization

    * Create a list of :math:`\lambda s`  (i.e. :math:`\lambda \in {0,0.01,0.02,0.04,0.08,0.16,0.32,0.64,1.28,2.56,5.12,10.24}).`
    * Create a set of models with different degrees or any other variants.

* Search the best :math:`\lambda` and :math:`\theta`

    * Iterate through the :math:`\lambda s` and for each :math:`\lambda s` go through all the models to learn some :math:`\theta`.
    * Compute the cross validation error using the learned :math:`\theta` (computed with :math:`\lambda`) on the :math:`J_{CV}(\theta)` without regularization or :math:`\lambda` = 0.
    * Select the best combo that produces the lowest error on the cross validation set.

* Apply to the  test set
    
    * Using the best combo :math:`\theta` and :math:`\lambda`, apply it on :math:`J_{test}(\theta)` to see if it has a good generalization of the problem.


Learning Curves
****************

Training an algorithm on a very few number of data points (such as 1, 2 or 3) will easily have 0 errors because we can always find a quadratic curve that touches exactly those number of points. Hence:

* As the training set gets larger, the error for a quadratic function increases.
* The error value will plateau out after a certain :math:`m`, or training set size.

----------
High bias
----------

* Low training set size

    * :math:`J_{train}(\theta)` will be low and :math:`J_{CV}(\theta)` will be high.

* Large training set size

    * Both :math:`J_{train}(\theta)` and :math:`J_{CV}(\theta)` will be high with :math:`J_{train}(\theta) \approx J_{CV}(\theta)`.

If a learning algorithm is suffering from **high bias**, getting :strike:`more training data` will not (by itself) help much.

.. figure:: img/regularization/learning_curve_high_bias.png
    :align: center
    :scale: 100%

--------------
High variance
--------------

* Low training set size

    * :math:`J_{train}(\theta)` will be low and :math:`J_{CV}(\theta)` will be high.

* Large training set size

    * :math:`J_{train}(\theta)` increases with training set size and :math:`J_{CV}(\theta)` continues to decrease without leveling off.
    * :math:`J_{train}(\theta) < J_{CV}(\theta)` but the difference between them remains significant.

If a learning algorithm is suffering from **high variance**, getting **more training data** is likely to help.

.. figure:: img/regularization/learning_curve_high_variance.png
    :align: center
    :scale: 100%


Deciding What to Do Next Revisited
***********************************

A decision process can be broken down as follows:

===============================  =============  ==================
Decision                         Fix high bias  Fix high variance
===============================  =============  ==================
Getting more training examples   X              O
Trying smaller sets of features  X              O
Adding features                  O              X
Adding polynomial features       O              X
Decreasing λ                     O              X
Increasing λ                     X              O
===============================  =============  ==================

---------------------------
Diagnosing Neural Networks
---------------------------

* A neural network with fewer parameters is prone to underfitting. It is also computationally cheaper.
* A large neural network with more parameters is prone to overfitting. It is also computationally expensive. In this case you can use regularization (increase λ) to address the overfitting.

Using a single hidden layer is a good starting default. You can train your neural network on a number of hidden layers using your cross validation set. You can then select the one that performs best.

-------------------------
Model Complexity Effects
-------------------------

* Lower-order polynomials (low model complexity)

    * Have high bias and low variance.
    * The model fits poorly consistently.

* Higher-order polynomials (high model complexity)

    * Fit the training data extremely well and the test data extremely poorly.
    * These have low bias on the training data, but very high variance.

In reality, we would want to choose a model somewhere in between, that can generalize well but also fits the data reasonably well.


Reference
===========

* `One page summary <https://docs.google.com/document/d/14wRFf7DJXR2zhh5L8VH4Jyfr4Pw2ry80YvhuoQlYrrM/edit?usp=sharing>`_
* `Coursera, Machine Learning <https://www.coursera.org/learn/machine-learning>`_
