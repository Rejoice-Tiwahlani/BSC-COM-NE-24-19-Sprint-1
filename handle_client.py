def client_handler_thread(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        else:
            client_socket.sendall(data)

    client_socket.close()


def connection_status_message(client_address):
    print(f"Connected to client: {client_address[0]}:{client_address[1]}")