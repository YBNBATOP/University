# Linux Firewalling
## Different firewalls for Linux
A firewall is something that is supposed to stop the "fire" from spreading. You want network traffic to be ruled.

Network firewalls work from layer 2 up to 4
Application firewalls work from layer 5 up to 7

Application firewalls can be either network based firewalls (web application firewall, focus on network), or host based (on the host itself, like SELinux).

Network firewalls can be network based firewalls (like physical hardware), and host based network firewalls (like a service on the host itself)

## Linux built-in network firewall
It can be mentioned (or worth mentioning) the `iptables (IPv4)`:
- ip6tables (IPv6)
- arptables (ARP)
- ebtables (Ethernet)

in general you can say `xtables`, which is a more common name. This are all user space (old style)

However, there is also Kernel levels like `netfilter`, that is supposed to drop some things.

User space but newer style is used `nft / nftables` to control network-filter functionality]
### netfilter
netfilter is supposed to be a part of the whole system, hence it does checks upon the whole packet(s) that are getting sent. This can be set into input and forwarding chains, depending on the type of communication.
There are 5 different hooks(chains) so needs to be checked in the simplified view.

`iptables` also has tables, which are meant for rules.

Rules are more like use cases (or just different types of tables desired for NAT for example and others)
### iptables
This one has various tables, and they come in into a certain order.
With this tool you can drop certain types of actions, like drop reply to pings.
### nftables
This is the newer version of the `iptables` and has also tables that can be shown. Right now, if you use `iptables`, this are getting translated into nf_tables related commands!

nftables has more improvements comparing to the "legacy" tool. For example this thing can work with IPv6

This tool is also usually underlying in the other tools.
### Services
Fun fact, but all of that is non-persistent. Now in order to change that - you need to make it work with a config file and service.
## TCP wrappers
In some distributions we have /etc/hosts.allow + deny and can have a shared library that is supposed to be used. It checks the /etc/ files and then uses it as an additional filter, in order to get rid of additional rules being added, and not by you.
This files work on application/process level, and not kernel like iptables.
## Systemd IP access lists
You can even make systemd units in order to block/allow various IP addresses and other cool shit.
This is even made even before being handled by the daemons.

# Conclusion
The things like `ufw` or `firewall-cmd` is actually more host based, hence if you want more way like the network firewall, then you better use `nftables` or `iptables`