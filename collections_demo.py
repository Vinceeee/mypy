#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from collections import namedtuple


# can not serialize "set" 
Person = namedtuple("Persion",["name","age","gender","like","schools"])

def encodeJson():
#   p1 = Person("aa","10","G",{"Basketball","Football"}) # could not be formated to json
    p1 = Person("aa","10","G",["Basketball","Football"])
#   p1 = Person("aa","10","G",["Basketball","Football"],{"primary":"NCC"})
#   print(p1._asdict())

    return p1._asdict()

def decodeJson(incoming):
    outgoing = json.dumps(incoming)
    return outgoing

def main():
    incoming = encodeJson()
    outgoing = decodeJson(incoming)
    print(outgoing)

if __name__ == '__main__':
    main()
