import random
import socket

PACKET_SIZE = 1024
SEQ_ID_SIZE = 4

def create_acknowledgement(seq_id):
    return int.to_bytes(seq_id, SEQ_ID_SIZE, signed=True, byteorder='big') + b'ack'

# create a udp socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
    # bind the socket to a OS port
    udp_socket.bind(("0.0.0.0", 5001))

    # file to write to
    recv = open('/hdd/recv.txt', 'wb')
    
    # start receiving packets
    while True:
        timeouts = 0
        try:
            # receive the packet
            packet, client = udp_socket.recvfrom(PACKET_SIZE)

            # get the message id
            seq_id, message = packet[:SEQ_ID_SIZE], packet[SEQ_ID_SIZE:]

            # if the message id is -1, we have received all the packets
            seq_id = int.from_bytes(seq_id, signed=True, byteorder='big')
            if seq_id == -1:
                # send the acknowledgement
                udp_socket.sendto(create_acknowledgement(seq_id), client)
                break
            
            # write message to file
            recv.seek(seq_id)
            recv.write(message)

            # create the acknowledgement
            acknowledgement = create_acknowledgement(seq_id)

            # send the acknowledgement
            udp_socket.sendto(acknowledgement, client)
        except socket.timeout:
            timeouts += 1
            if timeouts > 3:
                break
    
    recv.close()