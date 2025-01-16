# Lecture 1
We wanted to separate IT and OT as much as possible, however currently we blend it together.

In OT the most important is Availability, then Integrity + Confidentiality
OT also has other parts

Purdue model is a method of leveling various industry parts where Level 0 is like sensors, and the upper layers is the Level of access to the internet.
This one is just needed for proper network layering.

First approach of controlling is SCADA (Supervisory Control and Data Acquisition). The data that we get there is not always very fast, so it is a bit delayed sometimes.

Another one is DCS (Distributed Control System), is the thing that is information on the site itself. This thing sends information to SCADA. All of the things can be combined

PLC (Programmable Logic Controller) is meant to program machines.
PLC always has communication, IO module, CPU, and power supply
Work - RAM
Load - storage
Retentive - direct instructions
PLCs has to be different from normal devices, as they are modular and has to be easily connected with others.

RTU (Remote Terminal Unit) is put above the sensor, and is meant to send information further. It is plainly a transmitter of information. (like a big box)

IED (Intelligent Electronic Device) is like a PLC, but is meant to control the electrical circuits and etc (for electronic stuff). It can open loops, control power.

HMI (Human Machine Interface) is just meant to see all the things that happen everywhere

Remote IO is just meant to control IO and has to be connected via different filed bus.

Variable-Speed Drives - this is a separate tool to control the speed of something, like a saw.

Industrial Gateways - similar approach to remote IO, but allows to plug and connect more and various devices.

Field Device - every device installed in the field, like sensor, PLC, and etc. Different from control center.

Field Bus - We use the circle approach and how the things are connected.

Control Loop - it is a bunch of things like a if statement, so that multiple things have to be activated to activate another thing, like multiple sensors.

PID Controller - another approach for the loop, but the other one does the things infinitely, but now it has error connection, to try and lever the values so that have more flexibility.

SIGMA CONTROL 2 is a new approach to make PLC things and etc.

Currently it looks like a HMI -> Controller -> Actuators and Sensors

Industry protocols:
- STP Spanning Tree Protocol (or RSTP which is Rapid) - it has some redirection of packages if some of the ports do not work. It is preventing layer 2 loop. It works in **tree** topology
- MRP Media Redundancy Protocol - works in a **ring** topology, and is also meant to be redundant.
- PRP Parallel redundancy protocol - the devices just have 2 cables, using the same values for IP and MAC, but different ports.
- HSR Highly-Available Seamless Redundancy - similar to MRP, but can communicate both ways. The information goes only to the one who needs it. When first packet was received, the second one is dropped. The difference with MRP is that the second port is locked, and will be unlocked if needed.

In terms of stages, we are on the verge of controlling things from Cloud, and one of the things is Profinet.

Protocols:
- Modbus TCP 502 - it works like 1 master and multiple slaves.
- S7Comm TCP 102 - similar to modbus, very insecure with plain text communication
- Profinet TCP/UDP 34962-..64 

Safety Instrumental systems (SIS) - are meant to be yellow things that will save people from bad things happening.

PLC and Safety PLC has the same things, but doubled (redundancy, and double checks), has monitoring and processing.
In normal approach it has everything doubled.
This things can be installed in various approaches
![[Pasted image 20250112122612.png]]

HFT Hardware Fault Tolerance - is Random Failure (something with values like microP on the image)
SFT Software Fault Tolerance - is Systematic Failure.
![[Pasted image 20250112122619.png]]
![[Pasted image 20250112123045.png]]

# Lecture 2
A PLC has various modules and can be put in various places around of it. Like a Communication Module, Processing Unit, and Signaling Board or something like that.

Work Memory - RAM
Load - storage like SSD
Retentive - more like cache

The memory is addressed by Memory Area, Byte and address (I guess)
![[Pasted image 20250112123307.png]]

The programming PLC languages have some way of being standardized.
First one is
Instruction List Programming (IL) - it is written like assembly, think of Low Level Language
Structured Text Programming (ST) - same as PASCAL pretty much, and is overall a higher level, and if looks like bash because works when you say start and end of a loop for example
Functional Block Programming (FBD) - it has blocks, that can be other functions
![[Pasted image 20250112123914.png]]
Ladder Logic Programming (LD) - It is what we have worked with, with LogixPro, it just has various controls.
Sequential Function Charts (SFC) - you divide it into steps, similar to blocks, but it has more text in it.
# Lecture 3
There is different levels for requirements, in the office is easier, in the industry is different, because you have chemicals, noise, and many other things.
You even have to sometimes build the cable itself.
![[Pasted image 20250112124158.png]]
In industry you do not want almost any delay. You also want insane values for availability

Isochronous communication works in cycles.

Modbus:
- Works like master and slave, can have like 247 slaves for 1 master
- It is not secure
- Has request + response or exception response

Profinet:
- Using ethernet
- Encapsulates data
- Works like the S7Comm, and it has great delays and etc.

![[Pasted image 20250112124745.png]]

# Lecture 4
SDR Software Defined Radio is that we make our own radio decoding and other things
You have various frequencies starting from the bigger ones to smaller ones.
![[Pasted image 20250112124852.png]]
![[Pasted image 20250112124857.png]]
Low frequencies - short and fast
High frequencies - long and slow

Ham radio are publicly available and can be done on special frequencies. The frequencies are regulated internationally, and also for the countries themselves.

