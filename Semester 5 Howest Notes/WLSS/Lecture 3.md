# Systemd
## Systemd basics
systemd runs  as a process with PID 1 as "/sbin/init"
Configuration for it is simpler and more logical
It is easy to set the permission and resource limits for each service
systemd can monitor services and restart them if needed (watch dog)
**systemctl** command to manipulate the services
systemctl (manages systemd) != sysctl (reads and modifies the attributes of the system kernel)

Systemd has units, and hence can list and run them and have other features
Systemd units can be services, targets, and other options as well.
You can even view  the configuration of systemd services via `systemctl cat sshd` for example.
This configurations are different from something like sshd, which has like a .config folder or something similar. So overall you just want to customize the daemon, and a separate one to fit it to work with the systemd.

Systemd also has functionalities to show the requirements for each process as well, dependencies and other stuff like that
## Linux initialization
Previously - there was a separate **init** with lots of small "scripts" to start the system, so not enough concurency!
Now - there is systemd with "units", but deviates from the Linux philosophy, therefore it is criticized (SOYSTEM D)

