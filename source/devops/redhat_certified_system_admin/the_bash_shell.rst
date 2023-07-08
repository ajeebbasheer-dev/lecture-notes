================
The Bash Shell
================

- The Bourne-Again Shell
- RHEL supports a variety of shells of which the bash shell is the most common. It is also the default shell for users in RHEL 8.
- interface between a user and the Linux kernel.
- bash shell is identified by
    
    - Dollar sign ($) for normal users.
    - Hash sign (#) for the root user

- The bash shell is resident in the /usr/bin/bash.

Internal and External Shell Commands
======================================

- Internal commands: built-in commands that are executed directly by the shell **without spawning a process**.

    - Examples: cd, pwd, umask, alias/unalias, history, command, . (dot), export, exit, test, shift, set/unset, source, exec, and break

- External commands:  located in various directories, such as /usr/bin and /usr/sbin

    - the bash shell **spawns a temporary sub-shell (child shell) to run them**.

Environment Variables
=======================

- must be enclosed within quotation marks (“”).
- local variables (shell variables) are private to the shell. its value cannot be used by programs that are not started in that shell.
- The value of an environment variable is inherited from the current shell to the sub-shell during the execution of a program. variable is accessible to the program, as well as any subprograms that it spawns during its lifecycle. 

Predefined environment variables::

    [root@localhost ~]# echo $DISPLAY
    localhost:10.0
    [root@localhost ~]# echo $HISTFILE
    /root/.bash_history
    [root@localhost ~]# echo $HISTSIZE
    1000
    [root@localhost ~]# echo $PS1   # Defines the primary command prompt
    [\u@\h \W]\$
    [root@localhost ~]# echo $PS2
    >

Setting and Unsetting Variables
--------------------------------

To define a local variable called VR1::

    [root@localhost ~]# VAR1 = "FIS"
    bash: VAR1: command not found...
    [root@localhost ~]# VAR1="FIS"
    [root@localhost ~]# echo $VAR1
    FIS


To make this variable an environment variable::

    [root@localhost ~]# export VAR1

To undefine this variable and remove it from the shell environment::

    [root@localhost ~]# unset VAR1
    [root@localhost ~]# echo $VAR1

Input, Output, and Error Redirections
=======================================

- Default behavior: Programs read input from the keyboard and write output and errors (if any) to the terminal window where they are initiated.
- The bash handles input, output, and errors as character streams.
- (<) for stdin, (>) for stdout and stderr. 
- Can also use file descriptors  0, 1, and 2.

::

    [root@localhost ~]# cat /etc/redhat-release
    CentOS Linux release 7.9.2009 (Core)

- **/dev/null** is a special file that is used to discard data

To discard all errors, use `2> /dev/null`::

    [root@localhost ~]# find / -name core -print 2> /dev/null

