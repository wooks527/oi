Recommender systems
====================

Example: Predicting movie ratings
**********************************

User rates movies using one to five stars.

====================  =========  =======  =========  ========
Movie                 Alice (1)  Bob (2)  Carol (3)  Dave (4)
====================  =========  =======  =========  ========
Love at last          5          5        0          0
Romance forever       5          ?        ?          0
Cute puppies of love  ?          4        0          ?
Nonstop car chases    0          0        5          4
Swords vs. karate     0          0        5          ?
====================  =========  =======  =========  ========

* :math:`n_u = \text{no. users} = 4`
* :math:`n_m = \text{no. movies} = 5`
* :math:`r(i,j) = 1 \text{ if user } j \text{has rated movie } i \text{ (e.g. } r(2, 1) = 1)`
* :math:`y^{(i,j)} = \text{rating given by user } j \text{ to movie } i \text{ (defined only if } r(i,j) = 1 \text{, e.g. } y^{(2, 1)} = 5)`

The goal of recommender systems is to predict missing values like question marks through given data.

In this example, if Alice and Bob both like the romantic movies maybe we think that Alice would have given this a five. Maybe we think Bob would have given this a 4.5 or some high value, as we think maybe Carol and Dave were doing these very low ratings. And Dave, well, if Dave really likes action movies, maybe he would have given Swords and Karate a 4 rating or maybe a 5 rating.

A recommender system is to come up with a learning algorithm that can automatically go fill in these missing values so that we can look at the movies that the user has not yet watched, and recommend new movies to that user to watch.


==============================
Content based recommendations
==============================

====================  =========  =======  =========  ========  =====================  ====================
Movie                 Alice (1)  Bob (2)  Carol (3)  Dave (4)  :math:`x_1` (romance)  :math:`x_2` (action)
====================  =========  =======  =========  ========  =====================  ====================
Love at last          5          5        0          0         0.9                    0
Romance forever       5          ?        ?          0         1.0                    0.01
Cute puppies of love  ?          4        0          ?         0.99                   0
Nonstop car chases    0          0        5          4         0.1                    1.0
Swords vs. karate     0          0        5          ?         0                      0.9
====================  =========  =======  =========  ========  =====================  ====================

For each user :math:`j,` learn a parameter :math:`\theta^{(j)} \in \mathbb{R}^3.` Predict user :math:`j` as rating movie :math:`i` with :math:`(\theta^{(j)})^T x^{(i)}` stars.

Example:

* Find the missing value:

  * Given: :math:`x^{(3)} = \begin{bmatrix} 1 \\[0.3em] 0.99 \\[0.3em] 0 \end{bmatrix} \leftrightarrow \theta^{(1)} = \begin{bmatrix} 0 \\[0.3em] 5 \\[0.3em] 0 \end{bmatrix}`
  * :math:`(\theta^{(1)})^T x^{(3)} = 5 * 0.99 = 4.95`

* Find the resonable :math:`\theta^{(3)}` :

  * :math:`(\theta^{(3)})^T x^{(5)} = \theta_1^{(3)} * 1 + \theta_2^{(3)} * 0 + \theta_3^{(3)} * 0.9 \approx 5`
  * Answer: :math:`\theta^{(3)} = \begin{bmatrix} 0 \\[0.3em] 0 \\[0.3em] 5 \end{bmatrix}`


Optimization algorithm
***********************

**To learn** :math:`\theta^{(j)}` **(parameter for user** :math:`j` **):**

.. rst-class:: centered

  :math:`\mathcal{L}(\theta^{(j)}) = \min_{\theta^{(j)}} \frac{1}{2m^{(j)}} \sum_{i:r(i,j) = 1} \Big( \big( \theta^{(j)} \big)^T x^{(i)} - y^{(i,j)} \Big)^2 + \frac{\lambda}{2m^{(j)}} \sum_{k=1}^{n} \big( \theta_k^{(j)} \big)^2`

* :math:`r(i,j)` = 1 if user :math:`j` has rated movie :math:`i` (0 otherwise)
* :math:`y^{(i,j)}` = rating by user :math:`j` on movie :math:`i` (if defined)
* :math:`\theta^{(j)}` = parameter vector for user :math:`j`
* :math:`x^{(i)}` = feature vector for movie :math:`i`
* :math:`(\theta^{(j)})^T (x^{(i)})` = predicted rating for user :math:`j,` movie :math:`i`
* :math:`m^{(j)}` = no. of movies rated by user :math:`j`

We can remove :math:`m^{(j)}` for simplifying the model because it is just a constant.

.. rst-class:: centered

  :math:`\mathcal{L}(\theta^{(j)}) = \min_{\theta^{(j)}} \frac{1}{2} \sum_{i:r(i,j) = 1} \Big( \big( \theta^{(j)} \big)^T x^{(i)} - y^{(i,j)} \Big)^2 + \frac{\lambda}{2} \sum_{k=1}^{n} \big( \theta_k^{(j)} \big)^2`

**To learn** :math:`\theta^{(1)}, \cdots , \theta^{(n_u)}:`

.. rst-class:: centered

  :math:`\mathcal{L}(\theta^{(1)}, \cdots , \theta^{(n_u)}) = \min_{\theta^{(1)}, \cdots , \theta^{(n_u)}} \frac{1}{2} \sum_{j=1}^{n_u} \sum_{i:r(i,j) = 1} \Big( \big( \theta^{(j)} \big)^T x^{(i)} - y^{(i,j)} \Big)^2 + \frac{\lambda}{2} \sum_{j=1}^{n_u} \sum_{k=1}^{n} \big( \theta_k^{(j)} \big)^2`

Gradient descent update:

.. rst-class:: centered

  :math:`\theta_k^{(j)} = \theta_k^{(j)} - \alpha \sum_{\substack{i:r(i,j)=1}} \Big( \big( \theta^{(j)} \big)^T x^{(i)} - y^{(i,j)} \Big) x_k^{(i)}\ (for\ k = 0)`

  :math:`\theta_k^{(j)} = \theta_k^{(j)} - \alpha \Bigg( \sum_{\substack{i:r(i,j)=1}} \Big( \big( \theta^{(j)} \big)^T x^{(i)} - y^{(i,j)} \Big) x_k^{(i)}\ + \lambda \theta_k^{(j)} \Bigg)(for\ k \neq 0)`


===========
Reference
===========

* https://www.coursera.org/learn/machine-learning