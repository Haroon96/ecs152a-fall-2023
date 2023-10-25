import socket
from concurrent.futures import ThreadPoolExecutor

HOST = '127.0.0.1'
PORT = 5500

def handle_client(socket, addr, port):
    while True:
        data = socket.recv(1024)
        if data == b"ping":
            print(f"Received {data.decode()!r} from {addr}:{port}")
            socket.sendall(b"pong")
        elif not data:
            socket.close()
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    with ThreadPoolExecutor(max_workers=5) as executor:
        while True:
            client_socket, (client_addr, client_port) = server_socket.accept()
            print('here')
            executor.submit(handle_client, client_socket, client_addr, client_port)