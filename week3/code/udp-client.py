import socket

# specify server host and port to connect to
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5500

# open a new datagram socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:

    # send 10 ping messages to the server
    for message_id in range(1, 11):
        # craft message body
        # .encode() converts to bytes
        message = f"Ping #{message_id}".encode()

        # send message
        client_socket.sendto(message, (SERVER_HOST, SERVER_PORT))
