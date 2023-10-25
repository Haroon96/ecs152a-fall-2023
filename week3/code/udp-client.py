import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5500

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    for message_id in range(1, 11):
        message = f"Ping #{message_id}".encode()
        client_socket.sendto(message, (SERVER_HOST, SERVER_PORT))
