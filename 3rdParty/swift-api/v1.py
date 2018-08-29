#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import requests
import pprint

pretty_print = pprint.PrettyPrinter(indent=4).pprint

def get_info():

    URL="http://127.0.0.1:8080/info"
    resp = requests.get(URL)
    info = resp.json()
    print info
    print info.get("swift")

def account_info():
    account="admin"
    URL="http://127.0.0.1:8080/v1/{}".format(account)
    resp = requests.get(URL)
    print resp.status_code
    
    info = resp.json()
    

if __name__ == '__main__':

    account_info()
