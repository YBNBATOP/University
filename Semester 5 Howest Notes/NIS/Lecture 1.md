# Introduction
This is about securing networks.
We got a couple colors in CS:
- Red Team - NSP, pentesting
- Yellow Team - Security by design, secure development
- Blue Team - NIS, and servers and etc

# SOC (Security Operation Center)
Monitor network and devices for possible threats, monitor alerts and identify security incidents
Incident response
Incident analysis + remediation
Threat intelligence
Reverse Engineering

The Important Stuff:
- There are also possible to view some videos regarding something new

Study load - 3 ECTS / ~75 hours

Evaluation:
- exercises (40%) + 24% checkpoint exam before final exam + 36% final exam (on campus, closed-book, PURE THEORY)
- practical exercises every week
- checkpoint exams will be available during the complete course on netacad, so free to do them whenever you get time
- one deadline for the checkpoint exam, BUT do not wait to study the modules. So read material, then  do the chapter exams. Each checkpoint exam takes about an hour, and one attempt.
- Certificate of Attendance (PDF) + badge if score is good enough.

All the labs are now building on each other, so the whole network to be built is coming all together! First 5 labs are easier, so speed them.

# Theory course
I will be invited to the netacad by the teacher, in order to be able to do everything.

# Practical exercises
VM based labs on selected topics from Cyberops:
- Networking
- VLANs
- Router and Firewall configuration
- IDS/IPS network monitoring
- Siem/SOAR
- + additional instruction videos regarding networking (not part of the exam)

Overall idea: get a server, get an admin workstation, and now I am the the IT admin to know the network, configure it and improve security

All works with the proxmox interface, with remote access to the network over VPN

Credentials: student - student

First mission - CHANGE THE PASSWORD.

URL: your-name.co.edu.technet.howest.be:8006

A lot of other VMs can be found there. At 3 AM the VMs turn off automatically, and usually it is needed to manually launch the environment

## Basic rules

Do NOT abuse acces to howest infrastructure
Do NOT interfere with other students setup!
- in case of non-compliance, you will be denied access to the systems = 0 for the exercises
Do NOT change anything w.r.t. the "gt" user and usergroup (= lector account)
Do make sure you keep detailed notes of your commands and modifications + firewall config (there are no system backups) - MAKE SURE TO ADD A LOT OF NOTES UPON WHAT IS BEING DONE.
Do have fun
If your environment brakes - then you will get a blank one

## Firewall labs
Configure your own networks, based on a PaloAlto/Fortinet Firewall VM appliance
Experience with current commercial platforms
Time equivalent to 3 labs
Optional PaloAlto course for support.

PaloAlto also has a course on firewall configuration and etc.

## Video recordings
There are also video recordings that can be used to check some prior knowledge or etc.

## Environment
It can be started manually, and accessed with the Howest CIT network.
You check all the Proxmox (if started), and then access your own (with the credentials)

Some machines a keyboard dependent, so change the main keyboard layout.