#!/usr/bin/python3.6
# running in Python3
'''
基本爬虫 -- 保存 URL 资源
'''
import time
import os,re
from io import BytesIO
import requests
import threading
from urllib.error import ContentTooShortError

from requests.exceptions import ConnectionError,ConnectTimeout

PAGENAME="http://www.beautylegmm.com"
MAX_RETRY=3

# Save the url resources
def save(url,path):
    url = PAGENAME+url
    path = "."+path
    folder = path.split("/beautyleg-")[0]
    if not os.path.exists(folder):
        os.makedirs(folder)
    try:
        print("%s is retrieving to %s ... " % (url,path))
        if os.path.exists(path):
            return 1

        r = requests.get(url)
        image_stream = BytesIO(r.content)
        with open(path,"wb") as f:
            f.write(image_stream.read())
            
        return 0
    except ConnectionError as err:
        print(E)
        return -1
    except ContentTooShortError as E2:
        print(E2)
        return -1

def getImage(v_url):
    # v_url format : http://www.beautylegmm.com/{MODEL_NAME}/beautyleg-{seq}.html
    pattern = "<img src=\"(/photo/\S*.jpg)\""
    regex = re.compile(pattern)
    r = requests.get(v_url)
    groups = regex.findall(r.text) 
    for each in groups:
        retry = 1
        while retry < MAX_RETRY:
            if save(each,each) >= 0:
                break

    nextPage = re.findall("class=\"next\".*href=\"(\S*)\"",r.text)
#   time.sleep(3) #做人留一线 日后好相见
    if nextPage:
        print("Request for {0}".format(nextPage[0]))
        getImage(nextPage[0])

def searchModelByName(name,page=None):

    url = "http://www.beautylegmm.com/{NAME}/".format(NAME=name)
    pattern = "<a href=\"({URL}beautyleg-(\d+).html)\"".format(URL=url)
    regex_series = re.compile(pattern)
    regex_page = re.compile("class=\"next\".*href=\"(\S*)\"")

    def getModelSeriesList(response):
        return regex_series.findall(response.text)
    
    series_list = []
    page = url

    while True:
        print("Request for {0}".format(page))
        r = requests.get(page)
        series_list.extend(getModelSeriesList(r))
        next_page = regex_page.findall(r.text)
        if not next_page:
            break
        page = next_page[0]
        time.sleep(2) #做人留一线 日后好相见

    return series_list

if __name__ == '__main__':
    s_list = searchModelByName("Anita")
    s_list.reverse()
    from pprint import PrettyPrinter
    p = PrettyPrinter(indent=4)
    for each in s_list:
        getImage(each[0])
