#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing
from random import randint
import time
from os import getpid

def worker(procnum):
    print 'I am number %d in process %d' % (procnum, getpid())
    time.sleep(3.5)
    return getpid()

def foo(n,queue):
    time.sleep(0.3)
    queue.put(n**2)

def sample_pool():
    pool = multiprocessing.Pool(processes = 5)
    print(pool.map(worker, xrange(5)))# get the result in order

def sample_queue():
    queue = multiprocessing.Queue(maxsize=100)
    result = []
    jobs = []
    for i in xrange(1,15):
        p = multiprocessing.Process(target=foo,args=(i,queue))
        jobs.append(p)
        p.start()

    for i in xrange(1,15):
        result.append(queue.get())
        p.join()

    print result


if __name__ == '__main__':
    sample_queue()
