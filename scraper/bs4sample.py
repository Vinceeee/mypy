import requests
from bs4 import BeautifulSoup

"""
requests 与 bs4 的一些用例
"""

if __name__ == '__main__':
    html = '''
    <html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
    '''
    URL = "http://docs.python-requests.org/zh_CN/latest/user/quickstart.html"
    html = requests.get(URL)
    bs = BeautifulSoup(html.content,'html.parser') 
    # print(bs.prettify()) 
    print("get all the hyperlinks for this page")
    for a in bs.find_all('a'):
        print(a.get('href'))

    print("get all the tags by re for this page")
    import re
    bs_body = bs.body
    for e in bs_body.find_all(id=True):
        print("{0} -- id {1}".format(e.name,e.get('id')))
