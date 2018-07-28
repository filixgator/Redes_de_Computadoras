# Import Libraries
import socket

# Define IP Address, Port, and Buffer Size
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

# Create the TCP between the server and the client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr

# Make a loop to receive and send packets to the client
while True:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    conn.send(data)

# Close communication with the client
conn.close()
