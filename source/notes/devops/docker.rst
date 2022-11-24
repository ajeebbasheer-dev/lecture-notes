=======
Docker
=======

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

    host master {
        hardware ethernet 00:0c:29:5f:62:36;
        fixed-address 192.168.10.129;
    }


Now, restart the vmnetdhcp service::

    C:\ProgramData\VMware>net stop vmnetdhcp
    System error 109 has occurred.

    The pipe has been ended.


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
    [root@master ~]# ifconfig ens33 | grep -w inet
            inet 192.168.10.129  netmask 255.255.255.0  broadcast 192.168.10.255
    [root@master ~]# 





Containers
============

- A way to **package** application with all necessary dependencies and configuration.
- **Portable**, can be shared and moved around easily.
- **Container Repo**:

  - Containers live in container repositories. Many companies have their own private repositories where they host their containers.
  - Docker container has a public repository where you can find any application you want. This is called **Dockerhub**.

- What is a container?

  - Layers of images
  - Base is mostly a Linux image due it's small size
  - Then application image comes on top

  
.. image:: images/docker/layers.png
    :width: 600
    :align: center


Install Docker
===============

`Install docker <https://docs.docker.com/engine/install/>_`

To install on CentOS: https://docs.docker.com/engine/install/centos/

Need to install 3 things:

- Docker (Engine): Community edition.
- Docker CLI: To Run CLI commands.
- Docker compose: TBD


1. Setup Repo::

    sudo yum install -y yum-utils
    sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

2. Install Docker Engine::

    sudo yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin

3. Start docker::

    sudo systemctl start docker

4. Use the enable command to ensure that the service starts whenever the system boots::

    [root@master ~]# sudo systemctl enable docker
    Created symlink from /etc/systemd/system/multi-user.target.wants/docker.service to /usr/lib/systemd/system/docker.service.


5. Verify engine is installed::

    [root@master ~]# sudo docker run hello-world
    Unable to find image 'hello-world:latest' locally
    latest: Pulling from library/hello-world
    2db29710123e: Pull complete
    Digest: sha256:faa03e786c97f07ef34423fccceeec2398ec8a5759259f94d99078f264e9d7af
    Status: Downloaded newer image for hello-world:latest


see the image `hello-world` is not available locally. So, it is pulling from docker hub. 

Since docker hub is a public repo of thousands of application images, we don't need any authorization or password to provide. It will directly pull from the hub.

The next time you install a different version of same application, it will download only the changed layers.

For example, suppose you run nginx:1.22 for first time::

    [root@master ~]# docker run nginx:1.22
    Unable to find image 'nginx:1.22' locally
    1.22: Pulling from library/nginx
    e9995326b091: Pull complete
    6cc239fad459: Pull complete
    55bbc49cb4de: Pull complete
    a3949c6b4890: Pull complete
    b9e696b15b8a: Pull complete
    a8acafbf647e: Pull complete
    Digest: sha256:1e50e66b74695b703ab43b5c7d0cda4f682a6430ad1b1901d368ad32cb0aa8b3
    Status: Downloaded newer image for nginx:1.22
    /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
    /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
    /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
    10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
    10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
    /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
    /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
    /docker-entrypoint.sh: Configuration complete; ready for start up
    2022/11/12 04:04:53 [notice] 1#1: using the "epoll" event method
    2022/11/12 04:04:53 [notice] 1#1: nginx/1.22.1
    2022/11/12 04:04:53 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6)
    2022/11/12 04:04:53 [notice] 1#1: OS: Linux 3.10.0-1160.el7.x86_64
    2022/11/12 04:04:53 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
    2022/11/12 04:04:53 [notice] 1#1: start worker processes
    2022/11/12 04:04:53 [notice] 1#1: start worker process 29
    2022/11/12 04:04:53 [notice] 1#1: start worker process 30



These all are different layers of a docker application. When we pull a different version,

It will pull only the ones which are changed::

    [root@master ~]# docker run nginx:latest
    Unable to find image 'nginx:latest' locally
    latest: Pulling from library/nginx
    e9995326b091: Already exists ----------------->>> THIS IMAGE IS SAME, SO, NOT PULLED!
    71689475aec2: Pull complete
    f88a23025338: Pull complete
    0df440342e26: Pull complete
    eef26ceb3309: Pull complete
    8e3ed6a9e43a: Pull complete

Note that a **RUN** command will create a **Container**::

    [root@master ~]# docker ps
    CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS        PORTS     NAMES
    dde3dac78f19   nginx:latest   "/docker-entrypoint.…"   23 hours ago   Up 23 hours   80/tcp    crazy_booth

To run a container, it has to pull the images from docker hub (if not available locally)::

    [root@master ~]# docker image ls
    REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
    nginx        1.22      0ccb2559380c   2 weeks ago   142MB
    nginx        latest    76c69feac34e   2 weeks ago   142MB

.. important::
    - **docker pull**: Only pulls specified version of docker image.
    - **docker run**: Checks the image available locally, if not pull it from docker hub, then create a container using the image.
    - **docker start**: restarts a stopped container.
    - **docker stop**: stops a running container.
    - **docker run** = **docker pull** + **docker start**

.. important::
    - **docker run**: **Create** a **NEW** container with some attributes (-d, -p etc) set.
    - **docker start**: **Restarts** an **EXISTING** container with the attributes defined while creating the container.


Container vs Image
======================

**Container** is a running environment for **image**.

.. image:: images/docker/container.png
    :width: 600
    :align: center

- Container contains filesystem, configuration files, environment vars needed for running the image.
- A port is binded to the container to talk to the application running inside of a container.
- The file system inside a container is just a virtual abstraction of the host's filesystem

