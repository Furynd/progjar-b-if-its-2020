import sys
import socket
from datetime import datetime

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to port '+ str(server_address))
sock.connect(server_address)

print(len(sys.argv))

if len(sys.argv) == 1:
    print('No file selected.')
    fileName =  'pima-indians-diabetes.csv'
else :
    fileName = sys.argv[1]

print('requesting ', fileName, '...')

try:
    # Send request
    buff = bytes(fileName, 'UTF-8')
    sock.sendall(buff)
    print('request sent.')

finally:
    FILE = open('client/received.csv','wb')
	# Receive the data
    while True:
        data = sock.recv(1024)
        if data:
            FILE.write(data)
        else:
            break
    print('file received successfully.')
    FILE.close()
    print('closing socket')
    sock.close()
