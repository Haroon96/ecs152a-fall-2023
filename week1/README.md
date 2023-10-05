# Week 1: Wireshark + dpkt
## [Slides](https://docs.google.com/presentation/d/136Ypr11F75G9WfbH1vWkKr-sZnsW0-zpPL855_FHc5Q/edit?usp=sharing)

## Tutorial
### Wireshark ([installation](https://www.wireshark.org/download.html), [documentation](https://www.wireshark.org/docs/wsug_html_chunked/))
#### Capturing packets
1. Open Wireshark and choose a network adapter to capture packets from (e.g., Wi-Fi, ethernet, etc.).
2. Start capturing packets by cliking the icon on the top-left.
3. In your browser, visit [httpforever.com](httpforever.com), a HTTP-only website.
4. In Wireshark, stop capturing packets by clicking the stop icon.

#### Filtering packets
In the display filter field, experiment the following filters.
 - `http`: will show all http packets sent and received
 - `frame contains "some query"`: will show packets containing the string "some query"
 - `tcp.port==80`: will show all packets sent/received on port 80
 - `ip.src==ip_address`: will show all packets whose source IP is `ip_address` (replace `ip_address` with any IP)
 - `ip.dst==ip_address`: will show all packets whose destination IP is `ip_address` (replace `ip_address` with any IP)
 - `tcp.port==80 && ip.src==ip_address`: will AND both operators
 - `tcp.port==80 || ip.src==ip_address`: will OR both operators
 - `!ip.src==ip_address`: will NOT the filter

Read the documentation for more sophisticated filters.

#### Saving captures
Go to `File > Save As` and set the format as `Wireshark/tcpdump/... - pcap` to save the file in `.pcap` format. Use this saved file for the following dpkt tutorial.

### dpkt ([installation](https://pypi.org/project/dpkt/), [simple documentation](https://kbandla.github.io/dpkt/), [advanced documentation](https://dpkt.readthedocs.io/en/latest/))
- TBA
