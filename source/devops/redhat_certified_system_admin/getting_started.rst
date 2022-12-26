================
Getting Started
================

Useful commands
================

To see tree command with fullpath (-f), size (-h), permissons (-p) and include hidden files (-a)::

    [root@localhost work]# tree -phf
    .
    ├── [-rw------- 2.7K]  ./anaconda-ks.cfg
    └── [drwxr-xr-x   38]  ./project01
        ├── [-rw-r--r--    0]  ./project01/licence
        └── [-rw-r--r--    0]  ./project01/README.md

To see human readable file sizes, use `-h` with tree and ls commands::

    [root@localhost ~]# ls -lh
    total 8.0K
    -rw-------. 1 root root 2.8K Nov 26 10:48 anaconda-ks.cfg
    -rw-------. 1 root root 2.1K Nov 26 10:48 original-ks.cfg
    drwxr-xr-x. 4 root root   60 Dec 19 02:28 work

To inspect system's uptime::

    [root@localhost ~]# uptime
     02:51:41 up 41 min,  1 user,  load average: 0.17, 0.08, 0.06

To determine a command (which, whereis and type)::

    [root@localhost ~]# which pwd
    /usr/bin/pwd
    [root@localhost ~]# whereis pwd
    pwd: /usr/bin/pwd /usr/include/pwd.h /usr/share/man/man1/pwd.1.gz /usr/share/man/man1p/pwd.1p.gz
    [root@localhost ~]# type pwd
    pwd is a shell builtin


To view description about something::

    [root@localhost ~]# whatis yum.conf
    yum.conf (5)         - Configuration file for yum(8).
    [root@localhost ~]# whatis pwd
    pwd (1)              - print name of current/working directory
    pwd (1p)             - return working directory name


System info::

    [root@localhost ~]# uname -a
    Linux localhost.localdomain 3.10.0-1160.el7.x86_64 #1 SMP Mon Oct 19 16:18:59 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux

To view CPU specs::

    [root@localhost ~]# lscpu
    Architecture:          x86_64
    CPU op-mode(s):        32-bit, 64-bit
    Byte Order:            Little Endian
    CPU(s):                1
    On-line CPU(s) list:   0
    Thread(s) per core:    1
    Core(s) per socket:    1
    Socket(s):             1
    NUMA node(s):          1
    Vendor ID:             GenuineIntel
    CPU family:            6
    Model:                 154
    Model name:            12th Gen Intel(R) Core(TM) i5-1235U
    Stepping:              4
    CPU MHz:               2495.998
    BogoMIPS:              4991.99
    Hypervisor vendor:     VMware
    Virtualization type:   full
    L1d cache:             48K
    L1i cache:             32K
    L2 cache:              1280K
    L3 cache:              12288K
    NUMA node0 CPU(s):     0

Command Lookups (`man -k` or `apropos`)::

    [root@localhost ~]# man -k pwd
    lckpwdf (3)          - get shadow password file entry
    pwd (1)              - print name of current/working directory
    pwd (1p)             - return working directory name
    pwd.h (0p)           - password structure
    pwdx (1)             - report current working directory of a process
    ulckpwdf (3)         - get shadow password file entry
    unix_chkpwd (8)      - Helper binary that verifies the password of the current user

    [root@localhost ~]# apropos ssh-a
    ssh-add (1)          - adds private key identities to the authentication agent
    ssh-agent (1)        - authentication agent
    ssh-pkcs11-helper (8) - ssh-agent helper program for PKCS#11 support

To create a short file (type the lines you need to save in the file)::

    [root@localhost ~]# cat > newfile
    this is a one line file
    Ctrl+C

    [root@localhost ~]# cat newfile
    this is a one line file

To create a file old dated::

    [root@localhost ~]# touch -d 2019-09-08 oldfile
    [root@localhost ~]# ls -lrt oldfile
    -rw-r--r--. 1 root root 0 Sep  8  2019 oldfile

The `tac` does reverse of `cat`::

    [root@localhost ~]# cat myfile
    line #1
    line #2
    line #3
    [root@localhost ~]# tac myfile
    line #3
    line #2
    line #1

Both less and more are text filters that are used for viewing long text files one page at a time, starting at the beginning.

- The less command is more capable than the more command.
- less does not need to read the entire file before it starts to display its contents, thus making it faster.
- more: limited to forward text searches.
- less: both forward and backward.

Copy by preserving permissions (using `-p`)::

    [root@localhost ~]# ls -ltr myfile
    -r---wx--x. 1 root root 24 Dec 21 23:56 myfile

    [root@localhost ~]# cp myfile /tmp/
    [root@localhost ~]# ls -lrt /tmp/myfile
    -rw-r--r--. 1 root root 24 Dec 22 00:32 /tmp/myfile   # PERMISSIONS NOT PRESERVED

    [root@localhost ~]# cp -p myfile /tmp/
    [root@localhost ~]# ls -lrt /tmp/myfile
    -r---wx--x. 1 root root 24 Dec 21 23:56 /tmp/myfile   # PERMISSIONS PRESERVED!!

