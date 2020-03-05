========
Android
========

Anko 라이브러리 사용 준비
======================

Gradle Scripts > bundle.gradle (Project: XXX) 파일에서 buildscript 항목에 Anko 라이브러리 버전을 아래와 같이 추가한다.

.. code-block:: kotlin

    ext.anko_version = '0.10.5'

그리고 나서 Gradle Scripts > bundle.gradle (Module: app) 파일에서 dependencies 항목에 Anko 라이브러리를 아래와 같이 추가한다.

.. code-block:: kotlin

    dependencies {
        implementation "org.jetbrains.anko:anko-commons:$anko_version"
    }

위 작업을 완료한 후 에디터 창 상단에 'Sync Now' 링크를 클릭하여 싱크하면 된다.


이전 화면으로 돌아가는 업 네비게이션
==============================

AndroidManifest.xml 파일에서 parentActivityName 속성을 추가하면 된다.

.. code-block:: kotlin

    <activity
        android:name=".CurrentActivity"
        android:parentActivityName=".PrevActivity">


벡터 드로어블 하위 호환 설정
========================

Gradle Scripts > build.gradle (Module: app) 파일에서 벡터 이미지가 잘 표시되도록 아래와 같은 설정을 한다.

.. code-block:: kotlin

    defaultConfig {
        vectorDrawbles.useSupportLibrary = true
    }


액티비티 생명 주기
===============

액티비티 생명 주기는 다음과 같고, 자세한 내용은 `Android developers <https://developer.android.com/guide/components/activities/activity-lifecycle.html>`_ 에서 확인할 수 있다.

.. figure:: img/android/activity_lifecycle.png
    :align: center
    :scale: 100%


안드로이드 4대 컴포넌트
====================

* 액티비티: 화면 구성
* 콘텐츠 프로바이더: 데이터베이스, 파일, 네트워크의 데이터를 다른 앱에 공유
* 브로드캐스트 리시버: 앱이나 기기가 발송하는 방송 수신
* 서비스: 화면이 없고 백그라운드 작업 시 용이


프로그래먼트 생명 주기
==================

프로그래먼트 생명 주기는 다음과 같고, 자세한 내용은 `Android developers <https://developer.android.com/guide/components/fragments>`_ 에서 확인할 수 있다.

.. figure:: img/android/fragment_lifecycle.png
    :align: center
    :scale: 100%


서비스의 생명 주기
===============

서비스의 생명 주기는 다음과 같고, 자세한 내용은 `Android developers <https://developer.android.com/guide/components/services>`_ 에서 확인할 수 있다.

.. figure:: img/android/service_lifecycle.png
    :align: center
    :scale: 100%


뷰 제한
=======

* 앱 위젯에 배치하는 뷰

    * FrameLayout
    * LinearLayout
    * RelativeLayout
    * GridLayout

* 레이아웃에 배치하는 뷰

    * AnalogClock
    * Button
    * Chronometer
    * ImageButton
    * ImageView
    * ProgressBar
    * TextView
    * ViewFlipper
    * ListView
    * GridView
    * StackView
    * AdapterViewFlipper


체인 모드
========

체인 모드의 종류는 다음과 같고, 자세한 내용은 `Android developers <https://developer.android.com/reference/android/support/constraint/ConstraintLayout>`_ 에서 확인할 수 있다.

.. figure:: img/android/chains-styles.png
    :align: center
    :scale: 40%




Reference
==========

* 오준석의 안드로이드 생존코딩 코틀린 편
* `Android developers <https://developer.android.com/>`_
