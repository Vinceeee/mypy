#!/usr/bin/env python3.6
# coding=utf8

import six
import time
import threading

if six.PY2:
    import Queue # PY2
    share_q = Queue.Queue()
elif six.PY3:
    from queue import Queue
    share_q = Queue(maxsize=3)

def randomeSleep(n,m):
    ''' n,m indicate the sleep range '''
    ''' process will be stopped between n to m seconds '''
    from random import randint,random
    a = round(randint(n,m-1)+random(),1)
    print("Sleep {0} seconds".format(a))
    time.sleep(a)

sleep = lambda : randomeSleep(1,3)
obj = id("product")

def productor():
    while True:
        try:
            __import__('ipdb').set_trace()
            if share_q.full(): 
                print("爆咯爆咯")
                break
            share_q.put(obj)
            print("Produce an obj")
            sleep()
            print("queue size now :{}".format(share_q.qsize()))
        except Exception as excp:
            print(excp)
            break


if __name__ == '__main__':

    t = threading.Thread(target=productor)
    t.start()

