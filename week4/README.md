# Week 4: Socket Programming (Selectors + Multithreading)
## [Slides](https://docs.google.com/presentation/d/1AB5FJzucpvIFSb3GkcKP3CWLpxsQQCh8-ObmwBqWu_g/edit?usp=sharing)


## Socket Programming

### TCP
Transmission Control Protocol (TCP) is a reliable protocol for sending data over a network. With TCP, you are guaranteed reliable and in-order delivery of data albeit at higher performance overheads. TCP is a two-way protocol so data can flow between sender and receiver on the same socket.

#### v3
In v3, we change the server to communicate between multiple clients concurrently using selectors. We use the same v2 client for this server except the server can now communicate with several clients simultaneously.
##### Selector:
Selectors are a technique for multiplexing several I/O file descriptors like sockets. A selector registers with a descriptor (socket in this case) and its data. When the socket has data to be read or written, the selector fires an event that can be used to identify the socket and what it needs to be done. This way the program can iterate over fired events without being blocked by a particular `accept()`, `recv()`, or `send()/sendall()` command.
##### Server: 
    1. Initialize selector
    2. Register server socket as selector
    3. Retrieve events from selector
    4. Iterate over events
      4.1 If event is from server socket (i.e., data is None), accept new connection
      4.2 If event is not from server socket (i.e., data is not None so it is from a client socket), see what event was fired (READ or WRITE) and handle accordingly
    5. Repeat from step 3.
#### v4
In v3, while the server can communicate with multiple clients, it is technically not concurrently. It is still the main program which loops through each socket to see the events to respond to. Assume if the server had to perform a long-running operation that takes several seconds before responding to the client. In this case, all the clients would be stalled until the server finishes. To communicate with several clients simultaneously but not stall all of them, we can use threads instead.

##### Threads:
Threads are the most basic unit of instruction execution in a program. All processes by default have one thread (i.e., the main thread) which executes the program logic. Processes can spawn multiple threads to handle various tasks. In a multithreaded server, the main thread listens for new connections and spawns a child thread for each client.

##### Server: 
    1. Defines a handler function for the client
    2. Accepts a new connection
    3. Starts a new thread with the handler function and passes the newly connected client's socket
    4. Main thread repeats from step 2. Child thread executes the handler function.
