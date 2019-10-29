===========
자바 시작하기
===========

자바의 탄생
=========

* 1995년에 썬 마이크로시스템즈에서 발표한 객체지향 언어
* 현재 썬 마이크로시스템즈는 오라클에 인수가 된 상태


자바의 장단점
===========

장점
****

* 쉬운 언어이다.

    * C와 C++언어의 문법을 기본으로 차용하여 개발된 언어
    * C와 C++ 이 가진 어려운 문법인 포인터와 다중 상속 제거
    * C와 C++에 비해 쉬운 언어이다.

* 플랫폼에 독립적이다.

    * 자바는 JVM만 있으면 윈도우, 리눅스, 맥등 어떤 플랫폼에서도 실행이 가능

* 객체지향 언어이다.

* Garbage collector로 메모리 관리를 자동으로 해준다.

단점
****

* 속도가 느림

    * 자바는 하드웨어에 맞게 완전히 컴파일된 상태가 아니고, 실행시에 해석되기 떄문에 속도가 느림
    * 하지만 바이트코드를 하드웨어의 기계어로 변환해주는 JIT컴파일러와 Hotspot과 같은 기술 적용으로 JVM 기능이 향상되어 속도문제가 상당히 개선됨


파일 다운로드 및 설치
=================

* JDK 다운로드 및 설치
    
    * Ubuntu

        * 아래 명령어로 jre, jdk 설치
        
            * sudo apt install default-jre
            * sudo apt install default-jdk

    * Windows
    
        * Oracle 사이트에서 운영체제에 적절한 JDK 다운로드 후 설치
        * 환경변수 설정 (JAVA_HOME, Path, CLASSPATH)

    * OS X는 Java가 기본적으로 설치되어 있음

* 이클립스 다운로드 및 설치 (http://www.eclipse.org)


자바 개발순서
===========

1. 소스 작성
2. 작성한 소스 컴파일
3. 컴파일한 소스를 JVM을 이용하여 실행

간단한 예제
***********

* 소스 작성

    * HelloWorld.java 파일을 원하는 디렉토리에서 작성
    * 자바는 파일 이름 중요! 대소문자를 구별하니 잘 입력해 주어야 합니다.

    .. code-block:: java

        public class HelloWorld{
            public static void main(String args[]){
                System.out.println("Hello World");
            }
        }

* 컴파일

    * 터미널 실행
    * HellowWorld.java를 저장한 폴더로 이동
    * javac HelloWorld.java 로 컴파일 합니다.

* 실행

    * java HelloWorld 로 실행
    * 화면에 HelloWorld가 출력되는 것을 확인


이클립스로 동일한 작업 진행
**********************

* eclipse.exe를 실행

* 사용자 홈디렉토리 아래에 workspace 폴더를 지정

* first 프로젝트 생성

* 소스 작성

    * src폴더에서 HelloWorld.java파일 생성
    * 앞에서 만들었던 파일과 똑같은 파일을 HelloWorld.java파일로 작성
    * 워크스페이스 경로를 파일탐색기로 열어보면 src폴더에 HelloWorld.java파일 확인 가능

* 컴파일

    * bin폴더를 열어보면 HelloWorld.class파일 생성되어있음 (이클립스는 소스파일에 문제가 없다면 자동으로 컴파일하여 bin폴더에 클래스를 만들게 됩니다.)

* 실행

    * 클래스를 선택한 후 우측버튼을 클릭하고 자바 어플리케이션을 실행하는 메뉴를 선택


주석문
=====

주석이란, 프로그램의 코드와 실행에는 영향을 주지 않는 문장이다.


주석의 종류
**********

* 구현 주석

    * 행단위 주석 (// 를 해주면, 해당 행이 주석 처리됨 )

    * 블럭단위 주석 (/* 주석으로 사용할 내용 */ )

* 문서화 주석

    * /** 문서에 포함할 내용을 작성함 */

    * 문서화 주석은 클래스, 인터페이스 그리고 멤버 당 하나씩 가질 수 있고, 선언 바로 전에 작성

    .. code-block:: java

        import java.io.*;

        /**
        * <h1>Add Two Numbers!</h1>
        * The AddNum program implements an application that
        * simply adds two given integer numbers and Prints
        * the output on the screen.
        * <p>
        * <b>Note:</b> Giving proper comments in your program makes it more
        * user friendly and it is assumed as a high quality code.
        *
        * @author  Zara Ali
        * @version 1.0
        * @since   2014-03-31
        */
        public class AddNum {
            /**
            * This method is used to add two integers. This is
            * a the simplest form of a class method, just to
            * show the usage of various javadoc Tags.
            * @param numA This is the first paramter to addNum method
            * @param numB  This is the second parameter to addNum method
            * @return int This returns sum of numA and numB.
            */
            public int addNum(int numA, int numB) {
                return numA + numB;
            }

            /**
            * This is the main method which makes use of addNum method.
            * @param args Unused.
            * @return Nothing.
            * @exception IOException On input error.
            * @see IOException
            */
            public static void main(String args[]) throws IOException
            {

                AddNum obj = new AddNum();
                int sum = obj.addNum(10, 20);

                System.out.println("Sum of 10 and 20 is :" + sum);
            }
        }


참조
====

* `프로그래머스 > 자바 입문 <https://programmers.co.kr/learn/courses/5>`_
* `It's Foss <https://itsfoss.com/install-java-ubuntu/>`_
* `huhghiza <https://huhghiza.tistory.com/7>`_