Docker basic commands
======================

First you need an image locally available to run a container. To pull an image::

    [root@master ~]# docker pull redis
    Using default tag: latest
    latest: Pulling from library/redis
    e9995326b091: Pull complete
    f2cd78d6f24c: Pull complete
    8f3614d34c89: Pull complete
    697fd51ec515: Pull complete
    a554cf50a327: Pull complete
    66f93c02e79c: Pull complete
    Digest: sha256:aeed51f49a6331df0cb2c1039ae3d1d70d882be3f48bde75cd240452a2348e88
    Status: Downloaded newer image for redis:latest
    docker.io/library/redis:latest

We have the latest redis image locally available::

    [root@master ~]# docker image ls
    REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
    redis        latest    c2342258f8ca   2 weeks ago   117MB
    [root@master ~]#

Now run the image::

    [root@master ~]# docker run redis
    1:C 13 Nov 2022 04:43:32.570 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
    1:C 13 Nov 2022 04:43:32.571 # Redis version=7.0.5, bits=64, commit=00000000, modified=0, pid=1, just started
    1:C 13 Nov 2022 04:43:32.575 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
    1:M 13 Nov 2022 04:43:32.577 * monotonic clock: POSIX clock_gettime
    1:M 13 Nov 2022 04:43:32.579 * Running mode=standalone, port=6379.
    1:M 13 Nov 2022 04:43:32.580 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
    1:M 13 Nov 2022 04:43:32.580 # Server initialized
    1:M 13 Nov 2022 04:43:32.580 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
    1:M 13 Nov 2022 04:43:32.582 * Ready to accept connections

In a different window::

    [root@master ~]# docker ps
    CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS      NAMES
    eb28e5664a9e   redis     "docker-entrypoint.s…"   48 seconds ago   Up 46 seconds   6379/tcp   admiring_snyder

Kill container as it runs in forground using CTRL+C::

    ^C1:signal-handler (1668314722) Received SIGINT scheduling shutdown...
    1:M 13 Nov 2022 04:45:22.125 # User requested shutdown...
    1:M 13 Nov 2022 04:45:22.125 * Saving the final RDB snapshot before exiting.
    1:M 13 Nov 2022 04:45:22.129 * DB saved on disk
    1:M 13 Nov 2022 04:45:22.129 # Redis is now ready to exit, bye bye...
    [root@master ~]#

    [root@master ~]# docker ps
    CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
    [root@master ~]#


Now to run as detached::

    [root@master ~]# docker run -d redis
    eceb714c89a25c870f1cc92849684579fd139707e34921c54a617a745ee5cbe2
    [root@master ~]#

You will get a **container-id** and you can see it's prefix in `docker ps`::

    [root@master ~]# docker ps
    CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS      NAMES
    eceb714c89a2   redis     "docker-entrypoint.s…"   About a minute ago   Up About a minute   6379/tcp   crazy_shockley

To see all the containers (including the stopped ones)::

    [root@master ~]# docker ps -a
    CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS                     PORTS      NAMES
    eceb714c89a2   redis     "docker-entrypoint.s…"   About a minute ago   Up About a minute          6379/tcp   crazy_shockley
    eb28e5664a9e   redis     "docker-entrypoint.s…"   4 minutes ago        Exited (0) 3 minutes ago              admiring_snyder

Use container id to start and stop the containers::

    [root@master ~]# docker stop eceb714c89a2
    eceb714c89a2
    [root@master ~]# docker ps
    CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
    [root@master ~]# docker start eb28e5664a9e
    eb28e5664a9e
    [root@master ~]# docker ps
    CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS        PORTS      NAMES
    eb28e5664a9e   redis     "docker-entrypoint.s…"   6 minutes ago   Up 1 second   6379/tcp   admiring_snyder
    [root@master ~]#


You can run different versions of same application::

    [root@master ~]# docker run redis:6.2
    Unable to find image 'redis:6.2' locally
    6.2: Pulling from library/redis
    e9995326b091: Already exists
    f2cd78d6f24c: Already exists
    8f3614d34c89: Already exists
    82dae2827019: Pull complete
    b7764d91f67c: Pull complete
    333b12b955b1: Pull complete
    Digest: sha256:ffd3d04c8f7832ccdda89616ebaf3cb38414b645ebbf76dbef1fc9c36a72a2d1
    Status: Downloaded newer image for redis:6.2
    1:C 13 Nov 2022 04:53:12.474 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
    1:C 13 Nov 2022 04:53:12.474 # Redis version=6.2.7, bits=64, commit=00000000, modified=0, pid=1, just started
    1:C 13 Nov 2022 04:53:12.474 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
    1:M 13 Nov 2022 04:53:12.476 * monotonic clock: POSIX clock_gettime
    1:M 13 Nov 2022 04:53:12.479 # A key '__redis__compare_helper' was added to Lua globals which is not on the globals allow list nor listed on the deny list.
    1:M 13 Nov 2022 04:53:12.480 * Running mode=standalone, port=6379.
    1:M 13 Nov 2022 04:53:12.480 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
    1:M 13 Nov 2022 04:53:12.480 # Server initialized
    1:M 13 Nov 2022 04:53:12.480 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
    1:M 13 Nov 2022 04:53:12.482 * Ready to accept connections

    [root@master ~]# docker ps
    CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS          PORTS      NAMES
    324432055b97   redis:6.2   "docker-entrypoint.s…"   24 seconds ago   Up 21 seconds   6379/tcp   beautiful_gould
    eb28e5664a9e   redis       "docker-entrypoint.s…"   10 minutes ago   Up 3 minutes    6379/tcp   admiring_snyder
    [root@master ~]#

