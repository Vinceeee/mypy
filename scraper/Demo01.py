# use BeautifulSoup to interpr a html
from urllib.request import urlopen
from urllib.error import HTTPError , URLError
from bs4 import BeautifulSoup as BS

class BSGenerator(object):
    def __init__(self,url):
        self.url = url
    def getBSObj(self):
        try:
            html = urlopen(self.url)
        except (HTTPError,URLError) as E:
            raise E
            return None
        try:
            bsObj = BS(html.read(),"lxml")
        except AttributeError as E2:
            return None
        return bsObj
    def setUrl(self,url):
        self.url = url


def NaviTree(BSObj):
    for child in BSObj.find("table",{"id":"id84"}).children:
        print(child)



if __name__ == '__main__':
    # url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html"
    url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html"
    generator = BSGenerator(url)
    bsObj = generator.getBSObj()

    NaviTree(bsObj)

    exit()

    NameList = bsObj.findAll({"h1","h2"})
    for name in NameList:
        # print(name.get_text())
        print(name)
