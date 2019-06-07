Logistic regression
====================

==============
Classification
==============

**Example**

* Email: Spam / Not spam?
* Online transactions: Fraudulent (Yes / No)?
* Tumor: Malignant / Benign?


**Two classes**

:math:`y \in {0, 1}`

* 0: "Negative class" (e.g. benign tumor)
* 1: "Positive class" (e.g. malignant tumor)


**Method**

* If ℎ𝜃≥0.5 , 𝑝𝑟𝑒𝑑𝑖𝑐𝑡 "y = 1"
* If ℎ𝜃<0.5 , 𝑝𝑟𝑒𝑑𝑖𝑐𝑡 "y = 0"

.. figure:: img/logistic_regression/classification.png
  :align: center
  :scale: 40%


**Problem:**

* Linear regression

  * :math:`h_{\theta}(x)\ can\ be\ > 1\ or\ < 0`

* Logistic regression

  * :math:`0 \leq h_{\theta}(x) \leq 1`
  * Logistic regression is a classification, but people confused that it is a regression because of its name


**Check**

Which of the following statements is true?

(X) If linear regression doesn't work on a classification task as in the previous example shown in the video, applying feature scaling may help.

(X) If the training set satisfies :math:`0 \leq y^{(i)} \leq 1`  for every training example :math:`(x^{(i)},y^{(i)})`, then linear regression's prediction will also satisfy :math:`0 \leq h_\theta(x) \leq 1` for all values of :math:`x`.

(X) If there is a feature :math:`x` that perfectly predicts :math:`y`, i.e. if :math:`y=1` when :math:`x\geq c` and :math:`y=0` whenever :math:`x < c` (for some constant :math:`c`), then linear regression will obtain zero classification error.

(O) None of the above statements are true.


**Reading: Classification**

To attempt classification, one method is to use linear regression and map all predictions greater than 0.5 as a 1 and all less than 0.5 as a 0. However, this method doesn't work well because classification is not actually a linear function.

The classification problem is just like the regression problem, except that the values we now want to predict take on only a small number of discrete values. For now, we will focus on the **binary classification problem** in which :math:`y` can take on only two values, 0 and 1. (Most of what we say here will also generalize to the multiple-class case.) For instance, if we are trying to build a spam classifier for email, then :math:`x^{(i)}` may be some features of a piece of email, and :math:`y` may be 1 if it is a piece of spam mail, and 0 otherwise. Hence, :math:`y \in {0,1}`. 0 is also called the negative class, and 1 the positive class, and they are sometimes also denoted by the symbols “-” and “+.” Given :math:`x^{(i)}`, the corresponding :math:`y^{(i)}` is also called the label for the training example.


=========================
Hypothesis Representation
=========================

**Logistic regression model**

:math:`h_{\theta}(x) = g(\theta^{T}x),\ \ 0 \leq h_{\theta}(x) \leq 1`

Use sigmoid function (=Logistic function) for binary classification

:math:`h_{\theta}(x) = \frac{1}{1 + e^{-\theta^{T}x}}`

.. figure:: img/logistic_regression/sigmoid_function.png
  :align: center
  :scale: 100%


**Interpretation of Hypothesis Output**

* :math:`h_{\theta}(x):\ estimated\ probability\ that\ y=1\ on\ input\ x`

* Example:

  * :math:`If\ X = \begin{pmatrix} x_{0} \\ x_{1} \end{pmatrix} = \begin{pmatrix} 1 \\ tumor\ size \end{pmatrix}`

  * Let's assumed that :math:`h_{\theta}(x) = 0.7`

  * It tells us that 70 % chance to be classified to malignant tumor

* :math:`h_{\theta}(x) = P(y=1|x;\theta)`

* Probability that :math:`y=1`, given :math:`x`, parameterized by :math:`\theta`

* :math:`y` has two cases 0 or 1


**Check**