Note that both listening on the same port!.. So, How does this work????


Container Port Vs Host Port
=============================

We have 2 versions of same application running now::

    [root@master ~]# docker ps
    CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS          PORTS      NAMES
    324432055b97   redis:6.2   "docker-entrypoint.s…"   24 seconds ago   Up 21 seconds   6379/tcp   beautiful_gould
    eb28e5664a9e   redis       "docker-entrypoint.s…"   10 minutes ago   Up 3 minutes    6379/tcp   admiring_snyder
    [root@master ~]#

Both listening on same port (which is specified on the image)!! How does this works?? Why there is no conflict?

We know that, container is a virtual environment running on your host. There will be multiple containers running simultaneously on your host.

Your host (laptop/pc) has certain ports available for applications. You need **port-binding** between host ports and container ports.

You will get a conflict (**Port in use error**) if you use same **host port**.

.. image:: images/docker/hostport.png
    :width: 600
    :align: center

To do the port binding, do run with `-p<HOST-PORT>:<CONTAINER-PORT>`::

    [root@master ~]# docker stop 389a5f0b3c94
    389a5f0b3c94

    [root@master ~]# docker run -d -p6000:6379 redis:6.2
    4920b547862f5266d14a83073d8f8157afc14ecf7f42ac68b420a835e6c87c9e
    [root@master ~]# docker ps
    CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS          PORTS                                                    NAMES
    4920b547862f   redis:6.2   "docker-entrypoint.s…"   7 seconds ago    Up 3 seconds    0.0.0.0:6000->6379/tcp, :::6000->6379/tcp                sleepy_rhodes
    eb28e5664a9e   redis       "docker-entrypoint.s…"   37 minutes ago   Up 30 minutes   6379/tcp                                                 admiring_snyder

You can connect to the running container using the host-port as `some-app://localhost:6000`.

Let's try to run the latest redis on the same host-port::

    [root@master ~]# docker run -d -p6000:6379 redis
    1c56a9724cc91d8016aab9de71df2ff20ba2ae1743cc93335b526bec89ac3a92
    docker: Error response from daemon: driver failed programming external connectivity on endpoint boring_goldstine (fae0d6ee8bbf6aedd18e14b6c535032e8fbaccf97ad235e4c941840e633f9dc1): Bind for 0.0.0.0:6000 failed: port is already allocated.

Let's try on different host-port::

    [root@master ~]# docker run -d -p6001:6379 redis
    e43b0aaa251366c855364ca98bcb886b24570531b95603d279a6a56caa105e46

    [root@master ~]# docker ps
    CONTAINER ID   IMAGE       COMMAND                  CREATED         STATUS         PORTS                                       NAMES
    e43b0aaa2513   redis       "docker-entrypoint.s…"   8 seconds ago   Up 5 seconds   0.0.0.0:6001->6379/tcp, :::6001->6379/tcp   gallant_sutherland
    4920b547862f   redis:6.2   "docker-entrypoint.s…"   3 minutes ago   Up 3 minutes   0.0.0.0:6000->6379/tcp, :::6000->6379/tcp   sleepy_rhodes

To changes the name of a container::

    [root@master ~]# docker run -d -p6000:6379 --name redis-older redis:6.2
    bad6659fab671ee94696ccc05813bb7e27260cd6551ab02c61d44d2c21c65e26

    [root@master ~]# docker ps
    CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS          PORTS                                       NAMES
    bad6659fab67   redis:6.2   "docker-entrypoint.s…"   5 seconds ago    Up 3 seconds    0.0.0.0:6000->6379/tcp, :::6000->6379/tcp   redis-older
    e43b0aaa2513   redis       "docker-entrypoint.s…"   14 minutes ago   Up 14 minutes   0.0.0.0:6001->6379/tcp, :::6001->6379/tcp   gallant_sutherland
    [root@master ~]#

Logging and debugging
======================

Use `docker logs <container-id>` to see the logs::

    [root@master ~]# docker logs e43b0aaa2513
    1:C 13 Nov 2022 05:24:22.726 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
    1:C 13 Nov 2022 05:24:22.726 # Redis version=7.0.5, bits=64, commit=00000000, modified=0, pid=1, just started
    1:C 13 Nov 2022 05:24:22.726 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
    1:M 13 Nov 2022 05:24:22.726 * monotonic clock: POSIX clock_gettime
    1:M 13 Nov 2022 05:24:22.728 * Running mode=standalone, port=6379.
    1:M 13 Nov 2022 05:24:22.728 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
    1:M 13 Nov 2022 05:24:22.728 # Server initialized
    1:M 13 Nov 2022 05:24:22.728 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
    1:M 13 Nov 2022 05:24:22.728 * Ready to accept connections
    [root@master ~]#


To login to interactive terminal::

    [root@master ~]# docker exec -it redis-older /bin/bash
    root@bad6659fab67:/data# ls
    root@bad6659fab67:/data# pwd
    /data

We can see the virtual filesystem inside the container::

    root@bad6659fab67:/data# cd /
    root@bad6659fab67:/# ls
    bin  boot  data  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var

To see the environment variables::

    root@bad6659fab67:/# env
    HOSTNAME=bad6659fab67
    REDIS_DOWNLOAD_SHA=b7a79cc3b46d3c6eb52fa37dde34a4a60824079ebdfb3abfbbfa035947c55319
    PWD=/
    HOME=/root
    REDIS_VERSION=6.2.7
    GOSU_VERSION=1.14
    TERM=xterm
    REDIS_DOWNLOAD_URL=http://download.redis.io/releases/redis-6.2.7.tar.gz
    SHLVL=1
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    _=/usr/bin/env
    OLDPWD=/data

