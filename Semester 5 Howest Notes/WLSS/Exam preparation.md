# Lecture 1
Know the difference between different Linux distributions

pfSense can be used for the multiple management settings

To set the IP addresses:
- ifupdown (/etc/network/interfaces)
- systemd-networkd
- nmtui
- nmcli
# Lecture 2
Shells - translate the commands from the command line to "computer language"
SSH connections are connected as **pts/0** and can be seen like `who` command.
The virtual terminals in linux - **tty** - can be changed with ALT+F#

$( ) - used to get the output of the command
$(( )) - used for calculations in shell
You have stderr (`#2`) and stdout (`#1`)
By default for piping the stdout is being piped
`>` - overwrite file
`>>` - append to file
`<` - use file as input for command (read from file)
`2>` - redirect errors
`2>&1` - redirect errors to standard output
`2>&1 > /dev/null` - redirect stdout to /dev/null and redirect stderr to stdout
Basically reading from right to left might help

To check the shell:
- `echo $SHELL`
- `echo $0`
- `ps -p $$`

`rbash` is restricted `bash -r`
Things can be changed in /etc/passwd, like the default shell

If you have /etc/nologin, it will disallow login if not **root**
To restrict any shells, you set it to **/usr/bin/nologin** (in /etc/passwd)

SSH Port Forwarding:
- file for ssh client - **/etc/ssh/ssh_client**
- file for ssh server - **/etc/ssh/sshd_config**
- Local - `ssh -L localport:remotehost:remoteport user@ip` (Local to Remote)
- Remote - `ssh -R remoteport:localhost:localport user@ip` (Remote to local - Browse to `remoteport`)
# Lecture 3
We can change anything in systemd with `systemctl`

BIOS -> MBR -> BootLoader -> Kernel -> Systemd -> Targets

sysctl != systemctl
sysctl - is meant for kernel

systemd unit configuration files are set in **/lib/systemd/systemd/servicename**
When something is executed, it looks then for the configuration file, like **/etc/ssh/sshd_config**

Parts for config files:
`[Unit]`
- After - what to do after
- Before - what is needed before
- **WantedBy** - which other process needs it. This creates system links, and for example B service might need service A and create a link that it wants service A in the config files.
![[Systemctl enable.png]]
- Wants - ask for something but not mandatory
- Requires - mandatory thing I need
- Requisite - I need a service to be running
- Conflicts - another service I can not run along with
![[Systemd config paths.png]]

![[nftables config files path.png]]
# Lecture 4
You can have network and application firewalls
Network - usually regarded as WAF, on gateways and etc
Application - on a single host, next generation often MAC, services like netfilter and iptables. **netfilter** is a kernel module, **iptables** allows to talk to it.
![[Linux application firewalling.png]]
`iptables`:
- It has **Filter tables**, with **chains** like Input and Output, and then you have rules inside.
- ![[IPTables Routing.png]]
There are different tables:
- Raw
- Mangle
- Nat
- Filter
- Security
![[Tables.png]]
![[Table decisions.png]]
Chain names are in capital, and table names are in lower

`nftables`
- a better version of itables
- same approach
- more convenient
- one tool for multiple tables
- added another hook (routing decision) which is called **ingress** allowing you to see everything before prerouting.
- It adds a priority, which specifies the value of different hooks. Value 1 is more important than 5. The default values are the same as the iptables
- has /etc/nftables.conf which can be loaded by default with systemd.

There are tools above the firewall things themselves.
You have firewalld - a service - firewall-cmd and firewall-config for CLI and GUI configuration.

TCP Wrappers is next layer of security, and can use /etc/hosts.allow and /hosts.deny
It is daemon-less.
**hosts.deny** works on application/process level.
**iptables** is kernel level

IPAddressList can be specified in the Systemd processes and specifies whether something is allowed or not, to be processed.
# Lecture 5
NSS - a thing that verifies various things for authentication for example.
NSS specifies where to find various things responsible for different actions. It specifies where to look for users, or groups that exit
The configuration file is **/etc/nsswitch.conf**

