#coding=utf-8
# running in Python3
'''
爬东方财富网的股票
基本如下--
id-股票代号
name-股票名
current_price -
update_date -
float -
'''
import os,re
from urllib.request import urlopen
from urllib.error import HTTPError , URLError
from bs4 import BeautifulSoup as BS

class Stock(object):

    def __init__(self,sid):
        self.sid = sid

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

# get the info
def scrap_eastmoney():

    url="http://quote.eastmoney.com/sh600470.html"

    bs_obj = BSGenerator(url).getBSObj()

    # get the body
    bd_obj = bs_obj.div

    obj = bd_obj.find_next_sibling(class_="header-title")

    print(obj.h2.get_text())
    print(obj.b.get_text())

    obj2 = bd_obj.find_next_sibling(class_="qphox layout mb7")
    print(obj2)
    print(obj2.find(id="price9").get_text())
    print(obj2.find(id="km1").get_text())

    # for brother in obj.next_siblings

    # print(bs_obj.div)

if __name__ == '__main__':

    scrap_eastmoney()
