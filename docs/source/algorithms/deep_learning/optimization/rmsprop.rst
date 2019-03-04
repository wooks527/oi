RMSProp
========

AdaGrad의 문제점을 보안한 방법이다. AdaGrad는 Iteration이 계속될수록 G가 계속 증가해서 step size가 너무 작아질 수 있기 때문이다.
이러한 문제를 보완하기 위해서 RMSProp처럼 Exponential moving average를 사용하는 방법이 고안되었다.
Exponential moving average는 수식에서 알 수 있듯이 과거의 정보에 가중치를 작게 부여한다.
최근 값에 가장 민감하도록 최고 가중치를 부여하는 형태이다.


**Reference**
    * http://dalpo0814.tistory.com/29