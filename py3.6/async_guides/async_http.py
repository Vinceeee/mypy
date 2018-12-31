#!/usr/bin/env python
import asyncio
from random import randint
from urllib import request
"""
Non-blocking url-open by asyncio
"""


async def openurl(url):
    print("opening {} ".format(url))
    u = request.urlopen(url, timeout=10)
    print(u.read())
    st = randint(2, 3)
    await asyncio.sleep(st)
    return u.status


def normal_run():
    # only coroutine task instances ,
    # which need to be triggered in a event_loop

    loop = asyncio.get_event_loop()
    while True:
        task1 = openurl("http://localhost:12345")
        task2 = openurl("http://localhost:12345/home")
        tasks = [asyncio.ensure_future(task1), asyncio.ensure_future(task2)]
#       loop.run_until_complete(asyncio.wait(tasks))
        loop.run_until_complete(task1)

#       for task in tasks:
#           print(task.result())


if __name__ == '__main__':
    normal_run()
