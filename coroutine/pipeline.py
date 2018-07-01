#!/usr/bin/env python
# coding=utf-8
import os
import time
import traceback

def coroutine(func):
    def deco(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.__next__() # in python2 , generator has next() for iterate , but in python3 , it has been replaced by __next__()
        return cr
    return deco

@coroutine
def grep(pattern):
    print("looking for %s" % pattern)
    try:
        while True:
            line = (yield)
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("Exit ...")

@coroutine
def printer():
    while True:
        line = (yield)
        print(line)

def tail_f(fq,target):
    # implement "tail -f"
    fq.seek(0,2)
    while True:
        line = fq.readline()
        if not line:
            time.sleep(0.2)
            continue
        target.send(line)

def write_f(fq):
    while True:
        try:
            fq.write(r"{now}:aaa ".format(now=time.time()))
            fq.write(os.linesep)
            time.sleep(0.1)
            fq.flush()
        except Exception:
            print(traceback.format_exc())
            break

def main():
    g = grep("celine")
    # g.next()
    g.send("where is you?")
    g.send("here here")
    g.send("celine is here")
    
def example_tail_f():
    tail_f(open(r'e:\test.txt'),printer())

if __name__ == '__main__':
    f = open(r'e:\test.txt','a+')
    write_f(f)