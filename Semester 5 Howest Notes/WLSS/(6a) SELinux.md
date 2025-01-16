SELinux = Security-Enhanced Linux
It is not a different distro, it just a feature.
RedHat has it by default. In RedHat packages cannot always work after they are installed.

It implements **Mandatroy Access Control**. It is a labeling system, everything just gets another label, an additional one, which needs to be verified. It creates another level of protection, so in case of everything going down - you get less fucked. It was originally developed by NSA.

# DAC (Discretionary Access Control)
In linux by default we have rwx controls. Owner can do anything with files and folders.

Administrators have no way to control users. Processes can also make some changes to files and etc.

# MAC (Mandatory Access Control)
Additionally added on top of DAC with SELinux
More fine-grained Enhanced Linux

All of this things is a general concept, and SELinux is like a part of it.
It also has other functions like:
- apparmor

# SELinux
LSM (Linux Security Module) - is the way the things are plugged into the system itself.
## Possible states
**Disabled** - SELinux turned off, not enabled in the kernel or disabled via kernel parameters
**Permissive** - SELinux turned on, objects are labeled. Just logs denials but does not enforce them -> **what-if** mode
**Enforcing** - SELinux turned on, objects are labeled, logs and enforces denials for all enforcing domains (processes)

**Per-domain Permissive** - it can be enforced for some processes, and permissive for others.

You can change the states of the things, with **setenforce** for example, and check it with **getenforce**.
You can also set the selinux state on boot, with GRUB, or **/etc/selinux/config**.

## Labeling
Each process gets a kind of labeling.'
The labels can be checked by doing **ls -lZ** for example.
**id -Z** will also have a security context.
**-Z** is pretty much having the label show function.

It has 4 things:
- user_u:role_r:type_t:level
## Policy
With various policies, it can be told towards processes that they can not change or talk to other processes, or do something else.

With policies you can restrict access to a file from a webserver for example, which runs on the Apache server in that case. Confinement is one of the most interesting things wiht SELinux. This can also be called targeted policy. This targets only high-risk daemons.

Each user is mapped to an SELinux user, and has like a separate level of rules. Confined users (SELinux users) are something different, and can have various roles.

