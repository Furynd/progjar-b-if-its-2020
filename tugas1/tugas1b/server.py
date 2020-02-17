import sys
import socket
from datetime import datetime

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on' + str(server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
	# Wait for a connection
	print('waiting for a connection')
	connection, client_address = sock.accept()
	print('connection from' + str(client_address))
	now = datetime.now()

	# Receive the request
	req = connection.recv(1024)

	try:
		if req:
			FILE = open(req, 'rb')
			buff = FILE.read()
			connection.sendall(buff)
			print('File sent.')
			FILE.close()
	except:
		print('Error Occured.')
	connection.close()
