import sys
import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)

Data="list"
sock.send(Data.encode('utf-8'))
sock.shutdown(socket.SHUT_WR)

data = sock.recv(1024).decode()
hasil=data
while (data):
    data = sock.recv(1024).decode()
    hasil+=data
print("List File: ")
print(hasil)

print("shutdown client")
sock.close()