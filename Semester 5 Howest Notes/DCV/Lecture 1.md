# Practical information
Most times, the servers are virtual servers

Evaluation:
- 33% - Practical exercises (do not count for the resit) (Have deadlines monday after autumn break and winter break. Quizzes - to check the answers on track; screenshots - personal; personal labs) (They prepare greatly for the exam)
- 67% - Exam3

Exam - multiple choice, closed book, more theoretical (but also comprehension), no guess penalty

# Hardware and virtualization
All the hardware (computer) looks theoretically the same. 

## CPU
It is a piece of shit that is supposed to transform electricity into basic calculation.
Architectures - AMD, Intel, ARM... x32 and x64
Clock speed - the speed of processed instructions per second
The instructions for CPU can be modified, and then you get other types of CPUs, like RISC
CPU has other necessity/parts:
- socket - the place where it plugs in
- core - independent processor
- thread - it is a logical processor that shares resources with other threads on the same core.

RAM - Random Access Memory, volatile, costs more
Storage - persistent, lower cost
Cache - optimisation buffer

## Interconnect
Major ones for servers:
- Bus topology (SCSI-(P)ATA)- several endpoints
- Point to point (SAS-SATA)
- Ring (FC)
- Start/Tree/Mesh (I-SCSI)

Speed depend on what I do and mainly determined by:
- Throughout - amount of the unit that be trasnported during a certain period
- Latency - the time before you actually do it

## Server vs PC
It is mostly that Server has other purpose for use

Servers (Reliability-Availability-Serviceabiltiy)

Servers, usually have specific processors (like Xeon), and use ECC-RAM (Error-Correcting Code)

## Availability
RTO vs RPO:
- Return to operations - time to be back in business
- Recovery point objective - what data are you allowed to lose

Paradox:
- High availability - keep on running until you can, even if you loose data
- Disaster recovery - stop if you risk loosing data, but make sure what is agreed can be recovered.

## Storage virtualization
The types of storage have like:
- DAS
- SAN (This one have like 3 types inside)
- NAS