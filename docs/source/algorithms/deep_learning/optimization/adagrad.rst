AdaGrad
========

AdaGrad가 추구하는 것은 과거의 gradient 변화량을 참고하는 것이다. 이미 많이 변화한 변수들은 optimum에 거의 도달했다고 보고 stepsize를 작게하고 싶고, 여태까지 많이 변화하지 않은 변수들을 아직 가야할 길이 멀다고 보고 stepsize를 크게하고 싶은 것이다.


**Reference**
    * http://dalpo0814.tistory.com/29