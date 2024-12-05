import asyncio


async def count(counter):
    print(f'Items in list: {len(counter)}')

    while True:
        await asyncio.sleep(1/1000)
        counter.append(1)

        