Suppose we want to predict, from data :math:`x` about a tumor, whether it is malignant (:math:`y=1`) or benign (:math:`y=0`). Our logistic regression classifier outputs, for a specific tumor, :math:`h_{\theta}(x)=P(y=1|x;θ)=0.7`, so we estimate that there is a 70% chance of this tumor being malignant. What should be our estimate for :math:`P(y=0|x;θ)`, the probability the tumor is benign?

\(O\) :math:`P(y=0|x;\theta) = 0.3`

\(X\) :math:`P(y=0|x;\theta) = 0.7`

\(X\) :math:`P(y=0|x;\theta) = 0.7^{2}`

\(X\) :math:`P(y=0|x;\theta) = 0.3 \times 0.7`


**Reading:Hypothesis representation**

We could approach the classification problem ignoring the fact that :math:`y` is discrete-valued, and use our old linear regression algorithm to try to predict :math:`y` given :math:`x`. However, it is easy to construct examples where this method performs very poorly. Intuitively, it also doesn’t make sense for :math:`h_\theta (x)` to take values larger than 1 or smaller than 0 when we know that :math:`y \in {0, 1}`. To fix this, let’s change the form for our hypotheses :math:`h_\theta (x)` to satisfy :math:`0 \leq h_\theta (x) \leq 1`. This is accomplished by plugging :math:`\theta^{T}x` into the Logistic Function.

Our new form uses the "Sigmoid Function," also called the "Logistic Function":

.. math::
  h_{\theta}(x) = g(\theta^{T}x),\ z = \theta^{T}x\\
  g(z) = \frac{1}{1 + e^{−z}}


The following image shows us what the sigmoid function looks like:

.. figure:: img/logistic_regression/sigmoid_function_for_reading.png
  :align: center
  :scale: 80%


The function :math:`g(z)`, shown here, maps any real number to the (0, 1) interval, making it useful for transforming an arbitrary-valued function into a function better suited for classification.

:math:`h_\theta(x)` will give us the probability that our output is 1. For example, :math:`h_\theta(x)=0.7` gives us a probability of 70% that our output is 1. Our probability that our prediction is 0 is just the complement of our probability that it is 1 (e.g. if probability that it is 1 is 70%, then the probability that it is 0 is 30%).

.. math::

  h_{\theta}(x) = P(y=1|x;θ) = 1 − P(y=0|x;θ) \\
  P(y=0|x;θ) + P(y=1|x;θ) = 1


=================
Decision Boundary
=================

In a statistical-classification problem with two classes, a decision boundary or decision surface is a hypersurface that partitions the underlying vector space into two sets, one for each class.

**Logistic regression**

.. math::
  h_{\theta}(x) = g(\theta^{T}x),\ z = \theta^{T}x\\
  g(z) = \frac{1}{1 + e^{−z}}


Suppose predict ":math:`y = 1`" if :math:`h_{\theta} \geq 0.5` and predict ":math:`y = 0`" if :math:`h_{\theta} < 0.5`


**Decision boundary**

.. figure:: img/logistic_regression/decision_boundary.png
  :align: center
  :scale: 50%


:math:`h_{\theta}(x) = g(\theta_0 + \theta_1 x_1 + \theta_2 x_2)`

Predict ":math:`y = 1`" if :math:`-3 + x_1 + x_2 \geq 0`


**Check**

Consider logistic regression with two features :math:`x_1` and :math:`x_2`. Suppose :math:`\theta_0 = 5,\ \theta_1 = -1,\ \theta_2 = 0`, so that :math:`h_\theta(x) = g(5 - x_1)`. Which of these shows the decision boundary of :math:`h_\theta(x)`?

+---------------------------------------------------------------------+---------------------------------------------------------------------+
| .. image:: img/logistic_regression/decision_boundary_check_01.png   | .. image:: img/logistic_regression/decision_boundary_check_02.png   |
+---------------------------------------------------------------------+---------------------------------------------------------------------+
| .. image:: img/logistic_regression/decision_boundary_check_03.png   | .. image:: img/logistic_regression/decision_boundary_check_04.png   |
+---------------------------------------------------------------------+---------------------------------------------------------------------+


**Non-linear decision boundaries**

:math:`h_{\theta}(x) = g(\theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_03 x_1^2 + \theta_4 x_2^2)`

