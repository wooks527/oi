Adam
=====

Adam method는 Adagrad + RMSProp의 장점을 섞어 놓은 방법이다.
Adam method의 의 주요 장점은 Step size가 Gradient의 Rescaling에 영향 받지 않는다는 것이다.
Gradient가 커져도 Step size는 Bound되어 있어서 어떠한 Objective function을 사용한다 하더라도 안정적으로 최적화를 위한 하강이 가능하다.
게다가 Step size를 과거의 Gradient 크기를 참고하여 Adapted 시킬 수 있다.


============
Pseudo-code
============

.. figure:: img/adam_pseudo_code.png
    :scale: 50%


**Reference**
    * http://dalpo0814.tistory.com/29