Waves are the same things of a drop of water going down.
It is a combination of magnetic and electric wave
The waves go in all directions.
You have transmitter and antennas, and everything has to be sent in different sides.

Amplitude - difference on Y axys
Period - full movement on X value.

Phase shift - movement on X value
Vertical shift - movement on Y value

We use Fourier Theorem to translates waves into frequencies.

We have our Input Signal, and we usually need a carrier signal, and then you combine this to get modulation.

AM Modulation (Amplitude Modulation) - you have carrier, signal, and you do not care about the the frequency, you care about amplitude.
![[Pasted image 20250112125638.png]]
With FM (Frequency Modulation) - you change the frequency, and get different phase shift.

Decibel is meant to say how loud the signal is
![[Pasted image 20250112125915.png]]

Sampling - you have time access and when you care about it, and then you split the values and until they touch the line
Quantization - you build Y values

With AM you easily get noise.
With FM you get less noise, and you care about frequency. It is more expensive than the other one. Information is sent more often.
With PM Phase Modulation it is used in the very expensive things like satellites

To modulate signals we have values with 0 and 1
![[Pasted image 20250112130703.png]]
Shift key for example is when you have 0 and 1 values for the carrier + Signal
For frequency is the same approach, but the frequency is just much higher.
Phase shift key is even worse, because there you have more values in the 3 dimensional frequencies


![[Pasted image 20250112131017.png]]
![[Pasted image 20250112131116.png]]
RZ - Return to Zero
NRZ - Not Return to Zero
Unipolar - only positive values
Polar - negative and positive values
Bipolar - negative, positive, and zero values
![[Pasted image 20250112131306.png]]
![[Pasted image 20250112131351.png]]

Manchester Encoding is just meant to provide you with the clock, because otherwise knowing the clock is different every time.
![[Pasted image 20250112131704.png]]

All the remote devices need to be patented, and what is the exact code is being sent. This devices like remote things work on 433 MHz frequencies.

LF - K
MF - M
UF - G
# Lecture 5
Radio-Frequency Identification and Near-Field Communication is the same thing with the frequencies.

NFC is part of the other HF frequencies.
13.56 MHz.
It allows to communicate peer-to-peer

RFID need a tag, like a card, with antenna, and reader.
RFID can be passive, bipassive, and automatic.
This thing sends signals to readers when needed.
Reader is sending waves to identify passive cards, which give its power to the card, and then send it back.
![[Pasted image 20250112132401.png]]
- Low Frequency - RFID uses from 125 to 134 kHz for Low Frequency, less than 10 cm length. This also do not have security standards
- High Frequency - is from 3 to 30 MHz, and the length is 10 cm to 1 m, and it operates on the same frequency like NFC (13.56 MHz)
- Ultra High Frequency - is 860 to 960 MHz, it is either passive or active tags.
Active tags with Ultra High Frequency have a fucking battery inside, and make the tags more expensive.

Low Frequency (125kHz):
- HID Cards for RFID are one of the Low Frequency implementation, and can send limited data. The information needed is also printed on the card itself. Sends 26 bits.
- EM4x cards have the same approach, but send more data, 32 bits. Works with 125 kHz
- T55xx cards have like 224 bits that can be read. It uses manchester approach.
- ISO/IEC 14443

High Frequency:
- MIFARE Classic - this has encryption but it is already cracked. So this ones are not secure already
- MIFARE PLUS - this has 4 different modes of operation. It even uses AES once at least, starting with Level 3.
- MIFARE DESFire is one of the most sophisticated things.
- MIFARE Ultralight - this  is supposed to be the most secure version, because it uses Triple DES, or something like that, however it is not.

NFC has Data Exchange Format (NDEF) is an RFID High Frequency Implementation.
# AI
AI - Artificial Intelligence, with a lot of IF statements and they learns to solve problems
Strong AI - mimics humans
Narrow AI - something very specific
Machine learning - you do not have algorithms, but give data and results. They create the way to solve this.

Neural Networks - similar approach to our brains, because you have way more layers that allow to learn more deeply.
Output has multiple inputs or things that get us to the needed layer.
First layer does initial results, the other layers do some more computation.

Deep Learning is a subset of Machine Learning, you use smaller dataset that has sample algorithms and etc.

Narrow AI - is the AI that is meant to do some specific functions. ChatGPT is also considered narrow.

Strong AI - is something to copy the intelligence of people and think on their own.

One of the way that AI identifies objects, is that it does segmentation by Semantic, that it does separate instances.
Another is just putting everything in the looks of squares.
You can have optical character recognition.
Natural language processing - is to identify text and emails, translation and etc.

Document intelligence is just understanding the text, and do knowledge mining.

Problems with data is the same as IT Governance - Availability, Fairness, Ethical, Transparent, Reliable, and Safe and etc.

Machine Learning is more of a statistic, that calculates the probability of something being a case.

Supervised learning - you have known outputs
- Regression - predicts numeric values
- Classification - it tries to understand the values that will be there. It predicts class labels.
	- Binary classification
	- Multiclass classification

Unsupervised learning - you do not have known values.
- Clustering - it will narrow the amount of samples till the values will be the right ones or not.

You use Confusion Matrix to check how good your data has done.

![[Pasted image 20250112144345.png]]

![[Pasted image 20250112144349.png]]