Clean up::

    [root@master ~]# docker stop bad6659fab67
    bad6659fab67
    [root@master ~]# docker stop gallant_sutherland
    gallant_sutherland
    [root@master ~]# docker rm gallant_sutherland
    gallant_sutherland
    [root@master ~]# docker rm redis-older
    redis-older
    [root@master ~]# docker ps
    CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
    [root@master ~]# docker rmi redis
    Error response from daemon: conflict: unable to remove repository reference "redis" (must force) - container eb28e5664a9e is using its referenced image c2342258f8ca
    [root@master ~]# docker rmi redis --force
    Untagged: redis:latest
    Untagged: redis@sha256:aeed51f49a6331df0cb2c1039ae3d1d70d882be3f48bde75cd240452a2348e88
    Deleted: sha256:c2342258f8ca7ab5af86e82df6e9ade908a949216679667b0f39b59bcd38c4e9
    [root@master ~]# docker rmi redis:6.2 --force
    Untagged: redis:6.2
    Untagged: redis@sha256:ffd3d04c8f7832ccdda89616ebaf3cb38414b645ebbf76dbef1fc9c36a72a2d1
    Deleted: sha256:4608773ab2dbb8cc2db17ecf700305ddc0f93a5a5ad9989b9f5c4ffea222efb8
    [root@master ~]# docker images



Deploy mongo with docker
==========================

- Mongo-express is a web-based MongoDB admin interface written in Node. js, Express. js, and Bootstrap3.
- First we need to pull docker images of both from repo. Search at https://hub.docker.com for mongo.
- You can find all details including, docker-compose format, docker stack details, environment variables etc at https://hub.docker.com/_/mongo

pull the `mongo` image::

    [root@master ~]# docker pull mongo
    Using default tag: latest
    latest: Pulling from library/mongo
    eaead16dc43b: Pull complete
    8a00eb9f68a0: Pull complete
    f683956749c5: Pull complete
    b33b2f05ea20: Pull complete
    3a342bea915a: Pull complete
    fa956ab1c2f0: Pull complete
    138a8542a624: Pull complete
    acab179a7f07: Pull complete
    f88335710e84: Pull complete
    Digest: sha256:71a63fc2438e45714f6c8a2505968ee0beeb94ec77a88ef12190f7cee9b95f32
    Status: Downloaded newer image for mongo:latest
    docker.io/library/mongo:latest


