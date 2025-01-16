# Deadlock
There are multiple locks in a system, which allows the system itself to manage its processes properly. For example there should be some kind of scheduling for a process to access the internet, or do anything else specifically. Such mechanisms should have atomic mechanisms that would restrict something for a process.

Deadlocking is like a trafffic intersection.  If a process ask for something, and that something ask for something else in a loop - we are locked.

## Deadlock conditions:
- Mutual exclusion: "only one process at a time can use the resource"
- Hold and wait: "A process must be holding at least one resource and waiting to acquire additional resources that are being help by other processes"
- No preemption: There is no authority that can force to release a lock, only the process itself can do this
- Circular wait: a process has a resource locked, is waiting for a secind resource, which is used by another process that also wants the resource held by the first process. Can we multiple processes also

## Methods for handling deadlocks
- "Ignore the problem and pretend that deadlocks won't occur"
	- Assumes that device drivers and user process
- Allow the system to enter a deadlocked state (a)
	- Detect it
	- Recoover it
	- Typically, with algorithms
- Take measures to pprevent or avoid deadlocks, ensuring that the system will never enter a deadlocked state (b)

Deadlock **prevention (b)** vs deadlock **avoidance (a)**

"By ensuring that at least one of these conditions cannot hold, we can prevent the occurence of a deadlock"

## Consumer-Producer problem in distributed systems
It can be part of your application / the system to be in a "deadlocked" state

# Memory management

## Main memory
Basic hardware
"Main memory and the registers built into the processor itself are the only storage the CPu can access directly"

In other words:
- Processes (or parts) need to be stored in memory

## Cache
Registers built into CPU -> fast and accessible withing one cycle of the CPU clock. This is not the case with memory causing the CPU to "stall". Solution: cache == add "fast memory" between CPU and the main memory

## A process "lives" in the memory
Once again:
- A program/binary/executable - is not running - and lives typically on HDD/SSD
- A process - is running  - and lives in memory (RAM & Registers)
	- Exception: Virtual Memory:
		- Use HDD/SSD as if it is memory because of memory (RAM) shortage
		- Swapping/Swap Space/Page faults because page is not in memory

## Lack of memory
Swapping
- Swap out internal memory and put it on external memory
	- Time necessary for context switching can be high

## How to divide memory
- Consecutive memory allocation
- Memory of a process is whole block
	- Static partitioning
	- Dynamic partitioning
	- git pull != pull bitches
- Non-consecutive memory allocation
- Memory of a process is divided in blocks
	- Paging
	- Segmentation

## Partitioning
Fragmentation
- Internal fragmentation in case of static partitioning
- The operating system can keep track of average fragmentation so an improved partitioning can be determined
- External fragmentation in case of dynamic partitioning
- The operating system decides to reorganize memory (= garbage collection)
	- Coalescing = rebuild partition table, consecutive free partitions will be merged into one big free partition
	- Compaction = all occupied partitions will be stored consecutively followed by one freee partition; only possible in case of relocatable code

## Nonconsecutive
Nonconsecutive memory allocation
- Paging
- Segmentation
- Combination of segmentation and paging

## Paging
- Basic methods
	- Logical address space:
		- divided in pages
	- Physical address space:
		- divided in frames

Page size versus overhead:
- Normal page size? Between 512 bytes and 8KB
- Fragmentation? Internal, 1/2 frame average per process
- Page table needs internal memory, one entry per page
- Optimal page size?
	x = page size
	f(x) = overhead
	optimal f'(x) = 0

## Virtual memory
There are multiple algorithms
FIFO = first in, first out
- Oldest page needs to be swapped

LFU = least frequently used
- Less used pages will be swapped

OPT = optimal
- Replace the page that will be inactive (not used) for the longest time

LRU = least recently used
- Recent history as an indicator for the near future
- Timestamp usage of page or stack (put page on top of stack in case of reference)

Implication of virtual memory in coding
- Choose the right data structure
	- Stack, queue => good locality
	- Hash table => bad locality
- Choose the right algorithm
	- Compare array access by row with access by column
