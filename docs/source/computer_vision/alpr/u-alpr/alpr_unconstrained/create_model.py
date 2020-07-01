"""
    create_model
    =============

    WPOD-Net 모델을 생성하는 부분이다.
"""

def res_block(x,sz,filter_sz=3,in_conv_size=1):
    """작성 예정

    Args:

    Returns:

    Raises:
    """
    xi  = x
    for i in range(in_conv_size):
        xi  = Conv2D(sz, filter_sz, activation='linear', padding='same')(xi)
        xi  = BatchNormalization()(xi)
        xi 	= Activation('relu')(xi)
    xi  = Conv2D(sz, filter_sz, activation='linear', padding='same')(xi)
    xi  = BatchNormalization()(xi)
    xi 	= Add()([xi,x])
    xi 	= Activation('relu')(xi)
    return xi

def conv_batch(_input,fsz,csz,activation='relu',padding='same',strides=(1,1)):
    """작성 예정

    Args:

    Returns:

    Raises:
    """
    output = Conv2D(fsz, csz, activation='linear', padding=padding, strides=strides)(_input)
    output = BatchNormalization()(output)
    output = Activation(activation)(output)
    return output

def public_fn_with_googley_docstring(name, state=None):
    """This function does something.

    Args:
       name (str):  The name to use.

    Kwargs:
       state (bool): Current state to be in.

    Returns:
       int.  The return code::

          0 -- Success!
          1 -- No good.
          2 -- Try again.

    Raises:
       AttributeError, KeyError

    A really great idea.  A way you might use me is

    >>> print public_fn_with_googley_docstring(name='foo', state=None)
    0

    BTW, this always returns 0.  **NEVER** use with :class:`MyPublicClass`.

    """
    return 0
