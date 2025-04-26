import asyncio
import logging
import aiohttp
import sys

sys.path.append('/home/zoy/git/learn/asyncio/Matthew_Fowler/2')
from util import async_timed, fetch_status


async def main():
    async with aiohttp.ClientSession() as session:
        good_request = fetch_status(session, 'https://www.example.com')
        bad_request = fetch_status(session, 'python://bad')

        fetchers = [asyncio.create_task(good_request),
        asyncio.create_task(bad_request)]

        done, pending = await asyncio.wait(fetchers)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            # result = await done_task возбудит исключение
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("При выполнении запроса возникло исключение",
                exc_info=done_task.exception())

        # get done and pending after first exeptions
        # fetchers = \
        #     [asyncio.create_task(fetch_status(session, 'python://bad.com')),
        #     asyncio.create_task(fetch_status(session, 'https://www.example.com', delay=3)),
        #     asyncio.create_task(fetch_status(session, 'https://www.example.com', delay=3))]
        
        # done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)
        # print(f'Число завершившихся задач: {len(done)}')
        # print(f'Число ожидающих задач: {len(pending)}')
        # for done_task in done:
        #     if done_task.exception() is None:
        #         print(done_task.result())
        # else:
        #     logging.error("При выполнении запроса возникло исключение", exc_info=done_task.exception())

        # for pending_task in pending:
        #     pending_task.cancel()


asyncio.run(main())