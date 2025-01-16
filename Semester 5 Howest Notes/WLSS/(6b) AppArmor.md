AppArmor, same as SELinux, is just an implementation of MAC -> [[(6a) SELinux]]
It works based on policy files and pathnames.
It works with policy files, without labeling. 
It also have states:
- Disabled/unconfined
- Complain mode (Permissive)
- Enforce mode - Turned on

To make a change for a binary, there should be something done with regard to the **/etc/apparmor.d**. 

For example for **tcpdump**, you would create a file in **/etc/apparmor.d/usr.bin.tcpdump** and specify things in there.
with **aa-status** it can be seen which processes are in enforce mode.
Additional restrictions can be also made, as then you might restrict the output being saved as certain format.
AppArmor is built to protect well-known processes.
