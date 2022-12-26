================
File Management
================

Common File Types
===================

RHEL supports seven types of files (ls -l first character):

    - regular (-)
    - directory (d)
    - block special device (b)
    - character special device (c)
    - symbolic link (l)
    - named pipe
    - socket (s)

Linux doesn't require an extension to identify the type. We have `file` and `stat` command to identify the type.


The 'file' command::

    [root@localhost ~]# file anaconda-ks.cfg
    anaconda-ks.cfg: ASCII text

    [root@localhost ~]# file work/
    work/: directory

    [root@localhost dev]# file /dev/sda2
    /dev/sda2: block special

    [root@localhost dev]# file /dev/tty0
    /dev/tty0: character special

    [root@localhost dev]# file /dev/core
    /dev/core: symbolic link to `/proc/kcore'

    [root@localhost ~]# file /var/run/gssproxy.sock
    /var/run/gssproxy.sock: socket


The 'stat' command::

    [root@localhost ~]# stat anaconda-ks.cfg
      File: ‘anaconda-ks.cfg’
      Size: 2789            Blocks: 8          IO Block: 4096   regular file
    Device: 803h/2051d      Inode: 33574981    Links: 1
    Access: (0600/-rw-------)  Uid: (    0/    root)   Gid: (    0/    root)
    Context: system_u:object_r:admin_home_t:s0
    Access: 2022-12-19 02:28:44.925923345 -0800
    Modify: 2022-11-26 10:48:36.877202069 -0800
    Change: 2022-11-26 10:48:36.877202069 -0800
     Birth: -

    [root@localhost ~]# stat work/
      File: ‘work/’
      Size: 60              Blocks: 0          IO Block: 4096   directory
    Device: 803h/2051d      Inode: 33803040    Links: 4
    Access: (0755/drwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
    Context: unconfined_u:object_r:admin_home_t:s0
    Access: 2022-12-19 02:28:47.767917251 -0800
    Modify: 2022-12-19 02:28:44.924923347 -0800
    Change: 2022-12-19 02:28:44.924923347 -0800
     Birth: -

    [root@localhost dev]# stat /dev/tty0
      File: ‘/dev/tty0’
      Size: 0               Blocks: 0          IO Block: 4096   character special file

- **major number**: Every hardware device such as a disk, CD/DVD, printer, and terminal has an associated device driver loaded in the kernel. The kernel communicates with hardware devices through their respective device drivers. Each device driver is assigned a unique number called the **major number**, which the kernel uses to recognize its type.
- **minor number**: There may be more than one instance of the same device type in the system. In that case, the same driver is used to control all those instances. For example, SATA device driver controls all SATA hard disks and CD/DVD drives. The kernel in this situation allots a minor number to each individual device within that device driver category to identify it as a unique device.

.. important::
    - **Major Number**: Points to the device driver. 
    - **Minor Number**: Points to a unique device or partition that the device driver controls.

Here major number 8 represents block device driver for SATA disks. 1,2 & 3 are minor numbers ::

    [root@localhost ~]# ls -l /dev/sda*
    brw-rw----. 1 root disk 8, 0 Dec 19 02:10 /dev/sda
    brw-rw----. 1 root disk 8, 1 Dec 19 02:10 /dev/sda1
    brw-rw----. 1 root disk 8, 2 Dec 19 02:10 /dev/sda2
    brw-rw----. 1 root disk 8, 3 Dec 19 02:10 /dev/sda3

This means:

    - first (1) partition on your first (a) SATA drive is /dev/sda1
    - second (2) partition on your first (a) SATA drive is /dev/sda2
 
Character devices::

    2 pty:
    1 mem
    3 ttyp
    4 ttyS
    6 lp
    7 vcs
    10 misc
    13 input
    14 sound
    21 sg
    180 usb

Block devices:

    2 fd - floppy disk
    8 sd - SCSI drive in general, but is mostly popular for SATA drives and CD/DVD
    11 sr

Compression and Archiving
==========================

RHEL offers a multitude of compression tools such as gzip (gunzip) and bzip2 (bunzip2).

Using gzip and gunzip
-----------------------

- adds the .gz extension to each file.
- can be used with the -r option to compress an entire directory tree.
- `-l` option to display compression info.


To compress the file fstab located in the /etc directory copy this file in the root user’s home directory.

::

    [root@localhost ~]# cp /etc/fstab .
    [root@localhost ~]# gzip fstab
    [root@localhost ~]# ls -l fstab.gz
    -rw-r--r--. 1 root root 317 Dec 19 03:56 fstab.gz
    [root@localhost ~]# gzip -l fstab.gz
         compressed        uncompressed  ratio uncompressed_name
                317                 501  41.5% fstab


To decompress this file, use the gunzip command::

    [root@localhost ~]# gunzip fstab.gz
    [root@localhost ~]# ls
    anaconda-ks.cfg  fstab  original-ks.cfg  work

Using bzip2 and bunzip2
-------------------------

- adds the .bz2 extension.
- bzip2 has a better compression ratio (smaller target file size), but it is slower.

::

    [root@localhost ~]# bzip2 fstab
    [root@localhost ~]# ls -lrt fstab*
    -rw-r--r--. 1 root root 348 Dec 19 03:56 fstab.bz2

To decompress this file, use the bunzip2::

    [root@localhost ~]# bunzip2 fstab.bz2
    [root@localhost ~]# ls -lrt fstab*
    -rw-r--r--. 1 root root 501 Dec 19 03:56 fstab

Using tar (tape archive)
-------------------------

- The single file created using tar command is called **tarball** or **tarfile**.

Use `-c` to create a tarball for entire directory. Use `f` to specify filename::

    [root@localhost ~]# tar -cvf /tmp/home.tar /home
    [root@localhost ~]# ls -ltr /tmp/home.tar
    -rw-r--r--. 1 root root 3962880 Dec 21 23:12 /tmp/home.tar

To create a tarball called /tmp/files.tar containing only selected files::

    [root@localhost ~]# tar -cvf files.tar /etc/passwd /etc/yum.conf
    tar: Removing leading `/' from member names
    /etc/passwd
    /etc/yum.conf
    [root@localhost ~]# ls -ltr files.tar
    -rw-r--r--. 1 root root 10240 Dec 21 23:16 files.tar

