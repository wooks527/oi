=======
Ubuntu
=======

설치
====

* `HiSEON, 우분투 18.04 설치 <https://hiseon.me/linux/ubuntu/install-ubuntu-18-04/>`_
* `서지스원 @IT. 블로그 매거진, 리눅스 스왑(SWAP) 파티션이란 무엇? 어떤 일을 하나요? <https://sergeswin.com/1034>`_


명령어
=======

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

여러 가지 문제들
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
