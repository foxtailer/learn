import asyncio

async def count(counter: list):
    print(f'Notes in list: {len(counter)}')

    while True:
        await asyncio.sleep(1 / 1000)
        counter.append(1)


async def print_every_one_sec(counter):
    while True:
        await asyncio.sleep(1)
        print('- 1 sec pass.'
              f'Notes in list: {len(counter)}')
        

async def print_every_5_sec():
    while True:
        await asyncio.sleep(5)
        print('---- 5 sec pass.')
        

async def print_every_10_sec():
    while True:
        await asyncio.sleep(10)
        print('-------- 10 sec pass.')


# 1 way
# async def main():
#     counter = list()

#     c = count(counter)
#     p1 = print_every_one_sec(counter)
#     p5 = print_every_5_sec()
#     p10 = print_every_10_sec()

#     asyncio.create_task(c)
#     asyncio.create_task(p1)
#     asyncio.create_task(p5)
#     await p10


# 2 way
async def main():
    counter = list()

    tasks = [
        count(counter),
        print_every_one_sec(counter),
        print_every_5_sec(),
        print_every_10_sec(),
    ]

    await asyncio.gather(*tasks)

asyncio.run(main())

async def count(counter):
    print(f'Items in list: {len(counter)}')

    while True:
        await asyncio.sleep(1/1000)
        counter.append(1)