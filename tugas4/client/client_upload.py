import sys
import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)

Filename = input("input nama file ")
if os.path.isfile(Filename):
    command = "upload " + Filename
    print("Mengirim: " + Filename)
    myfile = open(Filename, "rb")
    Filename = "ITS" + command
    Filenc = Filename.encode("utf-8")
    datasend = myfile.read() + Filenc
    sock.send(datasend)
    sock.shutdown(socket.SHUT_WR)
    hasil = sock.recv(32).decode()
    print(hasil)
else:
    print("File tidak ditemukan")

print("shutdown client")
sock.close()