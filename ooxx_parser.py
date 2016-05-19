import re

def parse(html):
    print("__________________________________________________", html[:90])
    pa = re.compile(r'img src="(.*?)".*?/p', re.S)
    items = pa.findall(html)
    urls = []

    for item in items:

        urls.append(item)
    urls.pop()
    return urls
