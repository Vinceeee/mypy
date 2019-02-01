#!/usr/bin/env python3.6

import time
import threading

from functools import wraps

def logFun(func):

    @wraps(func)
    def deco(*args,**kwargs):
        result = func(*args,**kwargs)
        print("{} is completed".format(func.__name__))
        return result
    return deco

@logFun
def countdown(n,sleep_time=1):
    while n > 0:
        n -= 1
        print("countding down ... n is {} now ".format(n))
        time.sleep(sleep_time)

if __name__ == '__main__':
    # can not be terminated by "[C+C]"
    thread = threading.Thread(target=countdown,args=(10,0.4),daemon=True) # deamon is only supported in PY3
    thread2 = threading.Thread(target=countdown,args=(10,0.6))
    thread.start()
    thread2.start()
    
    main_n = 5
    while main_n > 0:
        print("counting down main n ... main n is {} now " .format(main_n))
        time.sleep(1)
        main_n -= 1
    print("Main finished")

    while thread.is_alive or thread2.is_alive:
        print("some threads are still running ...")
        time.sleep(0.5)
