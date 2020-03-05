=======
Ubuntu
=======

설치
====

부팅 디스크 만들기
******************

-------
Ubuntu
-------

우분투에서 부팅 USB는 아래 과정을 통해 간단하게 만들 수 있다.

* ISO 파일 다운로드 (`Link <https://ubuntu.com/download/desktop>`_)
* 프로그램 검색에서 "시동 디스크 만들기"를 실행
* 다운로드 받은 ISO 파일을 선택 ￫ 부팅 USB를 선택 ￫ 시동 디스크 만들기 클릭

:h4:`참조`

* `https://blankspace-dev.tistory.com/308 <https://blankspace-dev.tistory.com/308>`_

설치
*****

* `HiSEON, 우분투 18.04 설치 <https://hiseon.me/linux/ubuntu/install-ubuntu-18-04/>`_
* `서지스원 @IT. 블로그 매거진, 리눅스 스왑(SWAP) 파티션이란 무엇? 어떤 일을 하나요? <https://sergeswin.com/1034>`_

한글 키보드 설정
****************

::

    // 오른쪽 Alt키의 기본 키 맵핑을 제거하고 'Hangul'키로 맵핑
    xmodmap -e 'remove mod1 = Alt_R'
    xmodmap -e 'keycode 108 = Hangul'

    // 오른쪽 Ctrl키의 기본 키 맵핑을 제거하고 'Hangul_Hanja'키로 맵핑
    xmodmap -e 'remove control = Control_R'
    xmodmap -e 'keycode 105 = Hangul_Hanja'

    // 키 맵핑 저장
    xmodmap -pke > ~/.Xmodmap

:h4:`참조`

* `Ubuntu 18.04 한글 입력기 UIM 설정하기 <http://progtrend.blogspot.com/2018/06/ubuntu-1804-uim.html>`_

단축키 설정
***********

* "설정 > 장치 > 키보드"에서 가장 하단의 + 버튼을 클릭하여 새로운 단축키를 추가할 수 있음

    * 시스템 모니터: 단축키는 윈도우즈와 같이 Ctrl + Shift + ESC 로 했음

    .. figure:: ../img/ubuntu/add_short_cut_for_system_monitor.png
        :scale: 80%

응용 프로그램 설치
******************

* KolourPaint: 윈도우즈의 그림판 같은 프로그램


명령어
=======

* find

    * `개발자를 위한 레시피, 리눅스 find 명령어 사용법. (Linux find command) - 리눅스 파일 검색. <https://recipes4dev.tistory.com/156>`_

* dpkg

    * 특정 패키지 설치여부 확인

    ::

        dpkg -l | grep python

* ufw

    * 방화벽 상태 확인

    ::

        ufw status verbose
        ufw status numbered

* alias

    * 별명 설정

    ::

        alias ls='ll -s'


* Disk 관련 내용

    * 용량 확인 (출처: `UNIX/LINUX : 용량 확인 명령어 (df/du) <http://ra2kstar.tistory.com/135>`_)

    ::

        df -h

    * Mount 여부 확인

    ::

        lsblk


* Process 사용자 확인

::

    ps -u -p 43401


* Touchpad setting

    * `ㅈㅅㄹ, xinput을 이용한 리눅스에서 터치패드 끄고 켜기 <https://zeph1e.tistory.com/88#recentEntries>`_

* CPU 정보 확인 (`Link <http://sarghis.com/blog/1136/>`_)

::

    cat /proc/cpuinfo


활용법
=======

* ISO 마운트

    * `애돌이의 얕고 넓은 샘, Furious ISO Mount - 리눅스에서 ISO 이미지를 마운트하자 <https://edoli.tistory.com/132>`_


Troubleshooting
================

Grub으로 부팅되는 경우
*********************

::

    grub rescue> ls
    (hd0) (hd1) (hd1,gpt1) (hd1,gpt2) ......

    grub rescue> ls (hd1,gpt10)/
    /boot ......

    grub rescue> set prefix=(hd1,gpt10)/boot/grub
    grub rescue> insmod normal
    grub rescue> normal

    $ sudo grub-install /dev/sda
    $ sudo update-grub

:h4:`출처`

* `Medium, Ubuntu 부팅시 발생하는 grub rescue 메세지 <https://medium.com/@jjeaby/ubuntu-%EB%B6%80%ED%8C%85%EC%8B%9C-%EB%B0%9C%EC%83%9D%ED%95%98%EB%8A%94-grub-rescue-%EB%A9%94%EC%84%B8%EC%A7%80-8dfc3ff8ffd9>`_
* `Umundu's Zapary, Ubuntu BIOS 및 UEFI Grub 복구 <https://zapary.blogspot.com/2014/08/ubuntu-bios-uefi-grub-recovery.html>`_