Pull the mongo-express image (https://hub.docker.com/_/mongo-express)::

    [root@master ~]# docker pull mongo-express
    Using default tag: latest
    latest: Pulling from library/mongo-express
    6a428f9f83b0: Pull complete
    f2b1fb32259e: Pull complete
    40888f2a0a1f: Pull complete
    4e3cc9ce09be: Pull complete
    eaa1898f3899: Pull complete
    ab4078090382: Pull complete
    ae780a42c79e: Pull complete
    e60224d64a04: Pull complete
    Digest: sha256:2a25aafdf23296823b06bc9a0a2af2656971262041b8dbf11b40444804fdc104
    Status: Downloaded newer image for mongo-express:latest
    docker.io/library/mongo-express:latest

::

    [root@master ~]# docker images
    REPOSITORY      TAG       IMAGE ID       CREATED         SIZE
    mongo           latest    b70536aeb250   2 weeks ago     695MB
    mongo-express   latest    2d2fb2cabc8f   12 months ago   136MB

Ok. Now we have two applications. How can we connect these two. Mongo-express need to communicate with mongo to get the db data.

For that, we have something called **Docker Network**.

.. important::
    - **Isolated Docker Network**: Two containers can talk to each other using just **Container Name**. No port or localhost is required.

.. image:: images/docker/isolatednw.png
    :width: 600
    :align: center

Applications which are outside of this network can connect them using localhost and port number.

When we run our app from outside.

.. image:: images/docker/app_outside.png
    :width: 600
    :align: center

When we create a docker image of our application. Here, browser runs from outside. So, the entire thing that we are going to develop will look like,

.. image:: images/docker/app_inside.png
    :width: 600
    :align: center


To see the networks auto generated so far::

    [root@master ~]# docker network ls
    NETWORK ID     NAME      DRIVER    SCOPE
    84244377a9b6   bridge    bridge    local
    350c58ba2bf8   host      host      local
    71f03a16c8a5   none      null      local

Let's create a new network for mongo and mongo-express::

    [root@master ~]# docker network create mongo-network
    09dfde03c9ed44a9ef534dc51396249a58253e148ebc11bc432d88ffd26a6d15
    [root@master ~]# docker network ls
    NETWORK ID     NAME            DRIVER    SCOPE
    84244377a9b6   bridge          bridge    local
    350c58ba2bf8   host            host      local
    09dfde03c9ed   mongo-network   bridge    local
    71f03a16c8a5   none            null      local

To add mongo and mongo-express in the same network, we need to use the network when running the container.

Before running the container, check the environment variable provided at `https://hub.docker.com/_/mongo`.

.. image:: images/docker/envvars.png
    :width: 600
    :align: center

Run the container::

    [root@master ~]#  docker run -d \
    > -p 27017:27017 \
    > -e MONGO_INITDB_ROOT_USERNAME=admin \
    > -e MONGO_INITDB_ROOT_PASSWORD=Melcow1 \
    > --name mongodb \
    > --net mongo-network \
    > mongo
    ddee1d84dedbfc240bdfab74022cf676d21e5324df4397d8dd78687f62893074
    [root@master ~]#

- `-d`: detached
- `-d`: environment variable
- `--name`: name of the container.
- `--net`: name of the docker network.
- `mongo`: image name

::

    [root@master ~]# docker ps
    CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                                                                 NAMES
    ddee1d84dedb   mongo     "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:27017->27017/tcp, :::27017->270                      17/tcp   mongodb

To see what is happening::

    [root@master ~]# docker logs ddee1d84dedb
    about to fork child process, waiting until server is ready for connections.
    forked process: 28

    {"t":{"$date":"2022-11-15T06:27:23.603+00:00"},"s":"I",  "c":"CONTROL",  "id":20698,   "ctx":"-","msg":"***** SERVER RESTARTED *****"}

    . . .

    {"t":{"$date":"2022-11-15T06:27:37.874+00:00"},"s":"I",  "c":"STORAGE",  "id":22262,   "ctx":"initandlisten","msg":"Timestamp monitor starting"}
    {"t":{"$date":"2022-11-15T06:27:37.879+00:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"/tmp/mongodb-27017.sock"}}
    {"t":{"$date":"2022-11-15T06:27:37.879+00:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"0.0.0.0"}}
    {"t":{"$date":"2022-11-15T06:27:37.879+00:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":27017,"ssl":"off"}}

Now start mongo express.

.. image:: images/docker/mongoexpress_cmd.png
    :width: 600
    :align: center

::

    [root@master ~]# docker run -d \
    > -p 8081:8081 \
    > -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
    > -e ME_CONFIG_MONGODB_ADMINPASSWORD=Melcow1 \
    > --net mongo-network \
    > --name mongo-express \
    > -e ME_CONFIG_MONGODB_SERVER=mongodb \
    > mongo-express
    6664999245ef651d0913e5dd69e49ae4f84aec4b67a332194540caa98d4082ca

Note that ME_CONFIG_MONGODB_SERVER is the **container name** of mongo that we created earlier.

::

    [root@master ~]# docker logs 6664999245ef651d0913e5dd69e49ae4f84aec4b67a332194540caa98d4082ca
    Welcome to mongo-express
    ------------------------


    (node:7) [MONGODB DRIVER] Warning: Current Server Discovery and Monitoring engine is deprecated, and will be removed in a future version. To use the new Server Discover and Monitoring engine, pass option { useUnifiedTopology: true } to the MongoClient constructor.
    Mongo Express server listening at http://0.0.0.0:8081
    Server is open to allow connections from anyone (0.0.0.0)
    basicAuth credentials are "admin:pass", it is recommended you change this in your config.js!

See mongo-express running on the server.

.. image:: images/docker/mongoexpress_gui.png
    :width: 600
    :align: center

.. important::
    - The database created and the contents will be **permanently lost when you restart the container**. Docker has concept called **Volumes** to avoid this case.

Deploy mongo with docker compose
=================================

Docker compose is a tool to automate running multiple containers with all the environment setup.

Docker run command for mongo was::

    docker run -d \
    > -p 27017:27017 \
    > -e MONGO_INITDB_ROOT_USERNAME=admin \
    > -e MONGO_INITDB_ROOT_PASSWORD=Melcow1 \
    > --name mongodb \
    > --net mongo-network \
    > mongo

Docker run command for mongo-express was::

    docker run -d \
    > -p 8081:8081 \
    > -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
    > -e ME_CONFIG_MONGODB_ADMINPASSWORD=Melcow1 \
    > --net mongo-network \
    > --name mongo-express \
    > -e ME_CONFIG_MONGODB_SERVER=mongodb \
    > mongo-express

Corresponding docker compose file will look like.

mongo-docker-compose.yaml::

    version: '3' # latest version of docker compose.
    services:
        mongodb:                            # container name (--name mongodb)
            image: mongo                    # image name
            ports:
                - 27017:27017               # HOST:CONTAINER
            environment:
                - MONGO_INITDB_ROOT_USERNAME=admin
                - MONGO_INITDB_ROOT_PASSWORD=Melcow1
        mongo-express:                      # container name (--name mongo-express)
            image: mongo-express
            ports:
                - 8081:8081
            environment:
                - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
                - ME_CONFIG_MONGODB_ADMINPASSWORD=Melcow1
                - ME_CONFIG_MONGODB_SERVER=mongodb

.. important:: Docker Compose will automatically create a common network for these containers!!

Let's remove the running container to avoid port conflict::

    [root@master ~]# docker stop mongodb
    mongodb
    [root@master ~]# docker stop mongo-express
    mongo-express
    [root@master ~]# docker rm mongodb
    mongodb
    [root@master ~]# docker rm mongo-express
    mongo-express

::

    [root@master ~]# cat mongo-docker-compose.yaml
    version: '3'
    services:
        mongodb:
            image: mongo
            ports:
                - 27017:27017
            environment:
                - MONGO_INITDB_ROOT_USERNAME=admin
                - MONGO_INITDB_ROOT_PASSWORD=Melcow1
        mongo-express:
            image: mongo-express
            ports:
                - 8081:8081
            environment:
                - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
                - ME_CONFIG_MONGODB_ADMINPASSWORD=Melcow1
                - ME_CONFIG_MONGODB_SERVER=mongodb

Run docker-compose (note it creates a network)::

    [root@master ~]# docker-compose -f mongo-docker-compose.yaml up
    Creating network "root_default" with the default driver
    Creating root_mongodb_1       ... done
    Creating root_mongo-express_1 ... done
    Attaching to root_mongo-express_1, root_mongodb_1
    mongodb_1        | about to fork child process, waiting until server is ready for connections.

    "Listening on","attr":{"address":"0.0.0.0"}}
    mongodb_1        | {"t":{"$date":"2022-11-15T07:26:45.104+00:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":27017,"ssl":"off"}}

However, we can see only mongo container is running::

    [root@master ~]# docker ps
    CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                           NAMES
    76e40d378bb8   mongo     "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   0.0.0.0:27017->27017/tcp, :::27017->27017/tcp   root_mongodb_1

    [root@master ~]# docker ps --all
    CONTAINER ID   IMAGE           COMMAND                  CREATED         STATUS                      PORTS     NAMES
    499f09f8e43d   mongo-express   "tini -- /docker-ent…"   3 minutes ago   Exited (0) 3 minutes ago              root_mongo-express_1


Mongo-express was stopped with error::

    mongo-express_1  | Welcome to mongo-express
    mongo-express_1  | ------------------------
    mongo-express_1  |
    mongo-express_1  |
    mongo-express_1  | (node:6) [MONGODB DRIVER] Warning: Current Server Discovery and Monitoring engine is deprecated, and will be removed in a future version. To use the new Server Discover and Monitoring engine, pass option { useUnifiedTopology: true } to the MongoClient constructor.
    mongo-express_1  | Could not connect to database using connectionString: mongodb://admin:Melcow1@mongodb:27017/"
    mongo-express_1  | (node:6) UnhandledPromiseRejectionWarning: MongoNetworkError: failed to connect to server [mongodb:27017] on first connect [Error: connect ECONNREFUSED 172.19.0.3:27017

This is because mongo-express came up before mongo is up. To resolve this issue we can provide a strict restart policy as follows::

    [root@master ~]# cat mongo-docker-compose.yaml
    version: '3'
    services:
      mongodb:
        image: mongo
        ports:
          - '27017:27017'
        environment:
          - MONGO_INITDB_ROOT_USERNAME=admin
          - MONGO_INITDB_ROOT_PASSWORD=Melcow1
      mongo-express:
        image: mongo-express
        ports:
          - '8081:8081'
        environment:
          - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
          - ME_CONFIG_MONGODB_ADMINPASSWORD=Melcow1
          - ME_CONFIG_MONGODB_SERVER=mongodb
        restart: unless-stopped


::

    [root@master ~]# docker-compose -f mongo-docker-compose.yaml up
    Creating root_mongo-express_1 ... done
    Creating root_mongodb_1       ... done
    Attaching to root_mongo-express_1, root_mongodb_1
    . . .
    mongo-express_1  | Welcome to mongo-express
    mongo-express_1  | ------------------------
    mongo-express_1  |
    mongo-express_1  |
    mongo-express_1  | (node:7) [MONGODB DRIVER] Warning: Current Server Discovery and Monitoring engine is deprecated, and will be removed in a future version. To use the new Server Discover and Monitoring engine, pass option { useUnifiedTopology: true } to the MongoClient constructor.
    mongo-express_1  | Could not connect to database using connectionString: mongodb://admin:Melcow1@mongodb:27017/"
    mongo-express_1  | (node:7) UnhandledPromiseRejectionWarning: MongoNetworkError: failed to connect to server [mongodb:27017] on first connect [Error: connect ECONNREFUSED 172.19.0.3:27017

    . . .
    mongo-express_1  | Welcome to mongo-express
    mongo-express_1  | ------------------------
    mongo-express_1  |
    mongo-express_1  |
    mongo-express_1  | (node:7) [MONGODB DRIVER] Warning: Current Server Discovery and Monitoring engine is deprecated, and will be removed in a future version. To use the new Server Discover and Monitoring engine, pass option { useUnifiedTopology: true } to the MongoClient constructor.
    mongo-express_1  | Could not connect to database using connectionString: mongodb://admin:Melcow1@mongodb:27017/"
    mongo-express_1  | (node:7) UnhandledPromiseRejectionWarning: MongoNetworkError: failed to connect to server [mongodb:27017] on first connect [Error: connect ECONNREFUSED 172.19.0.3:27017
    . . . 
    mongodb_1        | MongoDB init process complete; ready for start up.
    . . .
    
    mongo-express_1  | Welcome to mongo-express
    mongo-express_1  | ------------------------
    mongo-express_1  |
    mongo-express_1  |
    mongo-express_1  | (node:7) [MONGODB DRIVER] Warning: Current Server Discovery and Monitoring engine is deprecated, and will be removed in a future version. To use the new Server Discover and Monitoring engine, pass option { useUnifiedTopology: true } to the MongoClient constructor.
    mongo-express_1  | Could not connect to database using connectionString: mongodb://admin:Melcow1@mongodb:27017/"
    mongo-express_1  | (node:7) UnhandledPromiseRejectionWarning: MongoNetworkError: failed to connect to server [mongodb:27017] on first connect [Error: connect ECONNREFUSED 172.19.0.3:27017
    . . .
    
    mongodb_1        | {"t":{"$date":"2022-11-15T09:17:59.092+00:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"/tmp/mongodb-27017.sock"}}
    mongodb_1        | {"t":{"$date":"2022-11-15T09:17:59.092+00:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"0.0.0.0"}}
    mongodb_1        | {"t":{"$date":"2022-11-15T09:17:59.092+00:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":27017,"ssl":"off"}}

    . . .
    Bmongo-express_1  | Welcome to mongo-express
    mongo-express_1  | ------------------------
    mongo-express_1  |
    mongo-express_1  |
    mongo-express_1  | (node:7) [MONGODB DRIVER] Warning: Current Server Discovery and Monitoring engine is deprecated, and will be removed in a future version. To use the new Server Discover and Monitoring engine, pass option { useUnifiedTopology: true } to the MongoClient constructor.
    mongodb_1        | {"t":{"$date":"2022-11-15T09:18:02.642+00:00"},"s":"I",  "c":"NETWORK",  "id":22943,   "ctx":"listener","msg":"Connection accepted","attr":{"remote":"172.19.0.2:38548","uuid":"f65c8ebd-43f1-40c5-8446-a60776165427","connectionId":1,"connectionCount":1}}

    mongo-express_1  | Mongo Express server listening at http://0.0.0.0:8081


You can see as soon as mongodb is up, the connection is established and mongo-express starts running..

.. image:: images/docker/megui.png
    :width: 600
    :align: center

Both containers are running::

    [root@master ~]# docker ps
    CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS          PORTS                                           NAMES
    4806dd6ece42   mongo           "docker-entrypoint.s…"   11 minutes ago   Up 11 minutes   0.0.0.0:27017->27017/tcp, :::27017->27017/tcp   root_mongodb_1
    b58426805322   mongo-express   "tini -- /docker-ent…"   11 minutes ago   Up 11 minutes   0.0.0.0:8081->8081/tcp, :::8081->8081/tcp       root_mongo-express_1


Build your docker image
========================

Let's create a python application first using falcon.

Create your app
----------------

myapp.py::

    import json
    import falcon

    class ObjRequestClass:
        def on_get(self, req, resp):
            content = {
                "name": "ajeeb",
                "place": "bangalore"
            }
            resp.body = json.dumps(content)

    app = falcon.API()
    app.add_route('/test', ObjRequestClass())

prerequisites::

    yum install python3
    python3 -m venv venv
    pip install gunicorn
    pip install falcon

Start the app::

    gunicorn app:api
    (venv) [root@master demo]# gunicorn --bind 0.0.0.0:8182 myapp:app
    [2022-11-19 07:42:42 -0800] [35043] [INFO] Starting gunicorn 20.1.0
    [2022-11-19 07:42:42 -0800] [35043] [INFO] Listening at: http://0.0.0.0:8182 (35043)
    [2022-11-19 07:42:42 -0800] [35043] [INFO] Using worker: sync
    [2022-11-19 07:42:42 -0800] [35046] [INFO] Booting worker with pid: 35046
    /root/demo/myapp.py:12: DeprecatedWarning: Call to deprecated function __init__(...). API class may be removed in a future release, use falcon.App instead.
      app = falcon.API()


From another terminal::

    [root@master ~]# curl -X GET http://127.0.0.1:8182/test
    {"name": "ajeeb", "place": "bangalore"}

Dockerize app
--------------

Create a Dockerfile.

- **FROM python**: Install python as the base image.
- **RUN**: Execute any Linux command INSIDE the container.
- **COPY**: Perform copy command on the host.
- **CMD**: Executes the entry point.

.. important::
    - RUN executes **inside** the container
    - COPY executes **on the host**.
    - To copy from inside, we can do **RUN cp** command.

**DOCKER FILE**

::

    [root@master demo]# cat Dockerfile
    FROM python

    EXPOSE 8182

    # Important: RUN executes inside the container, COPY executes on the host.
    # Install gunicorn & falcon
    RUN pip install gunicorn falcon

    # Create a directory INSIDE the Container
    RUN mkdir -p /home/app

    # Copy everything from the current folder (on the host) to app directory.
    COPY . /home/app

    CMD ["gunicorn", "--bind", "0.0.0.0:8182", "/home/app/myapp:app"]


**Build image using Dockerfile**:

If pip install ends up in `[Warning] IPv4 forwarding is disabled. Networking will not work.`, do the following.

add the following to /etc/sysctl.conf::

    net.ipv4.ip_forward=1

See the changes are affected::

    [root@master demo]# systemctl restart network
    [root@master demo]# sysctl net.ipv4.ip_forward
    net.ipv4.ip_forward = 1

Build the image::

    [root@master demo]# docker build -t myapp:1.0 .
    Sending build context to Docker daemon  12.17MB
    Step 1/6 : FROM python
     ---> ee4e7a0f1c35
    Step 2/6 : EXPOSE 8182
     ---> Using cache
     ---> f1e490acf7c3
    Step 3/6 : RUN pip install gunicorn falcon
     ---> Running in e68a49cd20ac
    Collecting gunicorn
      Downloading gunicorn-20.1.0-py3-none-any.whl (79 kB)
         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 79.5/79.5 kB 651.9 kB/s eta 0:00:00
    Collecting falcon
      Downloading falcon-3.1.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (9.1 MB)
         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.1/9.1 MB 4.0 MB/s eta 0:00:00
    Requirement already satisfied: setuptools>=3.0 in /usr/local/lib/python3.11/site-packages (from gunicorn) (65.5.0)
    Installing collected packages: gunicorn, falcon
    Successfully installed falcon-3.1.1 gunicorn-20.1.0
    WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager        . It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

    [notice] A new release of pip available: 22.3 -> 22.3.1
    [notice] To update, run: pip install --upgrade pip
    Removing intermediate container e68a49cd20ac
     ---> bdcdbc100d15
    Step 4/6 : RUN mkdir -p /home/app
     ---> Running in af06b2e20274
    Removing intermediate container af06b2e20274
     ---> d2cea6f0bbe9
    Step 5/6 : COPY . /home/app
     ---> 4e8d27b0f06d
    Step 6/6 : CMD ["gunicorn", "--bind", "0.0.0.0:8182", "/home/app/myapp:app"]
     ---> Running in adff3d2f9bca
    Removing intermediate container adff3d2f9bca
     ---> b18545478c51
    Successfully built b18545478c51
    Successfully tagged myapp:1.0

You can see the image you build::

    [root@master demo]# docker images
    REPOSITORY      TAG               IMAGE ID       CREATED         SIZE
    myapp           1.0               b18545478c51   2 minutes ago   996MB
    python          latest            ee4e7a0f1c35   3 days ago      932MB
    rabbitmq        3.11-management   a97320763e5e   8 days ago      263MB
    mongo           latest            b70536aeb250   3 weeks ago     695MB
    mongo-express   latest            2d2fb2cabc8f   13 months ago   136MB

Run the container::

    [root@master demo]# docker run -d -p8182:8182 --name my-falcon-app myapp:1.0
    4fdfbaa0bef4c8b874305c6d02b633fa2bff60fd061a873b73c76408d7a2823d

Something went wrong::

    [root@master demo]# docker ps | grep myapp
    [root@master demo]# docker ps --all| grep myapp
    4fdfbaa0bef4   myapp:1.0                  "gunicorn --bind 0.0…"   2 minutes ago    Exited (3) 2 minutes ago                                                                                                                                                          my-falcon-app

Let's see the logs::

    [root@master demo]# docker logs 4fdfbaa0bef4
    [2022-11-19 16:07:29 +0000] [1] [INFO] Starting gunicorn 20.1.0
    [2022-11-19 16:07:29 +0000] [1] [INFO] Listening at: http://0.0.0.0:8182 (1)
    [2022-11-19 16:07:29 +0000] [1] [INFO] Using worker: sync
    [2022-11-19 16:07:29 +0000] [7] [INFO] Booting worker with pid: 7
    [2022-11-19 16:07:29 +0000] [7] [ERROR] Exception in worker process
    ...
    ModuleNotFoundError: No module named '/home/app/myapp'

Before rebuild, delete stopped container and the image::

    [root@master demo]# docker rm 4fdfbaa0bef4
    4fdfbaa0bef4
    [root@master demo]# docker rmi b18545478c51
    Untagged: myapp:1.0
    Deleted: sha256:b18545478c5111d37d11f4732a40d015476133d6ddb8a3363350c0b2ac829720
    Deleted: sha256:4e8d27b0f06df3972ee46a2f9d27a5f8df050367ff32f6ae35f993ba1c2c3dc1
    Deleted: sha256:6dd6e4f0c908cd9602a1c937da787aa526591696f230c927a994677603691741
    Deleted: sha256:d2cea6f0bbe9fdd5b989a6d8ab04c9a44eb87c553107f5bed36b7b3140072a2a
    Deleted: sha256:3243b69afe82415a76c870b9cfad5c850f7a4c9a6905003f31b4ff22b2d9cf49
    Deleted: sha256:bdcdbc100d159ce6a354ae9e37ac8da801e130706245fd17cd4e097b3fc1e50e
    Deleted: sha256:c278daead33e90f564115c1c5c46fb3a8bfcfacc7f1ebfb7952c3cda2cd0ac34

Correct the Dockerfile::

    FROM python

    EXPOSE 8182

    # Install gunicorn & falcon
    RUN pip install gunicorn falcon

    # Create a directory INSIDE the Container
    RUN mkdir -p /home/app

    # Copy everything from the current folder (on the host) to app directory.
    COPY . /home/app

    WORKDIR /home/app

    CMD ["gunicorn", "--bind", "0.0.0.0:8182", "myapp:app"]

Build the image::

    [root@master demo]# docker build -t myapp:1.0 .
    Sending build context to Docker daemon  12.17MB
    Step 1/7 : FROM python
     ---> ee4e7a0f1c35
    Step 2/7 : EXPOSE 8182
     ---> Using cache
     ---> f1e490acf7c3
    Step 3/7 : RUN pip install gunicorn falcon
     ---> Running in 9f8ef354385a
    Collecting gunicorn
      Downloading gunicorn-20.1.0-py3-none-any.whl (79 kB)
         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 79.5/79.5 kB 505.7 kB/s eta 0:00:00
    Collecting falcon
      Downloading falcon-3.1.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (9.1 MB)
         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.1/9.1 MB 1.3 MB/s eta 0:00:00
    Requirement already satisfied: setuptools>=3.0 in /usr/local/lib/python3.11/site-packages (from gunicorn) (65.5.0)
    Installing collected packages: gunicorn, falcon
    Successfully installed falcon-3.1.1 gunicorn-20.1.0
    [notice] A new release of pip available: 22.3 -> 22.3.1
    [notice] To update, run: pip install --upgrade pip
    Removing intermediate container 9f8ef354385a
     ---> 963b143c6a7a
    Step 4/7 : RUN mkdir -p /home/app
     ---> Running in 0dc8698fe6aa
    Removing intermediate container 0dc8698fe6aa
     ---> 33ec89eaf10c
    Step 5/7 : COPY . /home/app
     ---> c1201874f3c4
    Step 6/7 : WORKDIR /home/app
     ---> Running in bc55fa8e7363
    Removing intermediate container bc55fa8e7363
     ---> ef216069d3ba
    Step 7/7 : CMD ["gunicorn", "--bind", "0.0.0.0:8182", "myapp:app"]
     ---> Running in 3c7683a57ea2
    Removing intermediate container 3c7683a57ea2
     ---> 45362d2909f9
    Successfully built 45362d2909f9
    Successfully tagged myapp:1.0

Run the container::

    [root@master demo]# docker run -d -p8182:8182 --name my-falcon-app myapp:1.0
    525f94695e0c895458956147953ea143a51ef5cc0b6514f969555f2ad320228b
    [root@master demo]# docker ps| grep myapp
    525f94695e0c   myapp:1.0                  "gunicorn --bind 0.0…"   12 seconds ago   Up 12 seconds   0.0.0.0:8182->8182/tcp, :::8182->8182/tcp                                                                                                             my-falcon-app

Test the endpoint::

    (venv) [root@master ~]# curl -X GET http://127.0.0.1:8182/test
    {"name": "ajeeb", "place": "bangalore"}(venv) [root@master ~]#
