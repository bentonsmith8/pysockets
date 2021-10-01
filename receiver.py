# This script receives data from a sender script using a UDP socket

import socket 
# import the socket module to use
import signal 
# import signals module so ctrl + c actually kills the program

signal.signal(signal.SIGINT, signal.SIG_DFL)
# tells the OS to interrupt execution no matter what when the interrupt signal
# (ctrl + c) is received

# define some "constants" to be used later 
HOST = '127.0.0.1' 
# 127.0.0.1 is the 'loopback' address, or the address
# of your own computer
PORT = 2000 
# this number is arbitrary as long as it is above 1024
BUFFERSIZE = 1024 
# this number is mostly arbitrary as long as it is big enough

# the with statement automates error handling and closing resources when they're no longer needed.
# more info here: https://www.geeksforgeeks.org/with-statement-in-python/
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # AF_INET tells the socket we want to use IPV4 (addresses that look like xxx.xxx.xxx.xxx)
    # and SOCK_DGRAM tells the socket we want a UDP connection.
    s.bind((HOST, PORT))
    # s.bind tells the socket to listen on a specific ip and port
    while True: 
        # start a loop to receive data from
        (message, addr) = s.recvfrom(BUFFERSIZE)
        # reads a message from the socket and stores the address it came from
        decoded_message = message.decode()
        # decodes the message from a byte array into a string
        print("Message from client: " + decoded_message)