To append new files to existing tarball::

    [root@localhost ~]# tar -rvf files.tar /etc/yum/version-groups.conf
    tar: Removing leading `/' from member names
    /etc/yum/version-groups.conf

To list the files::

    [root@localhost ~]# tar -tvf files.tar
    -rw-r--r-- root/root      2325 2022-11-26 10:48 etc/passwd
    -rw-r--r-- root/root       970 2020-10-01 10:03 etc/yum.conf
    -rw-r--r-- root/root       444 2020-10-01 10:03 etc/yum/version-groups.conf


To restore single file::

    [root@localhost ~]# tar -xf files.tar etc/yum.conf
    [root@localhost ~]# ls -ltr etc/yum.conf
    -rw-r--r--. 1 root root 970 Oct  1  2020 etc/yum.conf

To restore all files::

    [root@localhost ~]# tar -xf files.tar
    [root@localhost ~]# tree etc/
    etc/
    ├── passwd
    ├── yum
    │   └── version-groups.conf
    └── yum.conf


Compress a tarball with gzip (`-z`)::

    [root@localhost ~]# tar -czvf /tmp/home.tar.gz /home
    [root@localhost ~]# ls -lrt /tmp/home.tar.gz
    -rw-r--r--. 1 root root 686234 Dec 21 23:34 /tmp/home.tar.gz

Compress a tarball with bzip (`-j`)::

    [root@localhost ~]# ls -lrt /tmp/home.tar.gz2
    -rw-r--r--. 1 root root 545077 Dec 21 23:35 /tmp/home.tar.gz2

To extract the files, use `-x` (gzip or bzip)::

    tar -xf /tmp/home.tar.gz2
    tar -xf /tmp/home.tar.gz


File Linking
=============

Metadata of a file:

    - size, permissions, owner, group, last modified, link count, number of allocated blocks etc.
    - takes 128 bytes for each file.
    - this tiny storage space is called file's **inode** (index node).
    - inode has a unique number used by kernel to access, track and manage the file.
    - to access the inode and the data it points to, a filename is assigned.
    - the **mapping between filename and inode us called a Link**

.. important::
    - **inode**: Tiny storage space with a unique identifier to store metadata of a file.
    - **link**: Mapping between filename and inode.
    - inode **does not store filename** in it's metadata.
    - filename and it's inode number mapping is maintained in the directory's metadata.

- Linking files/directories creates additional instances of the same but **eventually points to the same physical data location**
- Two ways to link in RHEL:

    - Hard Links
    - Soft Links (symlinks)

Hard links
--------------

Mapping between one or more filenames and an inode number.

See both filenames points to same inode::

    [root@localhost ~]# cat > test1.txt
    TEST CONTENT
    [root@localhost ~]# ln test1.txt test2.txt
    [root@localhost ~]# cat test2.txt
    TEST CONTENT

    [root@localhost ~]# ls -li test*
    33803044 -rw-r--r--. 2 root root 13 Dec 22 00:54 test1.txt
    33803044 -rw-r--r--. 2 root root 13 Dec 22 00:54 test2.txt

    [root@localhost ~]# ln test2.txt test3.txt
    [root@localhost ~]# ls -li test*
    33803044 -rw-r--r--. 3 root root 13 Dec 22 00:54 test1.txt
    33803044 -rw-r--r--. 3 root root 13 Dec 22 00:54 test2.txt
    33803044 -rw-r--r--. 3 root root 13 Dec 22 00:54 test3.txt

Note that the link count is set to 3.

Let's delete the original file::

    [root@localhost ~]# rm test1.txt
    rm: remove regular file 'test1.txt'? Y

You still have access to the contents::
    
    [root@localhost ~]# ls -li test*
    33803044 -rw-r--r--. 2 root root 13 Dec 22 00:54 test2.txt
    33803044 -rw-r--r--. 2 root root 13 Dec 22 00:54 test3.txt
    [root@localhost ~]# cat test2.txt
    TEST CONTENT
    [root@localhost ~]# cat test3.txt
    TEST CONTENT

    [root@localhost ~]# ls -li test*
    33803044 -rw-r--r--. 1 root root 13 Dec 22 00:54 test3.txt
    [root@localhost ~]# cat test3.txt
    TEST CONTENT

i.e, all the filenames eventually points to same inode. Means same physical locations.


Soft Link
-----------

- Analogous to that of a shortcut in Microsoft Windows.
- With a soft link, you can access the file directly via the actual filename as well as any shortcuts.
- **Each soft link has a unique inode number** that stores the pathname to the file it is linked with.
- the link count does not increase or decrease.each symlinked file receives a new inode number
  
Soft link is merely a pointer to the file::

    [root@localhost ~]# cat test3.txt
    TEST CONTENT
    [root@localhost ~]# ln -s test3.txt test4.txt
    [root@localhost ~]# ls -li test*
    33803044 -rw-r--r--. 1 root root 13 Dec 22 00:54 test3.txt
    33833469 lrwxrwxrwx. 1 root root  9 Dec 22 01:01 test4.txt -> test3.txt
    [root@localhost ~]# cat test4.txt
    TEST CONTENT

if you remove the actual file, the softlink will stay but pointing to something that does not exists.

::

    [root@localhost ~]# rm test3.txt
    rm: remove regular file ‘test3.txt’? y
    [root@localhost ~]# ls -li test*
    33833469 lrwxrwxrwx. 1 root root 9 Dec 22 01:01 test4.txt -> test3.txt
    [root@localhost ~]# cat test4.txt
    cat: test4.txt: No such file or directory


.. important::
    - **Copy**: Each copy of file will store it's data at unique locations.
    - **link**: All linked files points to same data.


File Permissions
==================

- Users are categorized into 3 classes; **user (u), group (g) and other/public (o)**. There is special class called **all (a)** which represents all these 3 classes combined.
- hyphen character (-): Used if a read, write, or execute permission bit is not desired.
- `---`: no permission.
- `rwx` or `111`: read, write and execute permissions.
- `--x` or `001`: execute permission only.

To add an execute bit for the owner(`u`). Use `-v` to see what changed::

    [root@localhost ~]# chmod u+x newfile -v
    mode of 'newfile' changed from 0644 (rw-r--r--) to 0744 (rwxr--r--)

Add execute permissiont to group, write permissions to others/public ()::

    [root@localhost ~]# chmod g+x newfile -v
    mode of 'newfile' changed from 0744 (rwxr--r--) to 0754 (rwxr-xr--)
    [root@localhost ~]# chmod o+w newfile -v
    mode of 'newfile' changed from 0754 (rwxr-xr--) to 0756 (rwxr-xrw-)

Remove the write permission for public::

    [root@localhost ~]# chmod o-w newfile -v
    mode of 'newfile' changed from 0756 (rwxr-xrw-) to 0754 (rwxr-xr--)

Assign write and execute for all users (note that existing read permission revoked)::

    [root@localhost ~]# ls -lrt newfile
    -rw-r--r--. 1 root root 0 Dec 23 00:26 newfile
    [root@localhost ~]# chmod a=wx newfile -v
    mode of 'newfile' changed from 0644 (rw-r--r--) to 0333 (-wx-wx-wx)
    [root@localhost ~]# chmod a=r newfile -v
    mode of 'newfile' changed from 0333 (-wx-wx-wx) to 0444 (r--r--r--)

To change permissions for multiple groups, use **comma without space**::

    [root@localhost ~]# chmod u+wx,g+w,o-r newfile -v
    mode of ''newfile' changed from 0444 (r--r--r--) to 0760 (rwxrw----)

Default Permissions
--------------------

Linux assigns default permissions to a file or directory at the time
of its creation based on **umask subtracted from predefined permissions**.

**umask (user mask)**: three-digit octal value  that refers to read, write, and execute permissions for owner, group, and public.

    - Default umask value for root: 0022 
    - Default umask value for non-root: 0002

::

    [root@localhost ~]# umask
    0022
    [root@localhost ~]# umask -S
    u=rwx,g=rx,o=rx

**The predefined initial permission** values:

    - for files: 666 (rw-rw-rw-)
    - for directories: 777 (rwxrwxrwx)**

So, initial file permissions will be for normal user: 666-002 = **664**

for root::

    [root@localhost ~]# ls -l test.c
    -rw-r--r--. 1 root root 0 Dec 23 00:43 test.c # 644 (666-022)

Special File Permissions
-------------------------

The bits **suid and sgid bits** are defined on binary executable files to provide non-owners and non-group members the ability to run them with the privileges of the owner or the owning group.

- **setuid/suid** - set user identifier bit.  
- **setgid/sgid** - set group identifier bit. Also, set on shared directories
- **sticky bit** - set on public directories

Switch user (su) should be able run by any user::

    [root@localhost ~]# ls -l /usr/bin/su
    -rwsr-xr-x. 1 root root 32128 Sep 30  2020 /usr/bin/su

The write command allows users to write a message on another logged-in user's terminal.::

    [root@localhost ~]# ls -l /usr/bin/write
    -rwxr-sr-x. 1 root tty 19544 Sep 30  2020 /usr/bin/write

Setup a shared directory
--------------------------

::

    // add 2 users
    [root@localhost ~]# useradd user100
    [root@localhost ~]# useradd user200

    // add a group mygrp with GID 9999. add the users to the group.
    [root@localhost ~]# groupadd -g 9999 mygrp
    [root@localhost ~]# usermod -aG mygrp user100
    [root@localhost ~]# usermod -aG mygrp user200

    // create a directory and make ownership to the group.
    [root@localhost ~]# mkdir /mydir
    [root@localhost ~]# chown root:mygrp /mydir
    [root@localhost ~]# chmod g+s /mydir
    [root@localhost ~]# chmod g+w,o-rx /mydir
    [root@localhost ~]# ls -ld /mydir
    drwxrws---. 2 root mygrp 6 Dec 24 09:02 /mydir

    // Switch to the 2 users and see if they can do cd and create files.
    [root@localhost ~]# su - user100
    [user100@localhost ~]$ cd /mydir/
    [user100@localhost mydir]$ touch file100
    [user100@localhost mydir]$ ls -l file100
    -rw-rw-r--. 1 user100 mygrp 0 Dec 24 09:05 file100
    [user100@localhost mydir]$ exit
    logout
    [root@localhost ~]# su - user200
    [user200@localhost ~]$ cd /mydir/
    [user200@localhost mydir]$ touch file200
    [user200@localhost mydir]$ ls -l file200
    -rw-rw-r--. 1 user200 mygrp 0 Dec 24 09:05 file200

Sticky bit to prevent deletion by accident
--------------------------------------------

The sticky bit is set on public and shared writable directories to protect files and subdirectories owned by normal users from being deleted or moved by other normal users. 

Note the presence of 't' bit::

    [user200@localhost mydir]$ ls -ld /tmp/ /var/tmp/
    drwxrwxrwt. 14 root root 4096 Dec 19 02:11 /var/tmp/
    drwxrwxrwt. 23 root root 4096 Dec 24 09:11 /tmp/


Effect of sticky bit::

    [root@localhost ~]# su - user100
    Last login: Sat Dec 24 09:04:39 PST 2022 on pts/2
    [user100@localhost ~]$ cd /tmp/
    [user100@localhost tmp]$ rm stickyfile
    rm: remove write-protected regular empty file ‘stickyfile’? y
    rm: cannot remove ‘stickyfile’: Operation not permitted

.. important::
    - With the argument **+1000**, the chmod command sets the sticky bit on the specified directory without altering any existing underlying permissions.
    - `chmod -v +1000 /tmp`

::

    [root@localhost ~]# chmod o-t /tmp/ -v
    mode of '/tmp/' changed from 1777 (rwxrwxrwt) to 0777 (rwxrwxrwx)
    [root@localhost ~]# chmod +1000 /tmp/ -v
    mode of '/tmp/' changed from 0777 (rwxrwxrwx) to 1777 (rwxrwxrwt)

File Searching
================

find command
--------------

Syntax: **find <path> <search by> <action>**

**Search by name** (`-print` is default and optional)::

    [root@localhost ~]# find . -name anaconda-ks* -print  # search current directory
    ./anaconda-ks.cfg
    ./work/anaconda-ks.cfg

    [root@localhost ~]# find ~ -name .changed
    /root/home/dev-machine/.local/share/flatpak/.changed  # search home directory


    [root@localhost ~]# find /dev -name sd*
    /dev/sda3
    /dev/sda2
    /dev/sda1
    /dev/sda

**Search by name (case-insensitive)**::

    [root@localhost ~]# find . -iname myfile*
    ./myfile
    ./MyFile
    [root@localhost ~]# find . -name myfile*
    ./myfile

**Search by size**::

    [root@localhost ~]# ls -lh
    total 11G
    -rw-------. 1 root root 2.8K Nov 26 10:48 anaconda-ks.cfg
    drwxr-xr-x. 3 root root   47 Dec 21 23:20 etc
    -rw-r--r--. 1 root root  10K Dec 21 23:17 files.tar
    -rw-r--r--. 1 root root  10G Dec 24 18:37 gentoo_root.img
    drwxr-xr-x. 3 root root   25 Nov 26 10:48 home
    -rw-r--r--. 1 root root    0 Dec 24 18:28 MyFile
    -rw-------. 1 root root 2.1K Nov 26 10:48 original-ks.cfg
    drwxr-xr-x. 4 root root   60 Dec 19 02:28 work


find files of size 10G::

    [root@localhost ~]# find . -size 10G 
    ./gentoo_root.img

find files smaller than 1kb::

    [root@localhost ~]# find ./work/ -size -1k
    ./work/project01/README.md
    ./work/project01/licence
    ./work/.cache/abrt/lastnotification

find files bigger than 9GB::

    [root@localhost ~]# find . -size +9G 
    ./gentoo_root.img

To provide maxdepth (use `mindepth` to do the otherway)::

    [root@localhost ~]# find . -maxdepth 1 -name anaco*
    ./anaconda-ks.cfg
    [root@localhost ~]# find . -maxdepth 2 -name anaco*
    ./anaconda-ks.cfg
    ./work/anaconda-ks.cfg

Search by **time modified**

find files in the /etc directory that were modified last day::

    [root@localhost ~]# find /tmp  -mtime -1
    /tmp
    /tmp/stickyfile
    /tmp/newest

find files modified 2000 days ago::

    [root@localhost ~]# find /tmp  -mtime +2000

files modified in the past 10 mins::

    [root@localhost ~]# find /tmp  -mmin -10
    /tmp
    /tmp/newest

**Search by type**::

    [root@localhost ~]# find /dev -type b  # BLOCK DEVICES
    /dev/sr0
    /dev/sda3
    /dev/sda2
    /dev/sda1
    /dev/sda

    [root@localhost ~]# find /dev -type c -perm 222 # CHARECTER DEVICES WITH PERMISSIONS SET 222

find with exec and ok
----------------------

List files as they discovered::

    [root@localhost ~]# find . -name anaconda-ks* -exec ls -l {} \;
    -rw-------. 1 root root 2789 Nov 26 10:48 ./anaconda-ks.cfg
    -rw-------. 1 root root 2789 Dec 19 02:28 ./work/anaconda-ks.cfg

To prompt for confirmation before doing exec, use ok::

    [root@localhost ~]# find . -name anaconda-ks* -ok ls -l {} \;
    < ls ... ./anaconda-ks.cfg > ? y
    -rw-------. 1 root root 2789 Nov 26 10:48 ./anaconda-ks.cfg
    < ls ... ./work/anaconda-ks.cfg > ? n

Copy files to /tmp as they found::

    [root@localhost ~]# find . -name 'foo*' -ok cp {} /tmp \;
    < cp ... ./foo200 > ? y
    < cp ... ./foo100 > ? y
    [root@localhost ~]# ls -ltr /tmp/foo*
    -rw-r--r--. 1 root root 11 Dec 24 19:29 /tmp/foo200
    -rw-r--r--. 1 root root 14 Dec 24 19:29 /tmp/foo100


Locate command
----------------

Unlike find which perform search everytime you run it, locate will search only the **/var/lib/mlocate/mlocate.db**.

The database **/var/lib/mlocate/mlocate.db** is auto-updated daily.

::

    [root@localhost ~]# locate -S
    Database /var/lib/mlocate/mlocate.db:
            13,892 directories
            152,878 files
            7,677,475 bytes in file names
            3,510,381 bytes used to store database
    [root@localhost ~]# locate -n3 .sh
    /boot/grub2/i386-pc/modinfo.sh
    /etc/X11/xinit/xinitrc.d/00-start-message-bus.sh
    /etc/X11/xinit/xinitrc.d/10-qt5-check-opengl2.sh


ACL Management
================

::

    [root@localhost ~]# cd /tmp/
    [root@localhost tmp]# touch aclfile01
    [root@localhost tmp]# getfacl aclfile01
    # file: aclfile01
    # owner: root
    # group: root
    user::rw-
    group::r--
    other::r--
    [root@localhost tmp]# ls -l aclfile01
    -rw-r--r--. 1 root root 0 Dec 25 19:33 aclfile01


The **setfacl** command is used to apply, modify, or remove ACL settings.

**Mask value**: Maximum allowable permissions placed for a named user or group on a file or directory.