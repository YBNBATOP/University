Ethernet is considered Layer 2 from OSI
On Layer 3 we have packets, on Layer 2 we have frames, Layer 4 its frames. For Layer 3 we have IP protocol
One of the reason to learn OSI model:
- Troubleshooting
- Security (if you know what goes where, then you can easily secure it)

Class A - starts with 0-127 (0)
Class B - starts with (10)
Class C - starts with (110)
Class D - (1110)
Class E - (1111)

To know that a device is looking for a multicast packet, then it will first send an "question" to the router, and then the switch will also know that the device wants to hear the multicast

This is also related to IGMP Snooping

DNS - Domain Name System, transforms a **domain name** to an address. It can be both A and AAAA address. A is for IPv4, and the other one is IPv6 AAAA. IPv6 is usually faster, BECAUSE - 
For NAT you need recalculation for the IP Header, also for the UDP/TCP

Routing table keeps track of routes, subnets and everything from Within the network. Layer 2 connects different nodes (devices in the network)

Every device has an ARP table, used to find IP addresses linked to the MAC address.

ARP is a broadcast on the network, and asks for the MAC address for the IP addresses. The devices reply with Unicast.

Switch has ARP cache, but does not use it.

Layer 2 is the most important layer.

Everything is done with standards, and until layer 2 is IEEE, and then it is IETF

VLANs were the first virtualizations.\
VLAN encapsulation is done with the 802.1q tag.

