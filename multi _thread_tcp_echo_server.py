import socket
import threading
from handle_client import *

class multi_thread_tcp_echo_server:
    def __init__(self, host_ip, port_number):
        self._host = host_ip
        self._port = port_number

        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.bind((self._host, self._port))
        self._server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        self._server_socket.listen(20)
        print(f"Server listening on {self._host}:{self._port}")

        while True:
            tcp_client_socket, tcp_client_address = self._server_socket.accept()
            connection_status_message(tcp_client_address)

            tcp_client_thread = threading.Thread(target=client_handler_thread, args=(tcp_client_socket,))
            tcp_client_thread.start()

if __name__ == '__main__':
    server = multi_thread_tcp_echo_server('localhost', 9000)
    server.run()
