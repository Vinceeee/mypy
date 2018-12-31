#!/usr/bin/env python
import asyncio
import time


async def hi(msg="Async"):
    from random import randint
    await sleep(randint(4, 5) / randint(10, 20)
                )  # it will be stop until sleep function
    print("Hello {msg}".format(msg=msg))


async def sleep(seconds=10):
    print("wait {}".format(seconds))
    time.sleep(seconds)


async def call_fib(n=10):
    print('*' * 30)
    for i in fib(n):
        print(i, end=" ")
    print()
    print('*' * 30)


def fib(n: int):
    """
    : parm n: 下标
    : return 返回一个从0到n的斐波那契数列生成器
    """
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
    task_manager.run_until_complete(call_fib(150))
    task_manager.run_forever()
#   task_manager.stop()
    if task_manager.is_running():
        print("task_manager还在跑")
        task_manager.stop()
    print("还在跑吗？ -- {}".format(task_manager.is_running()))


if __name__ == '__main__':
    normal_run()
