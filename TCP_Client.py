# Create a TCP Socket that sends data to the socket created on the other machine using nc

# Questions:
# When we create a raw socket like this, do we need to define the receiving socket as well or only the sending socket?
# How do we set the attributes of an object?
# Why socket.socket() and not just socket?

import socket

# Why is it being weird about .1?
HOSTNAME = "192.168.0.161"
PORT = 49999


def tcp_client():
    # define address type and socket type
    sending_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind socket to an IP and a port
    sending_socket.connect((HOSTNAME, PORT))
    # send buffer, cannot be a string. Needs to be bytes
    sending_socket.send(b"Hello")
    # Close it out
    sending_socket.close()


tcp_client()
