import sys
import asyncio
import aiohttp

sys.path.append('/home/zoy/git/learn/asyncio/Matthew_Fowler/2')
from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetches = \
            [asyncio.create_task(fetch_status(session, 'https://example.com')),
             asyncio.create_task(fetch_status(session, 'https://example.com'))]

        # вернет управление, когда все
        # запросы завершатся, и мы получим два множества: завершившиеся
        # задачи и еще работающие задачи.
        done, pending = await asyncio.wait(fetches)

        print(f'Number of finished tasks: {len(done)}')
        print(f'Number of waiting tasks: {len(pending)}')
    
        for done_task in done:
            print(await done_task)

asyncio.run(main())