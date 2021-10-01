# This script sends data from the console to a receiver script using a UDP socket

import socket 
# imports the socket module

# (note, signal module not needed here because it behaves correctly)

HOST = '127.0.0.1' 
# 127.0.0.1 is the 'loopback' address, or the address
# of your own computer
PORT = 2000 
# this number is arbitrary as long as it is above 1024
BUFFERSIZE = 1024 
# this number is mostly arbitrary as long as it is big enough

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # AF_INET tells the socket we want to use IPV4 (addresses that look like xxx.xxx.xxx.xxx)
    # and SOCK_DGRAM tells the socket we want a UDP connection.
    s.connect((HOST, PORT))
    # s.connect tells the socket to try to connect to a specific ip and port
    while True:
        # start a loop to read from console and send all input over the socket
        message = str(input())
        # read input from console
        s.sendall(str.encode(message))
        # encode the string as bytes and send it over the socket