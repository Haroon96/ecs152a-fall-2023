import socket
import selectors
import types

HOST = '127.0.0.1'
PORT = 5500
selector = selectors.DefaultSelector()

def accept_connection(sock: socket.socket):
    conn, (addr, port) = sock.accept()
    data = types.SimpleNamespace(addr=addr, port=port, recv=[], send=[])
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    selector.register(conn, events, data)

def handle_message(key, mask):
    sock = key.fileobj
    data = key.data

    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data == b"ping":
            print(f"Received {recv_data.decode()!r} from {data.addr}:{data.port}")
            data.recv.append(recv_data)
            data.send.append(b"pong")
        elif not recv_data:
            selector.unregister(sock)
            sock.close()
    elif mask & selectors.EVENT_WRITE:
        if len(data.send) > 0:
            sock.sendall(data.send.pop(0))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    server_socket.setblocking(False)

    selector.register(server_socket, selectors.EVENT_READ, data=None)

    while True:
        events = selector.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                # accept a new connection
                accept_connection(key.fileobj)
            else:
                # receiving/writing data
                handle_message(key, mask)