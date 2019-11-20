======================================
Summarization and simplification tasks
======================================


Quiz: Summarization and simplification tasks
============================================

.. toggle-header::
  :header: **Quiz list**

  |
  **Question 1**

    Which type of information is not used for evaluation in machine translation (e.g. in BLEU score), but is used for evaluation in simplification task (e.g. in SARI score)?

    \(　\) System input

    \(　\) Human reference

    \(　\) System output


  **Question 2**
    
    Let us consider a simplification task and denote an input by II, a reference by RR, and a system output by :math:`O`. We have discussed several types of operations for simplification. How would you compute a precision score for the copying operation? (It described in Optimizing Statistical Machine Translation for Text Simplification, 2016)

    \(　\) |O∩I∩R||I∩R|

    \(　\) |O∩ I¯∩R||O∩I¯|

    \(　\) |O∩I∩R||O∩I|


  **Question 3**
  
    In the summarization video we talked about attention distribution and denoted its elements as :math:`p_{i}^j`. How are they normalized?

    \(　\) They sum to 1 over all positions of an input sentence: :math:`\sum_{i} p_i^j = 1` .

    \(　\) They sum to 1 over all positions of an output sentence: :math:`\sum_{j} p_i^j = 1` .

    \(　\) They are logits, we need to apply softmax to get the normalization constraint.


  **Question 4**

    Imagine you have trained an encoder-decoder-attention model to generate a text summary. Let's say you have a vocabulary [big, black, bug, bear] and the vocabulary distribution at some decoding moment is [0.3, 0.4, 0.1, 0.2].

    Now, let us consider how it changes if we add the pointer part from the paper "Get to the point! Summarization with pointer-generator network" to be able to copy some input words.

    Consider an input sentence: "a big black bug bit a big black bear". And the attention distribution [0.1, 0.1, 0.1, 0.1, 0.2, 0.1, 0.1, 0.1, 0.1].

    How will the final distribution look like, if the pointer network (copy distribution) is weighted equally with the generator network (vocabulary distribution)?

    Enter the probability for "black".

    Answer:


  **Question 5**
  
    Check the correct statements about the summarization models discussed in the video.

    \(　\) The copy mechanism encourages the model to generate new fragments that did not occur in the input.

    \(　\) The coverage trick helps to avoid repetitions of the input fragments.

    \(　\) The pointer-generator network performs extractive summarization.

    \(　\) The pointer-generator network with coverage trick outperforms all other baselines.

    \(　\) The pointer-generator network performs abstractive summarization.

|
  
References
===========

* https://www.coursera.org/learn/language-processing