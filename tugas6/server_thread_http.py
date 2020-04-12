from socket import *
import socket
import threading
import logging
import time
import sys
import json
from http import HttpServer

httpserver = HttpServer()

class ProcessTheClient(threading.Thread):
	def __init__(self,connection,address):
		self.connection = connection
		self.address = address
		threading.Thread.__init__(self)

	def run(self):
		recv = ""
		while True:
			try:
				data = self.connection.recv(1024)
				if data:
					d = data.decode()
					recv=recv+d
					if recv[-2:]=='\r\n':
						logging.warning("data dari client: {}" . format(recv))
						hasil = httpserver.proses(recv)
						hasil=hasil+"\r\n\r\n"
						logging.warning("balas ke client: {}" . format(hasil))
						self.connection.sendall(hasil.encode())
						recv=""
						self.connection.close()
				else:
					break
			except OSError as e:
				pass
		self.connection.close()

class Server(threading.Thread):
	def __init__(self):
		self.the_clients = []
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		threading.Thread.__init__(self)

	def run(self):
		self.my_socket.bind(('127.0.0.1',10001))
		self.my_socket.listen(1)
		while True:
			self.connection, self.client_address = self.my_socket.accept()
			logging.warning("connection from {}".format(self.client_address))
			
			clt = ProcessTheClient(self.connection, self.client_address)
			clt.start()
			self.the_clients.append(clt)
	

def main():
	svr = Server()
	svr.start()

if __name__=="__main__":
	main()

