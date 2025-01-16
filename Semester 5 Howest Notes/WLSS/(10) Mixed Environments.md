We use WSL sometimes, just because it is easier to find/use things overall.
WSL can have 2 versions, nowadays used WSL 2, which does not use a lightweight VM and just transforms system calls overall.

`hcsdiag list` will show the small VM that runs behind the scenes.
Windows and "Linux VM" Kernels are on the same level with WSL.
If you have different versions of Linux machines running, like Kali + Ubuntu, then within the Linux kernel, you will have the same types of machines, but booting at different times.

You can call windows commands from within WSL. The thing is, that C drive is also mounted, as Protocol P9 into the WSL machines.

In terminal, you can go to a directory and start `wsl` in there.

WSL also has other settings that can be set. It also stores all the settings on our machines, as well as the .vhdx files all the way.
There is also a file share with `\\wsl$` (With Windows + R)
WSL also has Xforwarding
It is also possible to have a full blown RPC to the Kali, running in WSL, called KeX. 

Docker Desktop uses WSL2 for Linux Containers

Powershell 7 has more features, because starting with Powershell 5or6 they had DotNet core implementations.

Powershell 7 can also be installed on Linux, because it is cross-platform. This can be useful for something like Ansible. This way, you can go to a VM, and from there in powershell, connect to another Windows machine o_0

Nowadays the normal version is 5.1 or something, and powershell 7 can be installed along side with powershell 5.1
Check version - `echo $PSversiontable`

There is also another lab, about Samba, and not SMB (like in Windows with `\\` accessing of file shares)
Linux can even join an Active Directory, and can be even used as a DC. o-0
This is the newest version like v4

# Exam Info
Same as DCV and Forensics.
Also can make a survey for additional forms (bonus point)
About 40 questions.

