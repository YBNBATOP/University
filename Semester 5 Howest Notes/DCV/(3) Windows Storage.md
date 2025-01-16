# Windows Storage
## SAN Environment (Windows)
Windows does things a bit differently
Today:
- VHD (Virtual Hard Drives)
- Storage spaces (flexibility + redundancy + deduplication of data)

**SAN** = Storage Area Network and it presents the storage as Block IO (as in it appears as a connected USD for example, but it is just away from you)
**iSCSI**= a solution to make block devices accessible over a network. Same as SAN.

## Virtual Hard Drive
In Disk Management you can create Action > Create VHD. This can come in different factors.
Initializing a disk = create a partition table on the disk. Then you can create volumes.
VHD/VHDX is the same principle of disks as the VMware for example. In that case it can be even expanded (VHDX). It is essentially the same thing is regular hard drives.
## Data deduplication
Data deduplication detects two identical clusters, it will keep the original but free the copy.
It works like moving things to other places, and then you have the similar places.

It can work for:
- NTFS (keeps track of data via the MFT)
- ReFS (via block cloning) - it is more efficient than NTFS

## Storage spaces
This is similar to LVM in some way. Moreover you can create **Storage Pools** through some Windows shenanigans.

It allows to create redundancy, and it is similar to RAID systems. You can make also mirrors and use VHDs.

After you make a storage space, it may use your virtual disks and also physical.

### Storage spaces Direct
Instead of having 1 storage space for every server, you may have like one multiple pool for everyone.

Hyperconverged = server with own storage attached directly.

### Storage Replica
Synchronization of data, but not a backup solution.  It is also done via SMB.

## iSCSI Target Server
You can make things similar to the Synology SAN, as you can make the server a whole target. That will allow to mount, for example, storage spaces/pools on your PC over the network.