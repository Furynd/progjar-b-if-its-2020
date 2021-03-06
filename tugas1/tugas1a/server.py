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

	FILE = open('server/received.csv','wb')

	# Receive the data
	while True:
		# try:
		data = connection.recv(1024)
		if data:
			FILE.write(data)
		else:
			break
		# except:
			# Clean up the connection
	print('file received successfully.')
	FILE.close()
	connection.close()
