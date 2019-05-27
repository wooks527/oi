Batch normalization
====================

===========
Definition
===========

Gradient vanishing and exploding 문제를 해결하기 위한 방법으로, Training 하는 과정 전체를 안정화하여 학습 속도를 가속화 시키는 방법이다.
위와 같은 불안정화가 발생하는 이유는 Internal covariance shift 때문인데, 이는 Network의 각 층이나 Activation 마다 Input의 Distribution이 달라지는 현상이다.
이를 해결하기 위해 각층의 Input distribution을 평균 0, 표준편차 1인 Input으로 Normalization 하거나 Whitening이라는 방법으로 해결할 수 있다.
Whitening은 기본적으로 들어오는 input의 feature들을 uncorrelated 하게 만들어주고, 각각의 variance를 1로 만들어주는 작업이다.

하지만 Whitening은 계산량이 많고 일부 Parameter들의 영향을 무시하기 때문에 이를 보완하고 Internal covariance shift를 줄이기 위해 아래와 같은 3가지 접근을 했다.

    * 각각의 feature들이 이미 uncorrelated 되어있다고 가정하고, feature 각각에 대해서만 scalar 형태로 mean과 variance를 구하고 각각 normalize 한다.
    * 단순히 mean과 variance를 0, 1로 고정시키는 것은 오히려 Activation function의 nonlinearity를 없앨 수 있다. 예를 들어 sigmoid activation의 입력이 평균 0, 분산 1이라면 출력 부분은 곡선보다는 직선 형태에 가까울 것이다. 또한, feature가 uncorrelated 되어있다는 가정에 의해 네트워크가 표현할 수 있는 것이 제한될 수 있다. 이 점들을 보완하기 위해, normalize된 값들에 scale factor (gamma)와 shift factor (beta)를 더해주고 이 변수들을 back-prop 과정에서 같이 train 시켜준다.
    * Training data 전체에 대해 mean과 variance를 구하는 것이 아니라, mini-batch 단위로 접근하여 계산한다. 현재 택한 mini-batch 안에서만 mean과 variance를 구해서, 이 값을 이용해서 normalize 한다.


**Reference**
    * https://shuuki4.wordpress.com/2016/01/13/batch-normalization-%EC%84%A4%EB%AA%85-%EB%B0%8F-%EA%B5%AC%ED%98%84/