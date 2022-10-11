========
Windows
========

Adding git in Windows
======================

Install git from `Official Website<https://git-scm.com/download/win>_`


Make sure `C:\Program Files\Git\cmd` is there in the PATH.

Type `SET` in cmd to see all env variables. 

In Powershell use `Get-ChildItem Env:` too the env variables. However, if the PATH is long, it may show only first few characters.

Adding aliases to Windows
===========================

Below commands will not work in Powershell.

Create a file::

    C:\Users\ajeeb> code init.cmd

Add this to registry::

    C:\Users\ajeeb>reg add "HKCU\Software\Microsoft\Command Processor" /v AutoRun /t REG_EXPAND_SZ /d "%"USERPROFILE"%\init.cmd" /f
    The operation completed successfully.

To Unregister::

    C:\Users\ajeeb\OneDrive\dev\sphinx-doc>reg delete "HKCU\Software\Microsoft\Command Processor" /v AutoRun
    Delete the registry value AutoRun (Yes/No)? Yes
    The operation completed successfully.
