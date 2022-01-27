# This script sends data from the console to a receiver script using a UDP socket

import socket 
# imports the socket module

# (note, signal module not needed here because it behaves correctly)

HOST = '192.168.1.100' 
# 127.0.0.1 is the 'loopback' address, or the address
# of your own computer
PORT = 80 
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
        if message == "wheel":
            data = [0x23,0x00,0x12,0xf1,0xf3,0xe3,0x5b,0x9f,0x00]
            cs = sum([x for x in data[2:8]])
            print(cs)
            data[8] = cs & 0xff
            print(data[8])
            s.sendall(bytes(data))
        else:
            s.sendall(str.encode(message))
        # encode the string as bytes and send it over the socket