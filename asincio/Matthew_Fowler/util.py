import asyncio

async def delay(delay_second: int) -> int:
    print(f'sleeping for {delay_second} second(s)')
    await asyncio.sleep(delay_second)
    print(f'finished sleeping for {delay_second} second(s)')
    return delay_second