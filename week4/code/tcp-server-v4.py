import socket
from concurrent.futures import ThreadPoolExecutor
from time import sleep

# specify host and port to listen on
HOST = '127.0.0.1'
PORT = 5500

# function to run in separate thread and handle client
def handle_client(socket, addr, port):
    # run indefinitely
    while True:
        # receive data from client
        data = socket.recv(1024)
        # do something with the data
        if data == b"ping":
            print(f"Received {data.decode()!r} from {addr}:{port}")
            # uncomment the line below to simulate long-response time from server
            # and how it doesn't stall other clients
            # sleep(10)
            socket.sendall(b"pong")
        elif not data:
            socket.close()
            break

# create a new TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # bind this socket to OS
    server_socket.bind((HOST, PORT))

    # set listening mode on for this socket
    server_socket.listen()

    # thread pool to contain all threads
    with ThreadPoolExecutor(max_workers=5) as executor:

        # run indefinitely
        while True:
            # accept a new connection
            client_socket, (client_addr, client_port) = server_socket.accept()

            # spawn new parallel thread for new client
            # main thread will continue back to accept new clients
            executor.submit(handle_client, client_socket, client_addr, client_port)