PAM is the second thing, which already decides how to use the information from NSS.
PAM has various modules that can be used. (**/usr/lib/x86_64-linux-gny/security/**, and have .so extension which means its a module)
PAM configuration files are stored in **/etc/pam.d/**. It has files for authentication and denial.
PAM has other control flags, that specify whether you are allowed to do something if a thing works or not
The structure is type, control flag, module
example: auth sufficien pam_rootok.so:
- required - a MUST succeed for authentication to succeed
- requisite - if one part fails, then everything fails
- sufficient - immediate success if the module is successful
- optional - this does not impact the success or failure
You always have to end with **pam_deny.so**
PAM modules have configuration files in **/etc/security**
# Lecture 6
SELinux is another enhancement for Linux
It uses MAC - Mandatory Access Control

SELinux gives a label to any object (file, folder, etc.)
DAC vs MAC:
- MAC is more strict that allows you to disallow more things
It is all already a Linux Security Module (LSM) and you can see **selinuxfs** mounted if you are using the SELinux
SELinux by default really wants to deny access for you
It also has 3 stages:
- Disabled - turned off
- Permissive - logs things, has labelling, turned on overall
- Enforcing - fully working, and denials based on the settings
All of this can be also configured for specific domains/partitions.
You can `getenforce` and `sestatus` and then you have various things.
Labelling (check with -Z) is meant to show SELinux labelling. 
You can have different Policies like **/etc/linux/config** and then have 
You can have mappings for restricted users and have explicit SELinux policies.

AppArmor is MAC, quite the same, but AppArmor does not have labelling and pseudo-filesystem.
It can be bypassed
There are 3 stages:
- Disabled / unconfined - turned off
- Complain mode (Permissive) - turned on, log denials
- Enforce mode

# Lecture 8
You need Windows Auditing for various logs
You have groups of policies. Then inside you have security policies, as a subclass.
Security policies can be edited with `secpol.msc` or `gpedit.msc`
Security policies are ran by `lsass.exe` by System32
Audit policies are a subset of security policies.
![[Subsets of policies.png]]

Local audit policies are not many, basically allows to log failure or success, and nothing special.
Then you have Advanced Audit Policies, where you have subpolicies for everything.
For subcategories to work, you need to enable it in other policies.

You can apply security policies for domain objects.

What to audit?
- Information useful for me, like successful logins

Event Viewer is the thing where you see various logs. You have different types like Applications, Security, and etc.
Logs are not automatically refreshed
![[Log types.png]]
You have 4 types:
- Warning
- Error
- Success
- Failure

You can install Sysmon to make the logging easier.

File access auditing works also for files and folders and what not, which setting for the security of those files.
You can also go for Global Object Access Auditing (GOAA)

# Lecture 9
WSUS (Windows Server Update Service) is meant to provide updates for machines, and it makes it more flexible to show what happens, and what is installed.

You have different types of updates:
- Critical updates
- Security updates
- Updates
- Definition updates
- Drivers
- Feature packs and etc.
- Upgrades

UEFI > BIOS (Basic Input Output System)
UEFI allows you to have more security for booting, like trusted boot
TPM modules allow you to store various keys like for VM encryptions.
UEFI uses GPT.
Only Linux can use BIOS with GPT.
ESP stands for EFI System Partition

Compatibility mode is CSM and you need it to run BIOS compatible things.

Bitlocker allows to encrypt data at rest.
Windows generates 2 keys, and stores 1 key. Another key is stored on anything else which is not encrypted. Additional authentication is possible.
Bitlocker keys can be also stored on the domain controller.
Bitlocker will go into rescue mode once something happens.
# Lecture 10
You have WSL 1 and 2, where 1 is storing things on your machine, and 2 is a lightweight VM.
To enable it you need Hyper-V and another feature.
WSL2 is used by docker as well

PowerShell can be installed, and you have Core version and is deprecated, now it is Windows PowerShell.
The version currently on Win 11 is like version 5. PowerShell 7 is the newest one.
PowerShell Core it is 6+, Windows PowerShell is usually 5~. If it is called Core, then it is an old one.
You can install and access powershell via `pwsh`.
You can also use PowerShell remote sessions to Windows machines.
-HostName and -UserName in case of Linux

We use Samba to have authentication with Active Directory





