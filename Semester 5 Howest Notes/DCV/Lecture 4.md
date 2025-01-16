# Server virtualization with VMware
We want to use virtualization to use the resources of our server.
VMs are just a bunch of files and it makes it easier to move it around.

## Virtualization
In case of hardware failure, the VMs can be moved to another place

# Kinds of virtualization
- Bare metal (Type 1)
- Hosted (Type 2)
- Containers (docker)
- desktop, application, data, device... virtualization

Hosted virtualization:
- VMware
- Virtualbox

Bare-metal:
- VMware ESXI
- Hyper-V
- Citrix XenServer
- KVM

## What is a VM?
VM is just a bunch of files.

.vmdk - are files regarding the storage itself
.vmx - are files that contain information with configuration for the machine
.nvram - is nonvolatile (stays after reboot), and it contains the BIOS information\
.vmem - virtual memory and is present while the vm is running

# VMware server virtualization
VM Esxi allows you to use bare-metal virtualization and run multiple VMs on one computer. It can also be used as a computer to connect as a server to. You can do it via VMware as well.

# Central VMware virtualization
VMware vSphere Suite - this thing can have various editions and have different software inside of itself.
vCenter Server can be viewed as a kind of Kubernetes to manage all possible "containers" (or VM in this case)

This all is just needed to minimize the possible downtime so that the VMs can be migrated to various servers between themselves.

