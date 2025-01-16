# Threading
Often called a "lightweight process"
-> Minimize context switching time
-> A "blocking thread does not block other threads"

Threading is mostly about splitting a process to multiple cores. What you in a word do - you virtually copy the "address" of a process and hand it to a CPU core for example. The pointers stay the same, but the moment one of the processes changes something, it changes for everything else (Copy on Write)

You keep the same virtual address, but you are starting a new code section inside the actual code space. Look at it like that - you can work in 2 people in 1 house, then everything is changed for you both. If you build one house, and your friend a separate one - you are independent from each other.

## Threads vs Processes
Processes & scheduling
- Responsibility with the OS -> CPU scheduling
Threads
- Responsibility with the application / program designer

## Threads vs fork()
Fork -> System call that creates a new child process
- If parent ends before child, the child becomes orphaned
Pthread_create -> All "part of" the same process
- There is no exit as virtual memory does not need clean up

## Child processes vs Parent processes
What happends with the child process if a parent process get's killed?
- It depends on the OS:
	- Child process get's killed as soon as parent get's killed
	- Child becomes an "orphan"
	- Child get's to live on without any issues
