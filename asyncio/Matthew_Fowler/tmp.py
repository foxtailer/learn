import asyncio


async def fu():
    await asyncio.sleep(10)
    print('Fu - done')

async def fufu():
    print('Fufu - done')

async def main():
    task = asyncio.create_task(fu())
    task2 = asyncio.create_task(fufu())

    await task
    await fufu()


asyncio.run(main())
