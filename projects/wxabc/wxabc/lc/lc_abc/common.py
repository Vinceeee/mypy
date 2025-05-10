import asyncio
from loguru import logger


async def main():
    for _i in range(10):
        await asyncio.sleep(0.1)
        logger.info(f"print out {_i}")


asyncio.run(main())
