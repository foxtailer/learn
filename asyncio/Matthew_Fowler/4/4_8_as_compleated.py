import sys
import asyncio
import aiohttp

sys.path.append('/home/zoy/git/learn/asyncio/Matthew_Fowler/2')
from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, 'https://www.example.com', 1),
                        fetch_status(session, 'https://www.example.com', 1),
                        fetch_status(session, 'https://www.example.com', 10)]
        for finished_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await finished_task
                print(result)
            except asyncio.TimeoutError:
                print('Произошел тайм-аут!')

        for task in asyncio.tasks.all_tasks():
            print(task)


asyncio.run(main())