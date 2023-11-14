# encoding=utf8
import asyncio


async def demo():
    print(11)


loop = asyncio.get_event_loop()
loop.run_until_complete(demo())
