# encoding=utf8
import asyncio


async def demo():
    print(11)


async def demo2():
    print(12)


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(demo(), demo2()))
