#!/bin/bash
# simulate 20% packet loss
tc qdisc add dev eth0 root netem loss "20%"
python receiver.py