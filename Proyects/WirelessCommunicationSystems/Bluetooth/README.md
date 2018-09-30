# Wireless Communication System using Bluetooth

Made by @Fernando_Cortez, @Felix_Quevedo, and @Luis_Serrano

Subject: **Computer Network**

Professor: **Dr. Moises Sanchez Adame**

University: **CETYS University, Tijuana**

#### Abstract

## Objective
Establish a wireless communication using Bluetooth between a transmitter and a receptor to control a process.

## Theoretical Framework

### Architecture
### Protocols
### Physical Layer
### MAC Sublayer Protocol
### Frame Structure

## Equipment and Material

## Development

### Electrical Circuit
### Software
To create the communciation between the two Raspberry Pi, their own bluetooth module were used.

### Communication

![Python version](https://img.shields.io/badge/python-v2.7-brightgreen.svg)

#### Server Code
```
import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port=1
server_sock.bind(("", port))
server_sock.listen(1)

client_sock, address = server_sock.accept()
print "Accepted Connection from ", address

data = client_sock.recv(1024)
print "received [%s]" % data

client_sock.close()
server_sock.close()
```
#### Client Code
```
import bluetooth

bd_addr = "00:00:00:00:00:00" #Server MAC address

port = 1 #Port to be used
sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM) #Create socket to use
sock.connect((bd_addr, port)) #Connect socket with the host

sock.send("Hello World!") #Send data to the server

sock.close() #Close communication
```

## Results and Analysis

## Conclusions

## References


