import asyncio

async def counter_1():
    n = 0
    while True:
        print(f"{n} second pass!")
        n += 1
        await asyncio.sleep(1)

async def counter_3():
    while True:
        print(f"3 second pass!")
        await asyncio.sleep(3)


async def main():
    task_1 = asyncio.create_task(counter_1())
    task_2 = asyncio.create_task(counter_3())

    await task_1
    await task_2


if __name__ == "__main__":
    asyncio.run(main())