# RAID/LVM/iSCSI
2 things are important in the server:
- The data needs to be stored somewhere
- It is supposed to be running multiple virtual servers

RAID - multiple hard disks (good for redundancy)
LVM - group storage devices/arrays (provides flexibility)
iSCSI - make block devices available over a network (to create a SAN)

## RAID
RAID  = Redundant Array of Independent Disks

You can just use your disks one by one, while they fill (Just a Bunch of Disks JBOD)

RAID 0 - it will distribute files between multiple disks. (so you have like 1 disk, logical, but there are more than one, the blocks of data itself)
- Capacity increases with number of disks
- NO redundancy

RAID 1 - duplicates data over disks
- Protected from disk failure
- 2 disks = 1 disks capacity, because it uses the second one as backup

RAID 5 - sacrifice the capacity of one drive, to store parity information in favor of redundancy
- Possible with 3+ drives
- Parity is spread over all disks
- 2 TB = 1 TB
- Single disk redundancy - one disk may fail, but as soon as 2 fail - data is lost.
- It is not possible to expand a RAID 5 array. That is why LVM is better

RAID 10 - Mirroring + striping
- combination of RAID 0 (mirroring) + RAID 1 (striping)
- Only possible with 4 drives or more
- Capacity is half of the 4 drives capacity
- Single or double disk redundancy - any disk may fail and possibly a second

### Software vs Hardware RAID
Difference: Where are the RAID calculations taking place?
- Hardware: dedicated RAID Chip
- Software: shared processor 

If working with DAS systems: hardware RAID has not much use!
- Main CPU is more than strong enough for added RAID functionality

RAID is not a backup!
Purpose of RAID is to make data available and system uptime, not data recovery like with backup
Protect against disk or other hardware failures, data loss in case of accidental things

3-2-1 rule:
- 3 copies of data
- 2 different media
- 1 at a different location

## LVM
LVM - Logical Volume Manager is a technology to "carve" disks, RAID sets and volumes into new "devices"

It has 3 layers:
- PV Physical Volume - partitions created
- VG Volume Groups - PVs can be grouped into one or more VGs
- LV Logical Volumes - a VG can be again divided into one or more LVs

It is super flexible, and looks similar to RAID 0

## iSCSI
It is used to connect remotely to disks, via the network.