import socket
from concurrent.futures import ThreadPoolExecutor
from handle_client import client_handler_thread

class thread_pool_tcp_echo_server:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._num_threads = 10

        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.bind((self._host, self._port))
        self._server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        self._server_socket.listen(20)
        print(f"Server listening on {self._host}:{self._port}")

        with ThreadPoolExecutor(max_workers=self._num_threads) as thread_executor:
            while True:
                client_socket, client_address = self._server_socket.accept()
                print(f"Connected to client {client_address[0]}:{client_address[1]}")

                # Submit the client connection to the thread pool
                thread_executor.submit(client_handler_thread, client_socket)

if __name__ == '__main__':
    port = 7777

    server = thread_pool_tcp_echo_server('localhost', port)
    server.run()
