import asyncio
from filelock import FileLock
from loguru import logger

async def main():

    async def coro(msg:str,running_time:int):
        async with FileLock("test.lock", 10):
            await asyncio.sleep(running_time)
            logger.info(f"running : {msg}")

    tasks = []
    for i in range(1, 5):
        tasks.append(asyncio.create_task(coro(f"t{i}", 1)))

    await asyncio.gather(*tasks)

asyncio.run(main())
