import sys
import socket

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

print('sending ', fileName, '...')

#check file existance
try:
    FILE = open(fileName, 'rb')
except:
    print('No such files.\n Terminating Program.')
    exit()

try:
    # Send file
    buff = FILE.read()
    sock.sendall(buff)
    print('file sent.')

finally:
    FILE.close()
    print('closing socket')
    sock.close()
