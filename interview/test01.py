#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
坑爹的默认参数
"""
def f(a,c=[]):
    c.append(a)
    return c

def main():
    lst = range(10)
    lst = f(10,lst)
    lst = f(11)
    lst = f(12)

if __name__ == '__main__':
    main()
