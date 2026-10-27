import socket

SERVER_IP = "192.168.0.161"
SERVER_PORT = 63238

CLIENT_IP = "192.168.0.161"
CLIENT_PORT = 64458


def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # bind address needs to an IP assigned to the machine
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.connect((CLIENT_IP, CLIENT_PORT))
    data, address = server_socket.recvfrom(128)
    print(data)
    print(address)


udp_server()
