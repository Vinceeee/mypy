#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 多进程的优点 
# - 避免全局线程锁，进程可控制
# 多进程的缺点
# - 消耗内存，跨进程访问较麻烦
import multiprocessing
from random import randint
import time
from os import getpid

def worker(procnum):
    print 'I am number %d in process %d' % (procnum, getpid())
    time.sleep(3.5)
    return getpid()

def foo(n,queue):
    time.sleep(randint(500,1000)*0.001)
    print(n)
    queue.put(n**2)

def sample_pool():
    pool = multiprocessing.Pool(processes = 5)
    print(pool.map(worker, xrange(5)))# get the result in order

def sample_queue():
    queue = multiprocessing.Queue(maxsize=100)
    result = []
    jobs = []
    for i in xrange(1,25):
        p = multiprocessing.Process(target=foo,args=(i,queue))
        jobs.append(p)
        p.start()

    for p in jobs:
        result.append(queue.get())

    queue.join()

    print result


if __name__ == '__main__':
    sample_queue()
