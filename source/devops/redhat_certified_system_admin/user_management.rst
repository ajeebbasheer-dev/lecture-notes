================
User Management
================

To list logged-in users (I have python shell in one terminal, did `cat > myfile` in another)::

    [root@localhost ~]# w
     20:33:09 up  9:25,  3 users,  load average: 0.10, 0.10, 0.07
    USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
    root     pts/0    192.168.10.1     20:24    5.00s  0.10s  0.03s w
    root     pts/1    192.168.10.1     19:31    1:09   0.22s  0.08s python
    root     pts/2    192.168.10.1     20:32   13.00s  0.08s  0.00s cat

    [root@localhost ~]# who
    root     pts/0        2022-12-25 20:24 (192.168.10.1)
    root     pts/1        2022-12-25 19:31 (192.168.10.1)
    root     pts/2        2022-12-25 20:32 (192.168.10.1)

The **last** command reports the history of successful user login attempts and reboots::

    [root@localhost ~]# last
    root     pts/2        192.168.10.1     Sun Dec 25 20:32   still logged in
    root     pts/0        192.168.10.1     Sun Dec 25 20:24   still logged in
    root     pts/1        192.168.10.1     Sun Dec 25 19:31   still logged in
    root     pts/0        192.168.10.1     Sat Dec 24 18:22 - 19:39 (1+01:16)
    root     pts/2        192.168.10.1     Sat Dec 24 09:00 - 19:39 (1+10:39)
    root     pts/1        192.168.10.1     Fri Dec 23 00:19 - 19:36 (1+19:16)
    root     pts/0        192.168.10.1     Wed Dec 21 22:57 - 09:11 (2+10:14)
    root     pts/1        192.168.10.1     Mon Dec 19 02:49 - 02:50  (00:01)
    root     pts/0        192.168.10.1     Mon Dec 19 02:11 - 06:16 (1+04:04)
    reboot   system boot  3.10.0-1160.el7. Mon Dec 19 02:10 - 20:36 (6+18:26)

::

    [root@localhost ~]# last reboot
    reboot   system boot  3.10.0-1160.el7. Mon Dec 19 02:10 - 06:43 (18+04:33)
    reboot   system boot  3.10.0-1160.el7. Sat Nov 26 10:49 - 06:43 (40+19:54)

    wtmp begins Sat Nov 26 10:49:22 2022

To list failed user login attempts, use **lastb**::

    [root@localhost ~]# lastb

    btmp begins Sun Jan  1 09:13:27 2023 // btmp is the log file name

To see recent login attempts of all users, use **lastlog**::

    [root@localhost ~]# lastlog
    Username         Port     From             Latest
    root             pts/0    192.168.10.1     Fri Jan  6 06:43:49 -0800 2023
    bin                                        **Never logged in**
    daemon                                     **Never logged in**
    adm                                        **Never logged in**
    ...
    tcpdump                                    **Never logged in**
    dev-machine      :0                        Sat Nov 26 10:50:12 -0800 2022
    user100          pts/1                     Sun Dec 25 20:22:22 -0800 2022
    user200          pts/2                     Sat Dec 24 09:05:41 -0800 2022

Use **id** command to list the user and group details::

    [root@localhost ~]# id
    uid=0(root) gid=0(root) groups=0(root) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
    [root@localhost ~]# id user100
    uid=1001(user100) gid=1001(user100) groups=1001(user100),9999(mygrp)
    [root@localhost ~]# id user200
    uid=1002(user200) gid=1002(user200) groups=1002(user200),9999(mygrp)

Local User Authentication Files
================================

RHEL supports three fundamental user account types:

    - root/superuser: administrator, has full access. created by default during installation.
    - normal: have user-level privileges, cannot perform any admin functions, but can run programs authorized for them.
    - service: specific to services. example: apache, ftp, mail, and chrony

User account information for local users is stored in four files (and their backups):

    - /etc/passwd: plain text file with user login info.
    - /etc/group: plain text file with group info.
    - /etc/shadow: contains hashed user passwords. no access permissions for any user, **not even for root**.
    - /etc/gshadow: contains hashed group passwords no access permissions for any user, **not even for root**.

::

    [root@localhost ~]# head -1 /etc/passwd
    root:x:0:0:root:/root:/bin/bash
    [root@localhost ~]# head -1 /etc/group
    root:x:0:
    [root@localhost ~]# head -1 /etc/shadow
    root:$1$vg17.YPu$eSluAh46C.zH/4LVSWUQ6/::0:99999:7:::
    [root@localhost ~]# head -1 /etc/gshadow
    root:::


To view contents of useradd file::

    [root@localhost ~]# useradd -D
    GROUP=100
    HOME=/home
    INACTIVE=-1
    EXPIRE=
    SHELL=/bin/bash
    SKEL=/etc/skel
    CREATE_MAIL_SPOOL=yes

Useradd, usermod, and userdel
===============================

To add a user::

    [root@localhost ~]# useradd ajeebdev
    [root@localhost ~]# passwd ajeebdev
    Changing password for user ajeebdev.
    New password:

::

    [root@localhost etc]# cd /etc ; grep ajeebdev: passwd shadow group gshadow
    passwd:ajeebdev:x:1003:1003::/home/ajeebdev:/bin/bash
    shadow:ajeebdev:$1$ZBEMKPsx$fyHMI3IdBpz76gBcXfbeU1:19363:0:99999:7:::
    group:ajeebdev:x:1003:
    gshadow:ajeebdev:!::

    [ajeebdev@localhost ~]$ id
    uid=1003(ajeebdev) gid=1003(ajeebdev) groups=1003(ajeebdev) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023

To set password aging, use **chage**::

    [root@localhost etc]# chage -m 7 -M 28 -W 5 -E 2023-01-15 user100
    [root@localhost etc]# chage -l user100
    Last password change                                    : Dec 24, 2022
    Password expires                                        : Jan 21, 2023
    Password inactive                                       : never
    Account expires                                         : Jan 15, 2023
    Minimum number of days between password change          : 7
    Maximum number of days between password change          : 28
    Number of days of warning before password expires       : 5


The `su`, `su -` and `sudo`
=============================

2 can carry out tasks that requires special previlages in 2 ways:

1. Substitute user: switch the user who has previlages to execute a task.

    - `su`: without executing startup scripts(which setup the environment).
    - `su -`: by executing startup scripts.

::

    [root@localhost ~]# su user100
    [user100@localhost root]$ whoami
    user100
    [user100@localhost root]$ logname  // who really am I.
    root

2. Superuser: If the user is in `/etc/sudoers` file, then we can use sudo command to do admin tasks.



