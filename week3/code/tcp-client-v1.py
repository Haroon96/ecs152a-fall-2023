import socket

# specify server host and port to connect to
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5500

# create a new TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to the server
    s.connect((SERVER_HOST, SERVER_PORT))

    # send a single ping message
    # `b` before string converts string to bytes (alternatively, use "ping".encode())
    s.sendall(b"ping")

    # receive response from server
    data = s.recv(1024)

    # print server response
    print(f"Received {data.decode()!r} from {SERVER_HOST}:{SERVER_PORT}")