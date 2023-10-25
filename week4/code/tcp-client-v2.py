import socket
from time import sleep
from random import randint

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_HOST, SERVER_PORT))
    while True:
        s.sendall(b"ping")
        data = s.recv(1024)
        print(f"Received {data.decode()!r} from {SERVER_HOST}:{SERVER_PORT}")
        sleep(1)