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

원격 접속 설정
**************

설치 방법은 다음과 같다.

* `RORYMON, How to: RDP to Ubuntu <https://www.rorymon.com/blog/how-to-rdp-to-ubuntu/>`_
* `Linuxize, How to Install Xrdp Server (Remote Desktop) on Ubuntu 18.04 <https://linuxize.com/post/how-to-install-xrdp-on-ubuntu-18-04/>`_

----------------
Troubleshooting
----------------

* Home folder에 접근할 수 없는 경우

    * 해결법

        * thinclient_drives를 Unmount 하고 폴더 이름 앞에 . 을 붙인다.

        ::

            sudo umount -f thinclinet_drives
            sudo mv thinclient_drives .thinclient_drives

    * 참조
    
        * `StackExchange, Annoying problem w/ xrdp <https://unix.stackexchange.com/questions/474844/annoying-problem-w-xrdp>`_


명령어
=======

* find

    * find / | grep docker ￩ / 폴더에서 docker가 들어간 모든 파일 검색
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


* iptables

    * Rule 삭제

        * 명령어
    
        ::

            sudo iptables -D [Chain명] [Rule number]

        * 예시

        ::

            sudo iptables -D DOCKER 4


    * 참조: `How To List and Delete Iptables Firewall Rules <https://www.digitalocean.com/community/tutorials/how-to-list-and-delete-iptables-firewall-rules>`_

* Ram의 속도와 Type 확인

    * 명령어

    ::

        sudo dmidecode --type memory | less

    * 참조

        * `VITUX, How to check the installed RAM on your Ubuntu System <https://vitux.com/how-to-check-the-installed-ram-on-your-ubuntu-system/>`_

* 삭제된 파일 복구

    * 방법
    
        * GUI 상에서 단순히 파일을 삭제를 한 경우에는 :code:`restore-trash` 라는 명령어로 손쉽게 복구할 수 있음
        * 위 명령어를 사용하기 위해서는 apt-get :code:`install trash-cli` 명령어로 trash-cli 패키지를 설치해야 함

    * 참조

        * `NightShadow의 블로그, [우분투 리눅스] 콘솔(터미널)에서 휴지통을 사용하는 방법. trash-cli <https://nightshadow.tistory.com/entry/%EC%9A%B0%EB%B6%84%ED%88%AC-%EB%A6%AC%EB%88%85%EC%8A%A4-%EC%BD%98%EC%86%94%ED%84%B0%EB%AF%B8%EB%84%90%EC%97%90%EC%84%9C-%ED%9C%B4%EC%A7%80%ED%86%B5%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-trashcli>`_


활용법
=======

* Mount

    * 하드디스크 마운트

        * `냉정과 열정사이, [Ubuntu] 추가 하드디스크 마운트 방법 <https://psychoria.tistory.com/521>`_
        * `파란크리스마스, Ubuntu 디스크 mount 하기 <https://bluexmas.tistory.com/632>`_

    * ISO 마운트

        * `애돌이의 얕고 넓은 샘, Furious ISO Mount - 리눅스에서 ISO 이미지를 마운트하자 <https://edoli.tistory.com/132>`_

* GUI에서 Root 폴더 보기

    * `StackExchange, root folder access via gui <https://askubuntu.com/questions/422950/root-folder-access-via-gui>`_

* 분할 압축 및 해제

    * Zip

        * `Tech, [Linux] 여러 파일로 분할 압축하고 해제하기 <https://m.blog.naver.com/wideeyed/221499054123>`_

    * 7zip

        * `ysh0222, 7zip 분할 압축 & 해제 <https://ysh0222.tistory.com/26>`_



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

gdm 문제로 부팅되지 않는 경우
*****************************

* 상황

    *  NVIDIA GPU를 2개 설치한 경우 갑자기 부팅되지 않는 현상 발생

* 오류 메시지

    * stopped user manager for uid 121
    * removed slice user slice of gdm

* 원인

    * gdm3가 X window와 연결하는 역할을 하는 것 같은데 제대로 동작하지 않음
    * NVIDIA 드라이버 gdm 사이에 뭔가 문제가 있는 것 같음

* 해결법

    * recovery 모드로 들어가서 (이 때 network 연결시켜야 함) nvidia 드라이버 관련 내용 제거

    ::

        apt-get purge nvidia*

    * lightdm을 설치하여 X window를 여는 도구 변경 후 재부팅

    ::

        apt-get install lightdm
        reboot
  
    * 참조

        * `ask ubuntu, Booting Problem - Ubuntu GNOME 16.04.01 LTS <https://askubuntu.com/a/826641>`_
        * `Ubuntu gdm3 package, Ubuntu does not finish boot, crashes loading gdm3 <https://bugs.launchpad.net/ubuntu/+source/gdm3/+bug/1768041>`_

* 추가 사항

    * gdm이 반복적으로 로그인하는 부분 해제하려면 coutom.conf 파일에서 WaylandEnable=false를 주석 처리하면 됨

        * 코드

        ::

            vi /etc/gdm3 custom.conf
    
        * 참조

            * `ubuntu forum, 17.10 upgrade, worked at first, hanging on reboot, GPU? <https://ubuntuforums.org/showthread.php?t=2377243>`_ 

    * Change display manager

        * 코드

        ::

            sudo dpkg-reconfigure gdm

        * 참조

            * `ask ubuntu, Can't seem to get my login screen back after installing slim <https://askubuntu.com/a/2594>`_

    * ``Ctrl`` + ``Alt`` + ``F2`` 를 누르면 Terminal에 접속할 수 있음
    
        * 참고로 Display manager에는 gdm3, lightdm, startx 등이 있음
        
        * 참조: `Q4OS Forum, GDM broke my system - there's anyway to re-enable TDM or LightDM? <https://www.q4os.org/forum/viewtopic.php?id=2195>`_

Remminar
*********

* Windows로 원격 접속 시 H264 관련 문제 발생

    * 해결법

        * Color depth를 High color (16bpp)로 변경하면 됨

    * 참조

        *`GitLab, Your libfreerdp does not support H264 <https://gitlab.com/Remmina/Remmina/issues/1584>`_
