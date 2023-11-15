#!/bin/bash
# simulate 100ms delay
# tc qdisc add dev eth0 root netem delay 100ms
# simulate 20% packet loss
tc qdisc add dev eth0 root netem loss "0%"
python receiver.py