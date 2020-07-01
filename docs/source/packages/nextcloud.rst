==========
Nextcloud
==========

Nextcloud is open source file sync and share software for everyone from individuals operating the free Nextcloud Server in the privacy of their own home, to large enterprises and service providers supported by the Nextcloud Enterprise Subscription. Nextcloud provides a safe, secure, and compliant file synchronization and sharing solution on servers that you control.

Accessing Nextcloud files using WebDAV
=======================================

Accessing files using Linux
****************************

You can use below address:

::

    davs://[server_url]/nextcloud/remote.php/dav/files/[username]/

If you can't access your Nextcloud server, then it can work to remove nextcloud words from above address.

----------------
Troubleshooting
----------------

* `I am getting an Error 302 Found trying to mount the directory using WebDAV <davs://cloud.lab.loopback.kr/remote.php/dav/files/hwk/>`_
* `How to Access Your Nextcloud Files via WebDAV on Ubuntu Desktop <https://www.linuxbabe.com/cloud-storage/access-nextcloud-files-webdav-ubuntu>`_
* `시놀로지 webDAV 설정 (외부에서 윈도우 탐색기로 나스 접속) <https://gumu.kr/blog/422/%EC%8B%9C%EB%86%80%EB%A1%9C%EC%A7%80-webdav-%EC%84%A4%EC%A0%95-%EC%99%B8%EB%B6%80%EC%97%90%EC%84%9C-%EC%9C%88%EB%8F%84%EC%9A%B0-%ED%83%90%EC%83%89%EA%B8%B0%EB%A1%9C-%EB%82%98%EC%8A%A4-%EC%A0%91/>`_

:h2:`Reference`

* `Nextcloud manual <https://docs.nextcloud.com/server/18/user_manual/contents.html>`_
