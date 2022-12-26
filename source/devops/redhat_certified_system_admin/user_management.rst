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