Predict ":math:`y = 1 if -1 + x_1^2 + x_2^2 \geq 0`

.. figure:: img/logistic_regression/non-linear_decision_boundaries.png
  :align: center
  :scale: 50%

We can get more complex non-linear decision boundaries.

:math:`h_{\theta}(x) = g(\theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_03 x_1^2 + \theta_4 x_2^2 + \theta_5 x_1^3 + \theta_6 x_2^3 + ...)`


**Reading: Decision boudnary**

In order to get our discrete 0 or 1 classification, we can translate the output of the hypothesis function as follows:

.. math::

  h_{\theta}(x) \geq 0.5 → y = 1 \\
  h_{\theta}(x) < 0.5 → y = 0


The way our logistic function g behaves is that when its input is greater than or equal to zero, its output is greater than or equal to 0.5:

.. math::

  g(z) \geq 0.5 \\
  when z \geq 0


Remember.

.. math::

  z=0,\ e^0 = 1\ ⇒\ g(z) = 1/2 \\
  z → ∞,\ e^−∞ → 0\ ⇒\ g(z) = 1 \\
  z → −∞,\ e^∞ → ∞\ ⇒\ g(z) = 0


So if our input to g is :math:`\theta^T X`, then that means:

.. math::

  h_{θ}(x) = g(θ^T x) \geq 0.5 \\
  when θ^T x \geq 0


From these statements we can now say:

.. math::

  θ^T x \geq 0\ ⇒\ y = 1 \\
  θ^T x < 0\ ⇒\ y = 0


The **decision boundary** is the line that separates the area where y = 0 and where y = 1. It is created by our hypothesis function.

**Example:**

.. math::

  θ = \begin{bmatrix}
        5 \\[0.3em]
        −1 \\[0.3em]
        0
      \end{bmatrix} \\
  y = 1\ if\ 5 + (−1) x_1 + 0x_2 \geq 0 \\
  5 − x+1 \geq 0 \\
  −x_1 \geq −5 \\
  x_1 \leq 5


In this case, our decision boundary is a straight vertical line placed on the graph where :math:`x_1 = 5`, and everything to the left of that denotes :math:`y = 1`, while everything to the right denotes :math:`y = 0`.

Again, the input to the sigmoid function g(z) (e.g. :math:`\theta^T X`) doesn't need to be linear, and could be a function that describes a circle (e.g. :math:`z = \theta_0 + \theta_1 x_1^2 +\theta_2 x_2^2`) or any shape to fit our data.


=============
Cost Function
=============

Training set:

:math:`{(x^{(1)},\ y^{(1)}),\ (x^{(2)},\ y^{(2)}),\ ...,\ (x^{(m)},\ y^{(m)})}`

m examples:

:math:`x \in \begin{bmatrix} x_9 \\[0.3em] x_1 \\[0.3em] ... \\[0.3em] x_n \end{bmatrix},\ x_0 = 1,\ y \in {0, 1}`

:math:`h_{\theta} (x) = \frac{1}{1} + e^{-\theta^T x}`

Parameters :math:`\theta` are chosen by a cost function.

**Linear regression**

:math:`J(\theta) = \frac{1}{m} \sum_{i=1}^{m} \frac{1}{2} (h_\theta (x^{(i)}) - y^{(i)})^2`

:math:`Cost(h_\theta (x^{(i)}),\ y) = \frac{1}{2} (h_\theta (x^{(i)}) - y^{(i)})^2`

In logistic regression :math:`h_{\theta} (x^{(i)}) = \frac{1}{1 + e^{-\theta^T x}}` and the cost function is non-convex. So, above cost function is not working well in logistic regression because it is hard to find global optimum.

.. figure:: img/logistic_regression/non-convex_and_convex_graph_for_cost_function.png
  :align: center
  :scale: 50%


**Logistic regression**

.. math::

  Cost(h_\theta (x^{(i)}),\ y) = 
    \begin{cases}
      -\log (h_\theta (x)) & if\ y = 1 \\
      -\log (1 - h_\theta (x)) & if\ y = 0 
    \end{cases}
  

