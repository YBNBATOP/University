# Networking in Java
Generally, we need to make communication between 2 computers
These 2 computers are - server, and a client
We will need to implement these.

# Needs
For the connection we will need to make use of sockets (which is genuiely a port)

# Start
We will need to create a package "network"
Afterwards - 2 classes, **client** and **server**

The first one we implement is the **client** because it is closer to the end user

# Client
We need a **psvm**, and then create a **socket** using **Socket**
``` java
Socket socker = new Socket("localhost", 1234) // a host, and then a port
```

The upper function can as well throw exception, so that we need to wrap it with a **try-catch**, and throw a exception
Might be also useful to throw your own exceptions

# Server
Here we need to create a **psvm**, and then another **ServerSocket** which requires only a port
``` java
ServerSocket socket = new ServerSocket(1234) // only a port is needed
```
It should better be also wrapped in the **try()-catch** so that the connection is automatically closed for us!

After that, inside, we also create a **Socket** that accepts the connection

``` java
try (ServerSocket serversocket = new ServerSocket(1234)) {
	Socket socket = serversocket.accept();
}
```

Also do not forget to log most of the times, instead of throwing exceptions!

# Time to start
We can now run first the **Server**, then the **Client**.

But it is not enough to just connect them, we need to actually transfer data.

We need to create streams between the client and server

## Client
We need to actually create a **PrintStream**
``` java
PrintStream out = new PrintStream(socket.getOutputStream());
```

## Server
For the server we would need to create a **Scanner**

``` java
Scanner in - new Scanner(socket.getInputStream());
```

After this we can actually see the information on the server side appearing

After that we need to actually write a **while** so that our system will keep on running, so that we can keep talking to the server

So we would need to add a while loop after actually creating a **ServerSocket** inside the **try()-catch**.
``` java
try(sockethere) {
	while(running) {
		//dostuff
	}
}
```

To actually respond, we would need to write another Stream, an **PrintStream**, and we use the socket **OutputStream**, so that we can send a response

After we write that, we will also have to create a **Scanner** that actually reads the data

# Time to improve things
We can create another **client**, which will actually also be able to send messages to the server

Inside it you can actually make use of the first class main

# Multi-threading
After we actually set-up the clients to send data and server accept it, we also need to set-up multi tasking for our server

We are going to make use of **Thread** so that multiple messages can be processed at the same time!

That should be also done on the server side, inside the while loop.
``` java
new Thread(() -> processConnection(socket)).start();
```
**processConnection** function is the function itself that is important for opening connection and etc.

