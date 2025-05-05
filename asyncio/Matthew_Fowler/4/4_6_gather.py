import asyncio
import sys
import aiohttp
from aiohttp import ClientSession

sys.path.append('/home/zoy/git/learn/asyncio/Matthew_Fowler/2')
from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]

        '''
        gather принимает последовательность допускающих ожидание объектов и запускает их
        конкурентно всего в одной строке кода. Если среди объектов есть со-
        программа, то gather автоматически обертывает ее задачей, чтобы
        гарантировать конкурентное выполнение.
        '''
        status_codes = await asyncio.gather(*requests)
        '''
        asyncio.gather возвращает объект, допускающий ожидание. Если
        использовать его в выражении await, то выполнение будет приоста-
        новлено, пока не завершатся все переданные объекты. А когда это
        произойдет, asyncio.gather вернет список результатов работы.
        '''
        print(status_codes)


asyncio.run(main())