import asyncio
import functools
import time
from typing import Callable, Any
from aiohttp import ClientSession


async def delay(delay_second: int) -> int:
    print(f'sleeping for {delay_second} second(s)')
    await asyncio.sleep(delay_second)
    print(f'finished sleeping for {delay_second} second(s)')
    return delay_second


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'выполняется {func} с аргументами {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func} завершилась за {total:.4f} с')
        return wrapped
    return wrapper


async def fetch_status(session: ClientSession, url: str, delay = 0) -> int:
    await asyncio.sleep(delay)
    
    async with session.get(url) as result:
        return result.status