.. figure:: img/logistic_regression/logistic_regression_cost_function.png
  :align: center
  :scale: 50%


:math:`Cost = 0\ if\ y = 1, h_\theta (x) = 1`

But as :math:`h_\theta (x) \rightarrow 0,\ Cost \rightarrow \infty`

Captures intuition that if :math:`h_\theta (x) = 0`, (predict :math:`P(y = 1|x;\theta) = 0)`, but :math:`y = 1`, we'll penalize learning algorithm by a very large cost.


**Check**

In logistic regression, the cost function for our hypothesis outputting (predicting) h_\theta(x)h θ​	 (x) on a training example that has label y∈{0,1} is:

:math:`cost(h_{\theta}(x),y) = −\log h_{\theta}(x) − log(1−h_{\theta}(x))\ if\ y = 1\ if\ y = 0`

Which of the following are true? Check all that apply.


\(O\) If :math:`h_\theta(x) = y`, then :math:`\text{cost}(h_\theta(x),y) = 0` (for :math:`y=0` and :math:`y=1`).

\(O\) If :math:`y=0`, then :math:`\text{cost}(h_\theta(x),y)\rightarrow\infty` as :math:`h_\theta(x)\rightarrow 1`.

\(X\) If :math:`y=0`, then :math:`\text{cost}(h_\theta(x),y)\rightarrow\infty` as :math:`h_\theta(x)\rightarrow 0`.

\(O\) Regardless of whether :math:`y=0` or :math:`y=1`, if :math:`h_\theta(x)=0.5`, then :math:`\text{cost}(h_\theta(x),y) > 0`.


**Reading**

We cannot use the same cost function that we use for linear regression because the Logistic Function will cause the output to be wavy, causing many local optima. In other words, it will not be a convex function.

Instead, our cost function for logistic regression looks like:

.. math::

  J(\theta) = \frac{1}{m} \sum_{i=1}^{m} \frac{1}{2} (h_\theta (x^{(i)}) - y^{(i)})^2 \\
  Cost(h_\theta (x^{(i)}),\ y) = -\log (h_\theta (x)),\ if\ y = 0 \\
  Cost(h_\theta (x^{(i)}),\ y) = -\log (1 - h_\theta (x)),\ if\ y = 0


When y = 1, we get the following plot for :math:`J(\theta)` vs :math:`h_\theta (x)`:

.. figure:: img/logistic_regression/logistic_regression_cost_function_for_reading_01.png
  :align: center
  :scale: 80%


Similarly, when y = 0, we get the following plot for :math:`J(\theta)` vs :math:`h_\theta (x)`:

.. figure:: img/logistic_regression/logistic_regression_cost_function_for_reading_02.png
  :align: center
  :scale: 80%

.. math::
  
  Cost(h_\theta (x),y) = 0\ if\ h_\theta (x) = y \\
  Cost(h_\theta (x),y) \rightarrow \infty \ if\ y = 0\ and\ h_\theta (x) \rightarrow 1 \\
  Cost(h_\theta (x),y) \rightarrow \infty \ if\ y = 1\ and\ h_\theta (x) \rightarrow 0


If our correct answer 'y' is 0, then the cost function will be 0 if our hypothesis function also outputs 0. If our hypothesis approaches 1, then the cost function will approach infinity.

If our correct answer 'y' is 1, then the cost function will be 0 if our hypothesis function outputs 1. If our hypothesis approaches 0, then the cost function will approach infinity.

Note that writing the cost function in this way guarantees that J(θ) is convex for logistic regression.


==============================================
Simplified cost function and gradient descent
==============================================

**Simplified cost function**

We can compress our cost function's two conditional cases into one case:

:math:`Cost(h_\theta (x),\ y) = −y \log (h_\theta (x)) − (1 − y) \log (1 − h_\theta (x))`

Notice that when y is equal to 1, then the second term :math:`(1 - y) \ \log (1 - h_\theta (x))(1 − y) \log (1 − h_\theta (x))` will be zero and will not affect the result. If :math:`y` is equal to 0, then the first term :math:`-y \log(h_\theta (x)) − y \log(h_\theta (x))` will be zero and will not affect the result.

We can fully write out our entire cost function as follows:

:math:`J(\theta) = - \frac{1}{m} \displaystyle \sum_{i=1}^m [y^{(i)}\log (h_\theta (x^{(i)})) + (1 - y^{(i)}) \log (1 - h_\theta(x^{(i)}))]`

A vectorized implementation is:

:math:`h = g(X_\theta)`

:math:`J(\theta) = \frac{1}{m} (−y^T \log (h) − (1 − y)^T \log (1 − h))`


**Gradient descent**

Remember that the general form of gradient descent is:

:math:`Repeat\ \{ \\ \ \ \ \ \theta_j := \theta_j − \alpha \frac{\sigma}{\sigma \theta_j} J(\theta) \\ \}`

We can work out the derivative part using calculus to get:

:math:`Repeat\ \{ \\ \ \ \ \ \theta_j := \theta_j − \frac{\alpha}{m} \sum{i=1}^{m} (h_\theta (x^{(i)}) − y^{(i)}) x_j^(i) \\ \}`

Notice that this algorithm is identical to the one we used in linear regression. We still have to simultaneously update all values in theta.

A vectorized implementation is:

:math:`\theta := \theta - \frac{\alpha}{m} X^{T} (g(X \theta ) - \vec{y})`


=========================
Advanced optimization
=========================

"Conjugate gradient", "BFGS", and "L-BFGS" are more sophisticated, faster ways to optimize :math:`\theta` that can be used instead of gradient descent. We suggest that you should not write these more sophisticated algorithms yourself (unless you are an expert in numerical computing) but use the libraries instead, as they're already tested and highly optimized. Octave provides them.

We first need to provide a function that evaluates the following two functions for a given input value θ:

:math:`J(\theta),\ \ \frac{\sigma}{\sigma \theta_j} J(\theta)`


We can write a single function that returns both of these:

.. code-block:: octave

  function [jVal, gradient] = costFunction(theta)
    jVal = [...code to compute J(theta)...];
    gradient = [...code to compute derivative of J(theta)...];
  end


Then we can use octave's "fminunc()" optimization algorithm along with the "optimset()" function that creates an object containing the options we want to send to "fminunc()".

.. code-block:: octave

  options = optimset('GradObj', 'on', 'MaxIter', 100);
  initialTheta = zeros(2,1);
  [optTheta, functionVal, exitFlag] = fminunc(@costFunction, initialTheta, options);


We give to the function "fminunc()" our cost function, our initial vector of theta values, and the "options" object that we created beforehand.


======================================
Multiclass classification: one-vs-all
======================================

Now we will approach the classification of data when we have more than two categories. Instead of :math:`y = {0,1}` we will expand our definition so that :math:`y = {0,1...n}`.

Since :math:`y = {0,1...n}`, we divide our problem into :math:`n+1` (+1 because the index starts at 0) binary classification problems; in each one, we predict the probability that ':math:`y`' is a member of one of our classes.

.. math::

  y \in {0,1...n} \\
  h_\theta^{(0)} \theta(x) = P(y = 0|x;\theta) \\
  h_\theta^{(1)}(x) = P(y = 1|x;\theta) \\
  ⋯ \\
  h_\theta^{(n)}(x) = P(y = n|x;\theta) \\
  prediction = \max_{i}(h_\theta^{(i)}(x))


We are basically choosing one class and then lumping all the others into a single second class. We do this repeatedly, applying binary logistic regression to each case, and then use the hypothesis that returned the highest value as our prediction.

The following image shows how one could classify 3 classes:


**To summarize:**

Train a logistic regression classifier :math:`h_\theta (x)` for each class￼ to predict the probability that :math:`y = i` ￼.

To make a prediction on a new :math:`x`, pick the class ￼that maximizes :math:`h_\theta (x)`.


===========
Reference
===========

* https://www.coursera.org/learn/machine-learning
* https://en.wikipedia.org/wiki/Decision_boundary