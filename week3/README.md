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
User Datagram Protocol (UDP) is a fast but unreliable protocol for sending data over a network. With UDP, there is no guarantee of data reaching the recipient and, even if it does reach the recipient, the packets may arrive out-of-order. There is no way for the sender to know whether the data was received.
### TCP
#### v1
#### v2
