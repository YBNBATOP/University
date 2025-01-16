# Lecture 1
TCO - Total Cost of ownerwhip
ROI - what profit will the investment give me (Return of Investment)
RPO - Recovery Point Objective - what data are you allowed to lose
RTO - what time its takes to recover from disaster.
HA - High Avaialability
DR - Disaster Recovery
HA-DR-RTO-RPO
RAS - Reliability, Availability, Serviceability


Types of Storage:
- DAS - hardware to PC (connected via SCSI and reads with Block I/O so it is direct connection) (Direct Attached Storage)
- NAS - Network area storage (it reads by File I/O) (Network Attached Storage)
- SAN - can be fiber or SCSI, is reading by the Block I/O. (Storage Area Network) - this will usually have some type of software that will translate the Block I/Os to other PCs

Hyperconverged - you use the same cluster to store and compute on one unit.
Then you have stuff yourself and cloud (Hybrid Cloud)
And then full cloud (Multi Cloud).

AVG Latency - time it gets data to get from head to controller.

Cloud storage is usually a combination of types of connections.

iSCSI Target - the one to connect to
iSCSI Initiator - the one that connects to the target.

In iSCSI you have 16 addresses, and address 7 is reserved for controller.

PCIe works in a BUS, so it scales to the slower working thing.

# Lecture 2
RAID, LVM (this is Linux specific), iSCSI (used to translate Block to File)

JBOD - Just a bunch of disk, just of storage.

RAID0 - splitting data to every disk you have
RAID1 - this is redundancy (you get half the space of the disk), and it creates a copy of your disk.
RAID01 - pretty much same principle. (stripping + mirror)
RAID10 - mirror + stripping
RAID5 - this is parity, with at least 3 disks, and you have backup in this case.

You can have hardware RAID (from a special part of motherboard), and software RAID (sharing some CPUs)

RAID is not a backup!
You should apply rule 3-2-1

LVM - Logical Volume Manager.
Very useful, as you can expand the "RAID".
It has 3 layers:
- PV (Physical Volume) - initial connection
- VG (Volume Group) - total space
- LV (Logical Volume) - "partition"

iSCSI - used in SAN. Works in a Block I/O.
You can use Fiber or another cable.
Fibre Channel requires hardware and software.
iSCSI is a problem, when you have a lot of users to connect to one.

In Windows we have Virtual Hard Drives (VHD and VHDx). Similar to our virtualization hard drives for VMware.
VHDx is the newer one, and goes higher than 2TB, and can be dynamically expanding. You have normal state (takes all space created) and dynamically expanding so takes as much as it has to.

Data deduplication will save the same parts, that are in various files.
ReFS (Resilient File System) is good for failure prevention, and its overall more secure.

Storage Spaces - software RAID on Windows.
First you create Storage Pool (like physical disks), then Storage Spaces (like volume group) that then can be formatted and used.
Storage Spaces are actually Virtual Disks.
Storage Spaces Direct (S2D) - having multiple connected storage spaces into one place.

iSCSI Target
LUN - can be part of multiple targets, and multiple LUNs can be part of a single target.

# Lecture 3

There is 2 types of virtualization:
![[Pasted image 20250109131832.png]]
Type 2 - Hosted, when you need a host to run.
Type 1 - VMware ESXi, Hyper-V, all that works on bare metal.

Virtualization is more about isolation, they do not know about each other.

.vmdk - storage
.nvram - firmware of the VM
.vmx - config file.
.mem - saves the memory state

VMware Virtualization is ESXi and is Type 1 - meaning bare-metal.
This is not supported by every CPU out there.
You can over provision amount of CPU to VMs.
Networking in Type 1 is done with virtual switches.
VMFS - solves the problem of SAN.
vSphere - management layer

vSwitches have 2 sides - virtual port groups, and uplinks
# Lecture 4
Remote Server Administration Tools (RSAT) for management.
Datacenter Windows has unlimited Hyper-V VMs

Hyper-V has VMs which are called (child) partitions.
The Host is called root partition.
Enlightened partition are those that understand that they are VMs and have custom things.
VMs are called child partitions.

# Lecture 6
Open-source can be GPL and MIT+Apache
In first case you have to share the code that you used (Copy-Left), in the other you do not need to (Permissive).

In Open-source you have KVM for virtualization (Kernel-Based Virtual Machines)
Q-EMU Quick Emulator - is for emulation, and translating instructions. It also provides a nice **libvirt** library for other usefulness and functions.

# Lecture 7
Containers are not virtual machines, they are just processes.
It is OS-Level virtualization
Dockerfile - specifies the images themselves, like what you will do
Docker compose - create a whole environment at the same time
runc and containerd is what docker uses under the hood. This makes it run basically, because this are daemons
- docker -> dockerd -> containerd -> runc
OCI - Open Container Initiative - just a framework for generalisation

Podman is deamonless, so does not need root privileges.
It even uses the same registries

LXD and LXC and Incus is made for OS, and not just applications

LXC is the old, LXD is the new one.
LXC is a lightweight VM of an image.
It is very similar to a virtualization engine, but it creates containers.
Incus was created as the newest one due to licensing issues.

# Lecture 7
Kubernetes was created to automate a lot of things. 
It can be imperative (tell to do something via CLI), or declarative (ask via a config file)
You have nodes, or computers; you connect them to clusters; and then you create pods (container + config)
Kubernetes has some things to remember:
- yaml files - they create some instances of 