#!/usr/bin/env python
import asyncio
import time

async def hi(msg="Async"):
    from random import randint
    await sleep(randint(4,5) / randint(10,20)) # it will be stop until sleep function
    print("Hello {msg}".format(msg=msg))

async def sleep(seconds=10):
    print("wait {}".format(seconds))
    time.sleep(seconds)

async def call_fib(n=10):
    for i in fib(n):
        print(i,end=" ")
    print()

def fib(n:int):
    from collections import deque
    q = deque(maxlen=2)

    for i in range(n):
        if i <= 0:
            continue
        if i <= 2:
            yield 1
            q.append(1)
        else:
            q.append(sum(q))
            yield q[-1]

def normal_run():
    """docstring for normal_run"""
    task_manager = asyncio.get_event_loop()
    task_manager.run_until_complete(call_fib())
    task_manager.run_until_complete(call_fib(50))
    task_manager.stop()

if __name__ == '__main__':
    normal_run()
