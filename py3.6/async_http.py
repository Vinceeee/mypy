#!/usr/bin/env python
import asyncio
import datetime
from urllib import request, parse

"""
Non-blocking url-open by asyncio
"""

async def openurl(url):
    u = request.urlopen(url,timeout=10)
    print(u.read(1000))
    return u.status

def normal_run():
    # only coroutine task instances , 
    # which need to be triggered in a event_loop
    task1 = openurl("https://www.baidu.com")
    task2 = openurl("https://www.hupu.com")
    task3 = openurl("https://www.google.com") # u never got access :)
    
    tasks = [
        asyncio.ensure_future(task1),
        asyncio.ensure_future(task2),
        asyncio.ensure_future(task3),
        ]
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    for task in tasks:
        print(task.result())

if __name__ == '__main__':
    normal_run()
