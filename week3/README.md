# Week 3: iPerf + Socket Programming
## [Slides](https://docs.google.com/presentation/d/1tZcDmWeixJttmM3WIbkqZgrDJSVMTp5hfPGky3FIYak/edit?usp=sharing)


## iPerf3 ([installation](https://iperf.fr/iperf-download.php), [documentation](https://iperf.fr/iperf-doc.php))
iPerf3 is a tool for active monitoring of the bandwidth of a network connection.
-  Server mode: `iperf3 -s`
-  Client mode:
    - TCP: `iperf3 -c <ip_addr>`
    - UDP: `iperf3 -c <ip_addr> --udp`
  
## Socket Programming

### UDP
User Datagram Protocol (UDP) is a fast but unreliable protocol for sending data over a network. With UDP, there is no guarantee of data reaching the recipient and, even if it does reach the recipient, the packets may arrive out-of-order. There is no way for the sender to know whether the data was received. UDP is also a one-way protocol so data can only flow one-way on the same socket.
### TCP
Transmission Control Protocol (TCP) is a reliable protocol for sending data over a network. With TCP, you are guaranteed reliable and in-order delivery of data albeit at higher performance overheads. TCP is a two-way protocol so data can flow between sender and receiver on the same socket.

#### v1
In v1, both the client and server only send one ping-pong message and then disconnect. The server then waits for a new client.
##### Client:
     1. Connects
     2. Sends one ping
     3. Receives one pong
     4. Disconnects
##### Server: 
    1. Accepts connection
    2. Receives one ping
    3. Sends one pong
    4. Repeats
#### v2
In v2, the client and server send ping-pong messages indefinitely until the client is force-killed. The server can only connect to one client at a time. Multiple clients have to wait for the server to disconnect before they can connect.
##### Client:
    1. Connects
    2. Sends pings indefinitely
    3. Receives pongs indefinitely
    4. Disconnects on force-kill (Ctrl-C)
##### Server: 
    1. Accepts connection
    2. Receives pings indefinitely
    3. Sends pongs indefinitely
    4. Repeats
