# Overview
What we study:
- OT/ICS Security
- Communication Security (SDR)
- RFID/NFC
- AI

Grading:
- Theory exam: 50%
- Labs | Reports: 50% 
# Intro
This is a course about a little bit of everything. As Security professionals we are supposed to see more about it.
Since ICS (Industrial Control Systems) is/are used in a bunch of branches, such as:
- Nuclear
- Oil & gas
- Transportation
- Pharmaceutical
- Water
- other industries
## Why?
Because the critical infrastructure and strategic industrial assets are within the most global risks! So making something about it is crucial!

Securing Industrial Systems feel like Sisyphus work.

## The challenge
The whole story with IT and OT being 2 different things - now became one big thing, as a symbiosis.

IT security:
- Data (CIA)
	- Confidentiality
	- Integrity
	- Availability

OT (Operational Technology) security (it has more than one thing):
- Data (AIC)
	- Availability
	- Integrity
	- Confidentiality
- Physical Process
	- Safety
	- Environment
	- Dependencies
	- Regulation

ICS = broad amount of command and control networks and systems that are meant to support all types of industrial processes. Such systems are:
- SCADA - Supervisory Control and Data Acquisition system
- DCS - Distributed Control Systems
- PCS - Process Control Systems
- SIS - Safety Control Systems
- PLC - Programmable Logic Controllers

Lets not forget about networks:
- Office (Corporate IT + ERP servers or Production Management Systems)
- Industrial Control Systems:
	- Supervision Network (Supervision consoles + Engineering Stations + SCADA Servers which are Historian/Logging servers) - like the network checking all the processes
	- Production Network (HMI + PLC + Sensors + Robots + Drives)

Most Industrial Control Systems are built according to **Purdue Model** which is responsible for splitting/segregating everything into various levels.

# Devices
## SCADA
This is like the main center that is responsible for supervision of the plant, with a lot of screens and looks like something from NASA
## DCS
Looks like an electrical box mostly responsible for automizing industrial equipment
## PLC (Programmable Logic Controller)
Usually looks like a brick, and quite a modular one. Can be added with more modules (all of course vendor specific). Such modules are PSU, CPU, IO (Input Output), Communication modules
### Features
- Rugged, noise immune
- Modular plug-in
- Standard input/output connections and signal levels
- Easily understood programming language
- Ease of reprogramming
- Capable of communicating with other devices (PLC, computers, intelligent devices)
- Competitive in both cost and space occupied with relay and solid-state logic systems 
## RTU (Remote Terminal Unit)
This looks like an electrical box as well, and has remote communication abilities to control processes in remote locations 
## IED (Intelligent Electronic Device)
Electronic device (duh) like a regulator or circuit control that can communicate
## HMI (Human-Machine Interface)
It is the user interface to the processes of the industrial control systems. It is responsible to communicate to PLCs, RTUs and other industrial assets and transform it into human readable interface, and all of this is used to monitor and control processes.
## Historian
It is a software service that accumulates data (time-stamped) with boolean alarms and events, which can then be queried 
## Remote IO
A separate hardware component, as the IO are not located on the controller itself. It communicates with the controller over fieldbus.
## Drives
Adjustable Speed Drives (ASD) or Variable-Speed Drives (VSD) describes the equipment used to control the speed of machinery.
Different speeds for different products = hence need to regulate the speed of the lane.
## Industrial Gateways
This connect serial devices to an Ethernet network, but also allow for multiple connections and can convert between different protocols.
## Field Device
Equipment that is connected to the field side of ICS, supposed to monitor and control physical processes  in the industrial infrastructures.
## Field Bus
It looks like a cable which can have various form-factors and they are used to eliminate the need of point-to-point wiring between controller and each device
## Miscs
**Control Loop** - combination of control loops that makes sure the whole process is working properly (like boiling water)

**PID Controller** - a proportional-integral-derivate controller is a control loop mechanism that actually sees the data from a machine, and can repeat a process more times if needed.

# Network Redundancy
## Industrial Redundancy Protocols
This is about an extra entity to make sure network availability, and serves as a backup network, and avoid **single point failure**.
Redundancy is very important for security measures and production measures.

Protocols:
- STP (Spanning Tree Protocol) / RSTP (Rapid Spanning Tree Protocol) - designed to prevent layer 2 loops. Standardized with 802.D IEEE and is overall meant to prevent broadcast storms and ensure loop-free topology
- MRP (Media Redundancy Protocol) - allows rings of Ethernet switches to overcome any single failure with recovery time much faster than achievable with STP
- PRP (Parallel Redundancy Protocol) - this one is about using two independent networks at all levels and send the same message at the same time in the same networks.
- HSR (Highly-available Seamless Redundancy) - it works like a ring, and the whole idea is  to send the information on the node in 2 ways, so that if one is broken, then the idea is still getting where it is supposed to.


# Safety
Safety != Security

There are couple of levels in a diagram that are supposed to show the Prevention and Mitigation phase:
- Prevention
	- Process Design
	- Process Control (when you get a loop)
	- Operator Intervention (when you get an alarm)
	- Safety Instrumented System (when you get a trip)
	- Active Protection - relief valve, rupture disk (when you get an incident)
- Mitigation:
	- Active Protection
	- Passive protection
	- Emergency response

## SIS (Safety Instrumented Systems)
This are designed to give a reaction to hazards, or raise the actions to being hazards if no actions have been taken, and of course can take actions defined that either prevent or mitigate the hazard.
Examples:
- High fuel gas pressure furnace initiates shutdown of main fuel gas valves
- High reactor temperature initiates fail open action of coolant valve
- High column pressure initiates fail open action of pressure vent valve

There are Controllers, Sensors, and Safety PLCs

Safety PLCs are different from normal PLCs as they have memory and processors continuously monitored by watchdog circuits

The normal and safety PLCs used to be split, but now this devices can be inter-connected together and have similar components