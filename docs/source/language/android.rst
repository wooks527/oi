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


Reference
==========

* 
