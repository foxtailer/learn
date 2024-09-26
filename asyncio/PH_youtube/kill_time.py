import asyncio
from time import time

async def print1(sec):
    await asyncio.sleep(sec)
    print(sec)


async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(1, 16):
            tg.create_task(print1(i))


start = time()
asyncio.run(main())
print(f'Time to run: {time() - start}')
