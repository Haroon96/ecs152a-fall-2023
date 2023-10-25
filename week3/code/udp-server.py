import socket

# specify host and port to receive messages on
HOST = '127.0.0.1'
PORT = 5500

# create a new datagram socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    # bind this socket to OS
    server_socket.bind((HOST, PORT))

    # receive messages indefinitely
    while True:
        # data -> message, addr -> (client_addr, client_port)
        data, addr = server_socket.recvfrom(1024)
        print(f"Received {data.decode()} from {addr}")