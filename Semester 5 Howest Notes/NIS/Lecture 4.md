Right now (Lab 01) we have all the devices in the same network.
The next step is to have a layer 2 network, but split it in various **subnets**.

**NOTE**: In Lab 2 you loose connection to the firewall, and you probably loose connection between networks.

Then we are going to split everything into VLANs and have everything connected to the firewall.

# Routers

# Network Address and Port Translation (NAPT)
Sometimes called PAT
NAT44 is most recent common name

Usually from private (RFC1918) IPv4 to public IPv4
Includes translation of ports
NAT Table includes:
- Internal IP address
- Internal source port number of requests
- External IP address
- External port address

# Sockets
A socket is a combination of port and IP address.

At any point in time only ONE application can use
- A certain IP address
- in combination with a protocol number (6 for TCP, 17 for UDP,...)
- and a certain port number for that protocol
- a socket identifies an application
- Notation: 192.168.12.12:8080 (IPv4) + [2001:db8:0:0::1]:8080

# TCP/UDP Header calculation

# Port Forwarding
Port Forwarding is a simplified version of NAPT, since you are using the same port number, but different IP address.

# Firewall rules
Note that rules for firewalling matter with the order

For Labs - make sure that you have snapshots of the firewall! and others as well
