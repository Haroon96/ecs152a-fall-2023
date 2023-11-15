#!/bin/bash

# remove existing container
docker rm -f ecs152a-simulator

# build docker image
docker build -t ecs152a/simulator .

# start container and expose port number 5001
## --cap-add adds network capabilities for tc
## --rm removes container after user exits
## -p 5001:5001/udp binds 5001 inside the container to 5001 on the localhost
## -v mounts the hdd directory as /hdd inside the container. any file written by the container code will appear here
docker run --name="ecs152a-simulator" \
    --cap-add=NET_ADMIN \
    --rm \
    -p 5001:5001/udp \
    -v "$(pwd)/hdd":/hdd \
    ecs152a/simulator