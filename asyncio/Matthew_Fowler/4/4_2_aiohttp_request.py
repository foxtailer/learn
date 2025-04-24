import sys
import asyncio

import aiohttp
from aiohttp import ClientSession

# Сеанс можно рассматривать как создание
# нового окна браузера. Внутри сеанса хранится много открытых подключений, их можно при
# необходимости использовать повторно. Это называется пулом под-
# ключений и играет важную роль в производительности приложений
# на базе aiohttp.

'''по умолчанию в сеансе ClientSession можно создать
не более 100 подключений, что дает неявную верхнюю границу коли-
чества конкурентных веб-запросов. Чтобы изменить этот предел, мож
но создать экземпляр класса TCPConnector, входящего в состав aiohttp,
указав максимальное число подключений, и передать его конструкто-
ру ClientSession.'''

sys.path.append('/home/zoy/git/learn/asyncio/Matthew_Fowler/2')
from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        status = await fetch_status(session, url)
        print(f'Состояние для {url} было равно {status}')


asyncio.run(main())
