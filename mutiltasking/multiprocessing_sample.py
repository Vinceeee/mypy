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

def run(instance,func_name):
    """
    这特么蛋碎的东西
    一定要最顶层才能够被pickled
    不然就不能执行对象方法
    """
    func = getattr(instance,func_name)
    func()
    
class BadGirl(object):
    def __init__(self):
        pass

    def skr(self):
        print(time.time())
        print(u"这个没混直接发")
        time.sleep(2.3)

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

def main():

    pool = multiprocessing.Pool(processes = 3)
    for i in xrange(10):
        pool.apply_async(run,args=(BadGirl(),"skr"))

    pool.close()
    pool.join()
    

if __name__ == '__main__':
    main()
