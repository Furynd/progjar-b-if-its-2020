import sys
import os.path
import uuid
from glob import glob
from datetime import datetime
import urllib.parse

class HttpServer:
	def __init__(self):
		self.sessions={}
		self.types={}
		self.types['.pdf']='application/pdf'
		self.types['.jpg']='image/jpeg'
		self.types['.txt']='text/plain'
		self.types['.html']='text/html'
	def response(self,kode=404,message='Not Found',messagebody='',headers={}):
		tanggal = datetime.now().strftime('%c')
		resp=[]
		resp.append("HTTP/1.0 {} {}\r\n" . format(kode,message))
		resp.append("Date: {}\r\n" . format(tanggal))
		resp.append("Connection: close\r\n")
		resp.append("Server: myserver/1.0\r\n")
		resp.append("Content-Length: {}\r\n" . format(len(messagebody)))
		for kk in headers:
			resp.append("{}:{}\r\n" . format(kk,headers[kk]))
		resp.append("\r\n")
		resp.append("{}" . format(messagebody))
		response_str=''
		for i in resp:	
			response_str="{}{}" . format(response_str,i)
		return response_str

	def proses(self,data):
		
		requests = data.split("\r\n")
	
		baris = requests[0]
	
		all_headers = [n for n in requests[1:] if n!='']

		j = baris.split(" ")

		hasil2=requests[len(requests)-1]
		hasil=hasil2.split("=", 2)
		try:
			method=j[0].upper().strip()
			if (method=='GET'):
				object_address = j[1].strip()
				return self.http_get(object_address, all_headers)
			if (method=='POST'):
				object_address = j[1].strip()
				return self.http_post(object_address, all_headers, hasil)
			else:
				return self.response(400,'Bad Request','',{})
		except IndexError:
			return self.response(400,'Bad Request','',{})

	def http_get(self,object_address,headers):
		if (object_address == "/"):
			isi = "<h1>SERVER HTTP</h1>"
		elif object_address == "/sending.html":
			fp = open("sending.html", 'r')
			isi = fp.read()
		else:
			return self.response(404,'Not Found','',{})

		headers = {}
		headers['Content-type'] = "text/html"
		return self.response(200,'OK',isi,headers)

	def http_post(self,object_address,headers,hasil):
		head = headers
		headers = {}
		headers['Content-type'] = "text/html"
		teks=urllib.parse.unquote_plus(hasil[1])
		temp = ""
		for h in head:
			temp = temp + h + "<br>"
		
		isi = "<h1>"+teks+"</h1>"+"<br>"+"<p>"+temp+"</p>"
		return self.response(200,'OK',isi,headers)