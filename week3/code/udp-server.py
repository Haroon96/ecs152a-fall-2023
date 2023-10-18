import socket

HOST = '127.0.0.1'
PORT = 5500

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received {data.decode()} from {addr}")