To list logged-in users (I have python shell in one terminal, did `cat > myfile` in another)::

    [root@localhost ~]# w
     20:33:09 up  9:25,  3 users,  load average: 0.10, 0.10, 0.07
    USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
    root     pts/0    192.168.10.1     20:24    5.00s  0.10s  0.03s w
    root     pts/1    192.168.10.1     19:31    1:09   0.22s  0.08s python
    root     pts/2    192.168.10.1     20:32   13.00s  0.08s  0.00s cat

Use `getfacl` command to see the permissions more readable::

    [root@localhost tmp]# getfacl myfile
    # file: myfile
    # owner: root
    # group: root
    user::rw-
    group::r--
    other::r--

Note the pattern is actually `user:GID:permission`. Example: `::rw-`

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


History
=========

Unix
-----

- Unix was **NOT** an opensource software.
- Unix source code was licensable via agreements with its owner, AT&T Bell Labs. The first known software license was sold to the University of Illinois in 1975.
- Key People of Bell Labs research facility: Kenn Thompson (Unix philosophy) and Dennis Ritchie (C Programming).
- Unix, written in C, made it portable across, multiple hardware architectures.
- Unix grew quickly. Berkeley became the center of unix research and new delivery of Unix was born called **BSD** (Berkeley Software Distribution). Initially, BSD was not an alternative to AT&T's Unix, but an add-on with additional software and capabilities.
- 2BSD (in 1979) came with 2 now-famous programs `vi` and `C Shell (/bin/csh)`.
- By 1880s, Unix's commercial offerrings exploded. HP-UX, IBM's AIX, Sun's Solaris, Sequent, and Xenix all joined the `Unix Family`.
- So, standardization became the new focus. That's how the POSIX standard was born in 1988.
- Separately, the BSD family of operating systems had grown over the years, leading to some open source variations that were released under the now-familiar BSD license.  FreeBSD, OpenBSD, and NetBSD.
- OS X (now macOS) operating system is a BSD-derivative.

Linux
------

