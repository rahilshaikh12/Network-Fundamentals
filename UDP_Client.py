import socket

HOST = "192.168.0.161"
PORT = 63238


def send_data():
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_client.connect((HOST, PORT))
    udp_client.send(b"Hello")


send_data()
