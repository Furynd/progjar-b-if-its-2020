import shelve
import uuid
import os
import io

srv_path = 'server/'

class File:
    def Upload(self,nama=None,data=None):
        fd=open(srv_path+nama, "wb")
        fd.write(data)
        fd.close()
        return True
    def Download(self,nama=None):
        if os.path.isfile(srv_path+nama):
            myfile = open(srv_path+nama, "rb")
            data=myfile.read()
            myfile.close()
        else:
            data=b'File tidak ditemukan'
        return data
    def Listing(self):
        dirlist = os.listdir(srv_path)
        fl = []
        for filename in dirlist:
            fl.append(filename)
        return fl