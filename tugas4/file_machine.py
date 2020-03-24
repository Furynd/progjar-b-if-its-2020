from file import File
import json
import logging

'''

protocol yang tersedia:
    list, download, upload

list
    penggunaan : list
    Melihat list file yang ada di server

download
    penggunaan : download [nama_file]
    Mendownload file [nama_file] dari server

upload
    penggunaan : upload [nama_file]
    Mengupload file [nama_file] ke server

'''

f = File()

class FileMachine:
    def proses(self, raw_input, data):
        s=raw_input
        s_input=s.split(" ")
        try:
            cmd=s_input[0].strip()
            logging.warning(cmd)
            if(cmd=='list'):
                logging.warning('List File')
                f_list=f.Listing()
                f_list={"list":f_list}
                return json.dumps(f_list)

            elif(cmd=='download'):
                logging.warning('Unduh File')
                f_name=s_input[1].strip()
                return f.Download(f_name)

            elif(cmd=='upload'):
                logging.warning("Unggah File")
                nama = s_input[1].strip()
                f.Upload(nama,data)
                return "OK"

            else:
                return "cmd salah"
        except:
            return "ada ERROR"