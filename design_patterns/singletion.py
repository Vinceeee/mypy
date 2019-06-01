#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
可继承单例
需要指定类常量字典 _SINGLE
每当创建一个类,则更新到字典里面
"""
class SingleDog(object):
    _SINGLE = {}
    def __new__(cls,*args,**kwargs):
        if cls not in cls._SINGLE:
            cls._SINGLE[cls] = object.__new__(cls, *args, **kwargs)
        return cls._SINGLE[cls]

    def __init__(self):
        pass

    def __str__(self):
        return "<SingleDog>{}".format(id(self))

class SuperSingleDog(SingleDog):
    def __str__(self):
        return "<SuperSingleDog>{}".format(id(self))


if __name__ == "__main__":
    dog1 = SingleDog()
    dog2 = SingleDog()
    print(id(dog1) == id(dog2))
    superdog = SuperSingleDog()
    superdog2 = SuperSingleDog()
    print(id(dog1) == id(superdog))
    print(id(superdog2) == id(superdog))
