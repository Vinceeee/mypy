#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading
import Queue


Thread = threading.Thread
class MyThread(threading.Thread):
    """docstring for MyThread"""
    def __init__(self, pool):
        super(MyThread, self).__init__()
        self.pool = pool

    def run(self):
        pass 
        
class ThreadPool(object):

    def __init__(self, pool_size = 10):
        self.pool = Queue(pool_size)
        
    def put(self,target,args=()):
        t =  Thread(target=target,args=args)
        
    def start(self):
        __import__('pdb').set_trace()
        print(len(self.pool))
        pass

    def join(self):
        self.pool.join()


def foo():
    time.sleep(1)
    print("i m foo")

def bar(n):
    if isinstance(n,int):
        print(n**2)
    else:
        print(n)

def fib(n):
    if n in (1,2):
        return 1
    if n > 2:
        return fib(n-1) + fib(n-2)


def main():
    pool = ThreadPool()
    pool.put(target=foo)
    pool.put(target=foo)
    

if __name__ == '__main__':
    main()
