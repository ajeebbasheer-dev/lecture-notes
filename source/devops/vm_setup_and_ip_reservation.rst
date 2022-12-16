===============================
VMWare VM and IP Reservations
===============================

Setup (Windows)
================

1. `Download VMWare Workstation Pro <https://www.vmware.com/in/products/workstation-pro/workstation-pro-evaluation.html>`_

2. Install using the Key: **ZF3R0-FHED2-M80TY-8QYGC-NPKYF**

3. `Download Centos7 (CentOS-7-x86_64-DVD-2009.iso) of 4GB size <http://isoredirect.centos.org/centos/7/isos/x86_64/>`_

4. Open terminal and verify the CPU cores and RAM.

::

    [master@localhost ~]$ hostnamectl
       Static hostname: localhost.localdomain
             Icon name: computer-vm
               Chassis: vm
            Machine ID: fbc15474d58147fe924ee5ce817f3973
               Boot ID: 46ee5457fc8644249fe154d4dae10c35
        Virtualization: vmware
      Operating System: CentOS Linux 7 (Core)
           CPE OS Name: cpe:/o:centos:centos:7
                Kernel: Linux 3.10.0-1160.el7.x86_64
          Architecture: x86-64


::

    [master@localhost ~]$ uname -a
    Linux localhost.localdomain 3.10.0-1160.el7.x86_64 #1 SMP Mon Oct 19 16:18:59 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
    [master@localhost ~]$ hostname
    localhost.localdomain


2 CPU cores::

    [master@localhost ~]$ lscpu
    Architecture:          x86_64
    CPU op-mode(s):        32-bit, 64-bit
    Byte Order:            Little Endian
    CPU(s):                2
    On-line CPU(s) list:   0,1
    Thread(s) per core:    1
    Core(s) per socket:    1
    Socket(s):             2
    NUMA node(s):          1
    Vendor ID:             GenuineIntel
    CPU family:            6
    Model:                 154
    Model name:            12th Gen Intel(R) Core(TM) i5-1235U
    Stepping:              4
    CPU MHz:               2495.999
    BogoMIPS:              4991.99
    Hypervisor vendor:     VMware
    Virtualization type:   full
    L1d cache:             48K
    L1i cache:             32K
    L2 cache:              1280K
    L3 cache:              12288K
    NUMA node0 CPU(s):     0,1

4GB RAM::

    [master@localhost ~]$ free -th
                  total        used        free      shared  buff/cache   available
    Mem:           3.7G        845M        2.2G         29M        715M        2.6G
    Swap:          2.0G          0B        2.0G
    Total:         5.7G        845M        4.2G

5. Verify we are able to connect to internet.

::

        .google.com (142.250.77.164) 56(84) bytes of data.
    64 bytes from maa05s17-in-f4.1e100.net (142.250.77.164): icmp_seq=1 ttl=128 time=292 ms
    64 bytes from maa05s17-in-f4.1e100.net (142.250.77.164): icmp_seq=2 ttl=128 time=30.0 ms

    --- www.google.com ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1000ms
    rtt min/avg/max/mdev = 30.034/161.085/292.136/131.051 ms

6. Get IP address and login from Putty.

::

    [master@localhost ~]$ ip addr
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host 
           valid_lft forever preferred_lft forever
    2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        link/ether 00:0c:29:5f:62:36 brd ff:ff:ff:ff:ff:ff
        inet 192.168.10.129/24 brd 192.168.10.255 scope global noprefixroute dynamic ens33
           valid_lft 1230sec preferred_lft 1230sec
        inet6 fe80::a8b3:f8bc:7cab:bb9f/64 scope link noprefixroute 
           valid_lft forever preferred_lft forever
    3: virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
        link/ether 52:54:00:71:d6:67 brd ff:ff:ff:ff:ff:ff
        inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
           valid_lft forever preferred_lft forever
    4: virbr0-nic: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master virbr0 state DOWN group default qlen 1000
        link/ether 52:54:00:71:d6:67 brd ff:ff:ff:ff:ff:ff


We can see localhost instead of Master::

    [root@localhost ~]#


7. Change hostname to Master

::

    [root@localhost ~]# hostnamectl set-hostname Master

After Reboot::

    [root@master ~]# hostname
    master
    [root@master ~]# hostnamectl
       Static hostname: master
       Pretty hostname: Master
             Icon name: computer-vm
               Chassis: vm
            Machine ID: fbc15474d58147fe924ee5ce817f3973
               Boot ID: 335cc717cdb74c80b74ae710c6a05489
        Virtualization: vmware
      Operating System: CentOS Linux 7 (Core)
           CPE OS Name: cpe:/o:centos:centos:7
                Kernel: Linux 3.10.0-1160.el7.x86_64
          Architecture: x86-64


Setup Reservations
=====================

To change the hostname::

    [root@localhost ~]# hostname devmachine
    [root@localhost ~]# hostname -f
    devmachine


This `ProgramData` folder is hidden and may not be visible in file explorer::

    C:\ProgramData\VMware>dir
     Volume in drive C is Windows
     Volume Serial Number is 7804-EB2C

     Directory of C:\ProgramData\VMware

    17-11-2022  15:24    <DIR>          .
    10-11-2022  16:24    <DIR>          logs
    10-11-2022  16:22             1,731 vmnetdhcp.conf
    17-11-2022  15:24                 0 vmnetdhcp.leases
    17-11-2022  15:24             1,512 vmnetdhcp.leases~
    11-11-2022  17:21                19 vmnetnat-mac.txt
    10-11-2022  16:21             2,780 vmnetnat.conf
    10-11-2022  16:21    <DIR>          VMware KVM
    10-11-2022  16:22    <DIR>          VMware USB Arbitration Service
    10-11-2022  16:21    <DIR>          VMware Workstation
    10-11-2022  16:21    <DIR>          vnckeymap
                   5 File(s)          6,042 bytes
                   6 Dir(s)  422,884,003,840 bytes free


Open DHCP Config::

    C:\ProgramData\VMware>notepad vmnetdhcp.conf


::

    host devmachine {
        hardware ethernet 00:0c:29:5f:62:36;
        fixed-address 192.168.10.129;
    }


Now, restart the vmnetdhcp service::

    C:\ProgramData\VMware>net stop vmnetdhcp
    The VMware DHCP Service service is stopping.
    The VMware DHCP Service service was stopped successfully.


    C:\ProgramData\VMware>net start vmnetdhcp
    The VMware DHCP Service service is starting.
    The VMware DHCP Service service was started successfully.

Release and renew current lease, before that make sure you are root::

    [master@master ~]$ su - root
    Password: 
    Last login: Tue Nov 15 01:18:39 PST 2022 from 192.168.10.1 on pts/4
    Last failed login: Thu Nov 17 03:11:12 PST 2022 on pts/0
    There was 1 failed login attempt since the last successful login.
    [root@master ~]# 

Release and renew::

    [root@master ~]# dhclient
    [root@master ~]# ifconfig ens33 | grep -w inet
            inet 192.168.10.129  netmask 255.255.255.0  broadcast 192.168.10.255
    [root@master ~]# 

Doesn't matter how many times you release and renew, it always get the same IP::

    [root@master ~]# dhclient -r
    [root@master ~]# dhclient
    [root@localhost ~]# ifconfig ens33 | grep -w inet
        inet 192.168.10.129  netmask 255.255.255.0  broadcast 192.168.10.255





