import logging
import requests
import os
import threading

class DownloaderClient(threading.Thread):
    def __init__(self,url,tid):
        self.url = url
        self.tid = tid
        self.dir = 'img'
        threading.Thread.__init__(self)

    def run(self):
        if (self.url is None):
            return False
        ff = requests.get(self.url)
        tipe = dict()
        tipe['image/png']='png'
        tipe['image/jpg']='jpg'
        tipe['image/jpeg']='jpg'
        tipe['image/gif']='gif'

        content_type = ff.headers['Content-Type']
        logging.warning(f'{self.tid}:{content_type}')
        if (content_type in list(tipe.keys())):
            namafile = os.path.basename(self.url)
            # ekstensi = tipe[content_type]
            logging.warning(f"{self.tid}:writing {namafile}")
            fp = open(f"{self.dir}/{namafile}","wb")
            fp.write(ff.content)
            fp.close()
        else:
            return False


def main():
    imglist = [ 
                'https://community-cdn-digitalocean-com.global.ssl.fastly.net/assets/tutorials/images/large/python.png',
                'https://loremflickr.com/1024/720/cat.jpg',
                # 'https://sample-videos.com/img/Sample-jpg-image-30mb.jpg',
                # 'https://sample-videos.com/img/Sample-jpg-image-1mb.jpg',
                'https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg',
                'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
                'https://www.google.com/logos/doodles/2020/bulgaria-liberation-day-2020-6753651837108306-2xa.gif']
    threadlist = []
    for img in imglist:
        threader = DownloaderClient(img,len(threadlist))
        threader.start()
        threadlist.append(threader)


if __name__=='__main__':
    main()
    # download_gambar('https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg')
