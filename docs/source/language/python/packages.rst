========
Packages
========

Built-in
=========

eval
*****

Convert string to code:

.. code-block:: python

  >>> eval('2+2')
  4


random
======

random
*******

.. code-block:: python

  >>> import random
  >>> random.random()
  0.42716323261498423

randrange
**********

Return a random integer N such that a <= N <= b-1

.. code-block:: python

  >>> random.randrange(1, 10)
  5

randomint
*********

Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1)

.. code-block:: python

  >>> random.randint(1, 10)
  5

choice
*******

.. code-block:: python

  >>> allowed_operators = ['+', '-']
  >>> operator = random.choice(allower_operators)
  '+'


Reference
==========

* https://wikidocs.net/79
