import socket


SERVER_IP = '127.0.0.1'
SERVER_PORT = 5006


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))



while True:
    data, addr = sock.recvfrom(1024)
    #buffer size 1024
    print("diterima ", data)
    print("dikirim oleh " , addr)



