import urllib.request

def download(url):
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'

    request = urllib.request.Request(url, headers = headers)
    html = urllib.request.urlopen(request).read().decode("utf-8")
    return html