- The GNU Project (GNU's Not Unix): By Richard Stallman, an American software engineer
    
    - **Truly free and open source** alternative to the **proprietary Unix** system.
    - **UNIX-compatible**
    - Started in 1984 and by 1991, significant software had been developed (Except the Kernel)

- Linux (The Kernel): By Linus Torvalds, A Finnish computer science student.
- Linux got integrated with GNU software gradually and it become GNU/Linux or simply Linux.
- **GNU GPL**: Provides public access to its source code free of charge and with full consent to amend, package, and redistribute.

Unix and Linux
---------------

- Unix is proprietary, Linux is opensource.
- Because of POSIX standards and compliance, software written on Unix could be compiled for a Linux operating system with a usually limited amount of porting effort.
- Many open source software components available on Linux are easily available through tools like Homebrew as MAC OS is BSD-like.
- Many of the advancements in Linux have been adopted in the Unix world  For example, IBM's AIX offered an AIX Toolbox for Linux Applications with hundreds of GNU software packages (like Bash, GCC, OpenLDAP, and many others) that could be added to an AIX installation to ease the transition between Linux and Unix-based AIX systems.
- Proprietary Unix is still alive.
- The BSD branch of the Unix tree is open source, and NetBSD, OpenBSD, and FreeBSD all have strong user bases.
- Linux is very common now: The Raspberry Pi, Android devices, smart TVs, etc.
- Many of today's most popular cloud-native stacks are Linux-based (container runtimes, Kubernetes etc.).
- Windows operating system would "run Linux" in 2016.  Windows Subsystem for Linux (WSL), Windows port of Docker etc. shows that Linux will continue to rule the world.

Linux from Red Hat
-------------------

- Red Hat, Inc., founded in 1993.
- In 1994, Redhad released the first **commercial Linux operating system distribution** called Red Hat Linux (RHL).
- Renamed to **RHEL** (RedHat Enterprise Linux) in 2003.
- RHL was originally assembled and enhanced within the Red Hat company. In 2003, Red Hat sponsored and facilitated the **Fedora Project** and invited the user community to join hands in enhancing and updating the source code.
- **RHEL is commercial, Fedora is completely free**

Download RHEL 8 Developer Version
----------------------------------

- Register and login at https://developers.redhat.com/login and download.

- GNOME Display Manager: Default display manager in RHEL.

    .. image:: _images/gnome.png
      :width: 400
      :align: center

File Systems
===============

- File Systems: Linux files are organized logically in a hierarchy for ease of administration and recognition. This organization is maintained in hundreds of directories located in larger containers called file systems.
- RHEL follows FHS (Filesystem Hierarchy Standard) which describes names, locations, and permissions.
- The root of the directory is represented by the forward slash (`/`).
- Top level directories

    .. image:: _images/top_level_dirs.png
      :width: 400
      :align: center

- There are a variety of file system types supported in RHEL, categorized in three basic groups.

    - **disk-based**: physical file-systems created on Hard Drive / USB flash drive.
    - **network-based**: disk-based file-systems that are shared over the network for remote access.
    - **memory-based**: virtual, created automatically at startup and destroyed when system goes down.

- disk and network-based file-systems store data persistantly. data stored on virtual file-systems is lost at reboots.

.. important::
    - During RHEL installation, two disk-based file systems are created when you select the default partitioning.
    - **root** and **boot** file systems.

Root file-system (`/`) - Disk Based
-----------------------------------

- Top-level file system in the FHS.
- /etc [extended text configuration]: Holds system configuration files. Common subdirectories are systemd, sysconfig, lvm (logical volume manager) skel etc.
- /root: default home location for root user. Size is automatically determined by installer program.
- /mnt: This directory is used to mount a file system temporarily
- /home: To store user home directories and other user contents.
- /opt: Optional Directory. A subdirectory is created for each installed software.
- /usr (UNIX System Resources Directory): Contains most of the system files.

    - /usr/bin:  Crucial user executable commands.
    - /usr/sbin ( System Binary): Crucial system administration commands that are are not intended for execution by normal users. **This directory is not included in the default search path for normal users**.
    - /usr/lib (or usr/lib64): Contains shared library routines, system initialization and service management programs.
    - /usr/include: header files for C.
    - /usr/local:  Serves as a system administrator repo for storing commands and tools downloaded from web, in-house or else where. Not generally comes with Linux dist.

        - /usr/local/bin: executables.
        - /usr/local/etc: configuration.
        - /usr/local/lib: library routines.
    - /usr/share: location for manual pages, documentation, templates, configuration files etc.
    - /usr/src: to store source code

- /var: Contains data that frequently changes. Logs, status, spool, lock and other dynamic data.

    - **/var/log**: **system logs, boot logs, user logs, failed user logs, installation logs, cron logs, mail logs** etc.
    - /var/opt: logs, status and other files for tools installed under /opt.
    - /var/opt: queue items before being sent out to their intended destinations are located here.
    - **/var/tmp**: Large temporary files or **temporary files that need to exist for longer periods of time than what is typically allowed in /tmp**.  These files survive system reboots and stay for **30 days**.

- /tmp: repo for temporary files. Many programs create temporary files here during runtime or installation. Will survive reboots and stay for 10 days.

The Boot File System (/boot) – Disk-Based
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Contains the **Linux kernel**, boot support files, and boot configuration files.

The Devices File System (/dev) - Virtual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Used to store device nodes for physical hardware and virtual devices.
- **The Linux kernel communicates with these devices through corresponding device nodes located here**.
- with these devices through corresponding device nodes located by the **udevd** service.
- Two types of device files:

    - **Character (raw) devices**: Accessed serially with streams of bits transferred during kernel and device communication. Example **console, serial printers, mice, keyboards, terminals**.
    - **Block devices**: Accessed in a parallel fashion with data exchanged in blocks (parallel) during kernel and device communication. Examples: Hard Disc, Optical Drives, etc. 

The Procfs File System (/proc) - Virtual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Used to maintain information about the current state of the running kernel.
- This includes the details for current hardware configuration and status information on CPU memory, disks, partitioning, file systems, networking, running processes, and so on.
- Contain thousands of **zero-length pseudo files**.
- Created in memory at system boot time updated during runtime, and destroyed at system shutdown.

The Runtime File System (/run) - Virtual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Repo for process data.
- /run/media: also used **to automatically mount external file systems such as those that are on optical (CD and DVD) and flash USB**.

The System File System (/sys) - Virtual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Information about hardware devices, drivers, and some kernel features.


GNOME Terminal Session
------------------------

- hash sign (#): root user
- dollar sign ($): normal user

Linux allocates unique pseudo (or virtual) numbered device files to represent terminal sessions opened by users on the system.  By default, these files are stored in the /dev/pts

When there was only one terminal::

    [root@localhost ~]# tty
    /dev/pts/0

Opened one more and the tty of the new terminal::

    [root@localhost ~]# tty
    /dev/pts/1

If we delete first and create a new terminal, new one will have the 0 index.

List commands (ls -l) explained
--------------------------------

::

    [root@localhost ~]# ls -l
    total 8
    -rw-------. 1 root root 2789 Nov 26 10:48 anaconda-ks.cfg
    -rw-------. 1 root root 2069 Nov 26 10:48 original-ks.cfg
    drwxr-xr-x. 4 root root   60 Dec 19 02:28 work

- Column #1: 

    - first character: Hyphen (-) indicates files and `d` indicates directory.
    - next 9 characters: permissions
- Column #2: Number of links
- Column #3: Owner name
- Column #4: Owner's group name.
- Column #5: File size in bytes. For directories, this is the number of blocks used by the directory to hold info about it's contents.
- Columns 6, 7, and 8: Month day time
- Column 9: name

