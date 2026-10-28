# create a socket
# bind it
# accept the connection
# receive data
# close it

import socket

SERVER_IP = ""
SERVER_PORT = 1


def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.accept()
    server_socket.recvfrom(1024)
    server_socket.close()


tcp_server()
