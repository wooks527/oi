Language modeling
==================

=======================
N-gram language models
=======================

In wikipedia, a statistical language model is a probability distribution over sequences of words. Given such a sequence, say of length m, it assigns a probability :math:`\displaystyle P(w_{1},\ldots ,w_{m})` to the whole sequence. The language model provides context to distinguish between words and phrases that sound similar. For example, in American English, the phrases "recognize speech" and "wreck a nice beach" sound similar, but mean different things.

한마디로 단어로 구성된 문장들의 확률분포를 통계적 언어모델이라고 할 수 있다.

For understanding a statistical language model, let's talk about the probability of the next word.


Probability of the next word
*****************************

**Toy corpus:**

* This is the house that Jack built.
* This is the malt
* That lay in the house that Jack built.
* This is the rat,
* That ate the malt
* That lay in the house that Jack built.
* This is the cat,
* That killed the rat,
* That ate the malt
* That lay in the house that Jack built.


**Example:**

* :math:`p(house|this\ is\ the) =\ ?`


N-gram
********

In the fields of computational linguistics and probability, an n-gram is a contiguous sequence of n items from a given sample of text or speech. Below image depicts 4-gram and bi-gram, and describe two next word probabilities.

한마디로 n개의 단어 묶음을 N-gram으로 이해하면 된다.

.. figure:: img/lm/n-gram.png
  :align: center
  :scale: 60%


Probability of the whole sequence
**********************************

Then, what is the probability of the whole sequence?

**Example:**

* :math:`p(this\ is\ the\ house) =\ ?`


**Predict probability of a sequence of words:**

Below ideas are to calculate the probability of a sequence.

:math:`w = (w_1 w_2 w_3 ... w_k)`

* Chain rule:

  * :math:`p(w) = p(w_1)p(w_2 | w_1) ... p(w_k | w_1 ... w_{k-1})`

* Markov assumption:

  * :math:`p(w_i | w_1 ... w_{i-1}) = p(w_i | w_{i-n+1} ... w_{i-1})`

한마디로 문장에 구성된 첫 단어부터 다음 단어가 나타날 학률을 모두 곱하여 한 문장의 확률을 계산한다.


Bigram language model
**********************

if :math:`n = 2`, this model is a bigram language model.

.. rst-class:: centered

  :math:`p(w) = p(w_1)p(w_2 | w_1) ... p(w_k | w_{k-1})`


**Toy corpus:**

* This is the malt
* That lay in the hous that Jack built

The probability of "this is the house" is:

.. rst-class:: centered

  :math:`\begin{split} p(this\ is\ the\ house) &= p(this) p(is|this) p(the|is) p(house|the) \\ &= \frac{1}{12} \cdot 1 \cdot 1 \cdot \frac{1}{2} \end{split}`


**Additional changes:**

In the sentence, "this" is at the first position, so it is better to change :math:`p(w)` to :math:`p(w_1 | start)`

.. rst-class:: centered
  
  :math:`p(w) = p(w_1 | start)p(w_2 | w_1) ... p(w_k | w_{k-1})`

  :math:`\begin{split} p(this\ is\ the\ house) &= p(this) p(is|this) p(the|is) p(house|the) \\ &= \frac{1}{2} \cdot 1 \cdot 1 \cdot \frac{1}{2} \end{split}`


If the sentence has the last word, then we just add the last probability.

.. rst-class:: centered
  
  :math:`p(w) = p(w_1)p(w_2 | w_1) ... p(w_k | w_{k-1}) p(end | w_k)`


Also, it's normalized separately for each sequence length!

.. rst-class:: centered

  :math:`p(this) + p(that) = 1.0`

  :math:`p(this\ this) + p(this\ is) + \cdots + p(built\ built) = 1.0`


Let's check the model
**********************

.. rst-class:: centered

  :math:`p(cat\ dog\ cat) = p(cat | \_) p(dog | cat) p(cat | dog) p(\_ | cat)`


.. figure:: img/lm/bi_gram_model_checking.png
  :align: center
  :scale: 70%


Bigram language model
**********************

**Define the model:**

.. rst-class:: centered

  :math:`p(w) = \prod_{i=1}^{k+1} p(w_i | w_{i-1})`
  

**Estimate the probabilities:**

.. rst-class:: centered

  :math:`p(w_i | w_{i-1}) = \frac{c(w_{i-1} w_i)}{\sum_{w_i} c(w_{i-1} w_i)} = \frac{c(w_{i-1} w_i)}{c(w_{i-1})}`


It's all about counting!!


Where do we need LM?
***********************

* Suggestions in messengers
* Spelling correction
* Machine translation
* Speech recognition
* Handwriting recognition
* ...


===========
Perplexity
===========


===========
Smoothing
===========



===========
References
===========

* https://www.coursera.org/learn/language-processing
* https://en.wikipedia.org/wiki/Language_model