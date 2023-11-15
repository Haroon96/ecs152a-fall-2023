#!/bin/bash

# remove existing container
docker rm -f ecs152a-simulator

# build docker image
docker build -t ecs152a/simulator .

# start container and expose port number
docker run --name="ecs152a-simulator" \
    --cap-add=NET_ADMIN \
    --rm \
    -p 5001:5001/udp \
    -v "$(pwd)/hdd":/hdd \
    ecs152a/simulator