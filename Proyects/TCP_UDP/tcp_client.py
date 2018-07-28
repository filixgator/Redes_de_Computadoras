# Import Libraries
import socket

# Define IP Address, Port, Buffer Size, Data
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

# Create the TCP between the client and the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)

# Receive packet and close communication
data = s.recv(BUFFER_SIZE)
s.close()

# Print in console the data received
print "received data:", data
