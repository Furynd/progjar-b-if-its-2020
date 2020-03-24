Tugas 4

protocol yang tersedia:
    list, download, upload

### list
penggunaan : list
<br>
Melihat list file yang ada di server
<br>
contoh respon :
![respon list](img/client_list.png)
menampilkan list kosong bila tidak ada file dalam server
<br><br>

### download
penggunaan : download [nama_file]
<br>
Mendownload file [nama_file] dari server
<br>
contoh respon :
![respon download](img/client_download.png)
mengembalikan Error jika file request tidak ditemukan di server
<br><br>

### upload
penggunaan : upload [nama_file]
<br>
Mengupload file [nama_file] ke server
<br>
contoh respon :
![respon upload](img/client_upload.png)
Tidak direquest apabila file tidak ada