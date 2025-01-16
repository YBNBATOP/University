*To make sure that you will succeed in the exam you need to be able to answer the after exam questions!
Also it would be very useful to know that the exam is multi-choice*

# Recap
The lower/closer you are to the OS in the "process topology" - the higher your performance.

"Imagine running teams in a browser in a virtual  
machine in your windows 10 virtual machine  
from hardware & desktop operating systems.”

If you use something "as-a-service" - then you would just pull a container.
In case of "on-prem" - then you would do everything yourself.

# Processes
Everythin we do is always compeled of processes (even Linux itself). There is a difrence between **job** and **process**. The difference is them being just different time meanings. Job is older (sometimes said as "job scheduling").

## Process
It works in the CPU. It is the component part of any Program, and is mainly being the thing altered to completely execute a program.

### Process state
Every process has a state:
- **New**: process created;
- **Running**: instructions are being executed;
- **Waiting**: it is waiting for some event to occur;
- **Ready**: it is waiting to be assigned to a processor;
- **Terminated**: process has finished execution

### Process Control Block
The information associated with a process is called a Process Control Block (PCB, also called task control block). A PCB contains everything that your kernel would need to execute the process.

### Context Switch
It is saving/storing the state of a process (or thread). So it takes time to work on a process, then save its state, and then go to another process.
## Program
If compiled a C program, then we get an executable that is sitting on our disk. Once we execute it, there are starting **processes** that are in your memory and disk!

# Stack vs Heap
Stack - managed "automatically" bu the compiler
Head - represents dynamic data, so managed by the programmer.

Stack works according to the LIFO (Last in First out), so that every time we call a function, we put it on top. Once we exit the function, it goes out.

The heap will store values afterwards.

# Let's crash the system
If anything goes wrong in the kernel (even though we as users cannot interfere with the kernel) then eveyrthing goes wrong.

# Introduction to C
C is a compiler. It will take the program we wrote, and transform that into an image that can be read by the system.

Structure:
Headers are used as readable files for the system. They are reusable. They have already been compiled by the system.
Main is always working.
Then variable declaration.
Then body of a function for example.
Then we return a value.

The compiler transforms the code into assembly code, which is then assembled with the libraries, and then you get your executable file.

With a compiler you have a final file!
With a interpreter, you would read instruction by instruction.

Kernel modules are making the Kernel itself a whole. By creating your own kernel modules, we add functionality to the kernel.

# Algorithms and Performance
Algorithm - step by step approach to get an output. OR a step-by-step procedure for solving a problem.

We can also have different Data Structures.

Data structures can be dynamic or static.

# Practical intermezzo
When a parameter is passed by reference, the caller and the callee is the same variable for the parameter. If the callee modifies the parameter variable, the effect is visible to the caller's variable.

When a parameter is passed by value, the caller and callee have two different variables with the same value. If the callee modifies the parameter variable, the effect is not visible to the caller.


