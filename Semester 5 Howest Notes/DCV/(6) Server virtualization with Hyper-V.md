# Windows management vision
They like to have GUI administrated servers, however right now, in the nearest feature they are transitioning.
## CLI Options
WinRM is what Windows can also be managed with (Windows Remote Management). Every server installation of Windows have it open by default.
For remote CLI you only need to setup your client.
# Windows Server versions
Standard edition vs Datacenter edition
Main difference: datacenter allows more Hyper-V VMs, and other differences like storage spaces direct.
## ESXi vs Hyper-V
ESXi - more monolithic, as it has separation of VMs and etc
Hyper-V - VMs can talk between each other.
### Hyper-V
The VMs are called partitions.
First VM, or main (Windows on the laptop) is the **Root Partitions**
VMs are called child partitions
Partitions that know they are running with special drivers and virtually - are called "enlightened" partitions

To install Hyper-V you just need to install Hyper-V. By installing it, you detach your windows from the hardware, so it is not really managed by it, but by a whole fucking hypervisor.

Hyper-V machines can be managed by:
- Hyper-V Management GUI client
- PowerShell
- Windows Admin Center

In the lab, we will have a lab to create similar to ESXi, but with Hyper-V.