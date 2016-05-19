import urllib.request

class Download_image():

    def __init__(self):
        self._num = 798

    def download(self, url):
        headers = {}
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"

        req = urllib.request.Request(url, headers = headers)
        image = urllib.request.urlopen(req).read()

        try:
            jpg = url.split(".")[-1]
            f = open(str(self._num) + "." + jpg, 'wb')
            f.write(image)
            f.close()
        except:
            pass

        self._num += 1

