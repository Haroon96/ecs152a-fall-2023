import socket

PACKET_SIZE = 1024
SEQ_ID_SIZE = 4
MESSAGE_SIZE = PACKET_SIZE - SEQ_ID_SIZE

# read data
with open('iliad.txt', 'rb') as f:
    data = f.read()
 
# create a udp socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:

    # bind the socket to a OS port
    udp_socket.bind(("localhost", 5000))
    udp_socket.settimeout(1)
    
    # start sending data from 0th sequence
    seq_id = 0
    while seq_id < len(data):
        
        # construct message
        # sequence id of length SEQ_ID_SIZE + message of remaining PACKET_SIZE - SEQ_ID_SIZE bytes
        message = int.to_bytes(seq_id, SEQ_ID_SIZE, signed=True, byteorder='big') + data[seq_id : seq_id + MESSAGE_SIZE]
        
        # send message out
        udp_socket.sendto(message, ('localhost', 5001))
                
        # move sequence id forward
        seq_id += MESSAGE_SIZE
        
    # send final closing message
    udp_socket.sendto(int.to_bytes(-1, 4, signed=True, byteorder='big'), ('localhost', 5001))