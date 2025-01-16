# Overview
We will see a lot of topics in one day:
- VPN (like you create one VPN with Wireguard?)
- Intruder detection + prevention (Surricata)
- SIEMs (like things similar to Elastic)
- Make our own commercial firewall
# VPN
Up until now, we configured Firewall, having then 3 VLANS, and all of this having access to network.
On the OSI layer, we already talked about:
- Data Link
- Switches
- Routing and IP
- Transport layer - Port forwarding
All of this - is default firewall configuration/functionality
We will still do things on this levels for now. We will make sure to get rid of firewall connection to internet (as in nothing will come to it, but can come out of it)
But to still have access to the network, we will need VPN, which we will create.
We will create a VPN to some network part of ours.
We have several options:
- Go to firewall
- LAN
- or Admin

Hence, we are not making one to Firewall, because otherwise everything can get compromised.
Why also have access to LAN, if we better get access to Admin, because we are administrators. We will do it in 2 ways, first making like a tunnel, and the other one will be opening the whole part of the network. For all the stuff we will use **Wireguard**
At first, we will open a port on firewall, and then point it to Admin server. Wireguard is using UDP, so the port should be UDP as well.

# IDS (Intrusion Detection System)
This thing looks beyond IP port, and look into the packets. That is a thing that can detect things being wrong.
IDS is useful because it is also favorable for the whole network.

# SIEMs, SOARs (Security Orchestration, Automation and Response), SOC (Security Operation Center)
We will get outside of our OSI model, and take a look at the log files, sessions, and other things.
We are going to take a look at the **Wazuh**. It is a very resource extensive thing.

## IDS/IPS
This things constantly monitor the network, and take actions.
IDS works on the firewall. It goes into the network layer of the firewall.
## EDR/XDR
Endpoint detection and response, focuses on endpoints and devices.
XDR takes a look at the payload. Everything coming after the header. 
Typical scope:
- Malware detection
- User behaviour
- Identity management
## SIEM/SOAR
Security Information and Event Management, which is focused towards events, or something that happens. It really looks for abnormal behaviour
SOAR though, is meant to make automation of the **threat responses**.
Typical scope:
- Event correlation and enterprise response
- OS behaviour
- Auditing and policy monitoring
- Regulatory compliance
- Threat intelligence

## SOC
It is a control system, that is supposed to respond to various things, but SOAR is the one already doing automation.
SOC though is a center where you control things. It is also responsible for governance
SOC includes:
- A central control center
- IT security analysis
- Processes
- IT security tools
- Various IT security services
Every system has vulnerabilities, so it is not going to be safe and needs to have monitoring.

## Wazuh ELK stack architecture
Data igestion (wazuh-agent) - is the main part where you get information from logfile and command execution (like password change)
Data storage (wazuh-manager) - stores and collects all the data
Most important files:
- Configuration file of agent or manager
- Logfile of agent or manager
- Manager only
- Binary that has the response action

Wazuh has a bunch of predefined rules for me. Also a lot of active response commands are also locked in and ready to trigger.

Agent (ossec.def) defines what to inject into the ELK stack engine, ahs modules, log ourput, active response.
Server has active responses that can be triggered, and have locations that can be redirected to.
Lets just say it works like an if statement that constantly looks for some information on the network.

Syscheck and rootcheck is more about file changes and their checksums, something related to that.

YARA is a way of detecting malware. It looks for certain characteristics.

Sigma rules, is also responsible for detection of things, and you can even make event correlation

In the exercise:
- I will start Wazuh server
- Add Wazuh agents
- Explore pre-defined rules
- Setup automation rules
