LSTM
=====

Long Short Term Memory networks – usually just called “**LSTMs**” – are a special kind of RNN, capable of learning long-term dependencies. They were introduced by Hochreiter & Schmidhuber (1997), and were refined and popularized by many people in following work. They work tremendously well on a large variety of problems, and are now widely used.

LSTMs are explicitly designed to avoid the long-term dependency problem. Remembering information for long periods of time is practically their default behavior, not something they struggle to learn! This is known as a **vanishing gradient problem**.

All recurrent neural networks have the form of a chain of repeating modules of neural network. In standard RNNs, this repeating module will have a very simple structure, such as a single tanh layer.

.. figure:: img/lstm/simple_rnn.png
  :align: center
  :scale: 20%

  The repeating module in a standard RNN contains a single layer.


LSTMs also have this chain like structure, but the repeating module has a different structure. Instead of having a single neural network layer, there are four, interacting in a very special way.

.. figure:: img/lstm/lstm.png
  :align: center
  :scale: 20%


These are notations which are used in LSTM.

.. figure:: img/lstm/lstm_notations.png
  :align: center
  :scale: 50%


===========================
The core idea behind LSTMs
===========================

The **cell state** is kind of like a conveyor belt. It runs straight down the entire chain, with only some minor linear interactions. It’s very easy for information to just flow along it unchanged.

.. figure:: img/lstm/cell_state.png
  :align: center
  :scale: 40%


The LSTM does have the ability to remove or add information to the cell state, carefully regulated by structures called gates.

Gates are a way to optionally let information through. They are composed out of a sigmoid neural net layer and a pointwise multiplication operation.

.. figure:: img/lstm/sigmoid_layer.png
  :align: center
  :scale: 40%


The sigmoid layer outputs numbers between zero and one, describing how much of each component should be let through. A value of zero means “let nothing through,” while a value of one means “let everything through!”

An LSTM has three of these gates, to protect and control the cell state.


===============================
Step-by-Step LSTM Walk Through
===============================

**First step: forget gate**

The first step in our LSTM is to decide what information we’re going to throw away from the cell state. This decision is made by a sigmoid layer called the “**forget gate layer**”. It looks at :math:`h_{t−1}` and :math:`x_t`, and outputs a number between 0 and 1 for each number in the cell state :math:`C_{t−1}`. 1 represents “completely keep this” while a 0 represents “completely get rid of this.”

Let’s think about language model trying to predict the next word based on all the previous ones. In such a problem, the cell state might include the gender of the present subject, so that the correct pronouns can be used. When we see a new subject, we want to forget the gender of the old subject.

.. figure:: img/lstm/forget_gate.png
  :align: center
  :scale: 35%


**Second step: input gate**

The next step is to decide what new information we’re going to store in the cell state. This has two parts.

First, a sigmoid layer called the “**input gate layer**” decides which values we’ll update. Next, a tanh layer creates a vector of new candidate values, :math:`\tilde{C}_t`, that could be added to the state. In the next step, we’ll combine these two to create an update to the state.

In the example of our language model, we’d want to add the gender of the new subject to the cell state, to replace the old one we’re forgetting.

.. figure:: img/lstm/input_gate_01.png
  :align: center
  :scale: 35%


It’s now time to update the old cell state, :math:`C_{t−1}`, into the new cell state :math:`C_t`. The previous steps already decided what to do, we just need to actually do it.

We multiply the old state by :math:`f_t`, forgetting the things we decided to forget earlier. Then we add :math:`i_t ∗ \tilde{C}_t`. This is the new candidate values, scaled by how much we decided to update each state value.

In the case of the language model, this is where we’d actually drop the information about the old subject’s gender and add the new information, as we decided in the previous steps.

.. figure:: img/lstm/input_gate_02.png
  :align: center
  :scale: 35%


**Final step: output gate**

Finally, we need to decide what we’re going to output. This output will be based on our cell state, but will be a filtered version. First, we run a sigmoid layer which decides what parts of the cell state we’re going to output. Then, we put the cell state through tanh (to push the values to be between −1 and 1) and multiply it by the output of the sigmoid gate, so that we only output the parts we decided to.

For the language model example, since it just saw a subject, it might want to output information relevant to a verb, in case that’s what is coming next. For example, it might output whether the subject is singular or plural, so that we know what form a verb should be conjugated into if that’s what follows next.

.. figure:: img/lstm/output_gate.png
  :align: center
  :scale: 35%


**Variants on Long Short Term Memory**

추후 작성 예정


===========
Reference
===========

* https://ratsgo.github.io/natural%20language%20processing/2017/03/09/rnnlstm/
* http://colah.github.io/posts/2015-08-Understanding-LSTMs/