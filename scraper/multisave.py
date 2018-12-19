#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from io import BytesIO
from urllib.parse import urlparse
import concurrent.futures

import requests
from requests.exceptions import ConnectionError,ConnectTimeout

import logging
ROOTPATH = "/tmp/BL"

def mylogger():
    LOGGERNAME = os.path.join(".","BLMM_scrapper.log")
    logger = logging.getLogger()
    handler = logging.FileHandler(LOGGERNAME)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt="[%(asctime)s](%(levelname)s) - %(message)s ",datefmt='%m/%d/%Y %H:%M:%S') # set datefmt
    handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.INFO)
    return logger

logger = mylogger()

def save_res(url,fn):

    logger.info("retrieving {} from {}".format(fn,url))
    try:
        r = requests.get(url)
        
        if r.status_code >= 400:
            logger.info("Failed to retrieved {} , status code {}".format(url,r.status_code))
            return r.status_code

        content_length = int(r.headers.get("Content-Length","0"))

        if content_length < 10000:
            logger.info("{} is too small , skipped .".format(url))
            return -3 

        with open(fn,"wb") as f:
            f.write(BytesIO(r.content).read())

    except ConnectionError as e1:
        logger.warn(e1)
        return -1
    except Exception as e2:
        logger.warn(e2)
        return -1

    logger.info("Successfully retrievied {} from {}".format(fn,url))
    return 200

def main():


    websites = []
    year = "2018"
    seires = "1627"
    total = 57
#   web_pattern = "http://www.beautylegmm.com/photo/beautyleg/2015/1169/beautyleg-1169-00{:02}.jpg"
    web_pattern = "http://www.beautylegmm.com/photo/beautyleg/{YEAR}/{SEIRES}/beautyleg-{SEIRES}-00{IDX:02}.jpg"

    for i in range(1,total):
        websites.append(web_pattern.format(YEAR=year,SEIRES=seires,IDX=i))

    uflist = []
    for url in websites:
        fn = os.path.join(ROOTPATH,seires,os.path.basename(urlparse(url).path))
        save_path = os.path.dirname(fn)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        uflist.append((url,fn))

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
        results = {pool.submit(save_res,url,fn):url for url,fn in uflist }
    
if __name__ == '__main__':
    main()
