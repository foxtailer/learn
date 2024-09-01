import asyncio
from util import delay

async def add_one(number):
    return number + 1

async def hello_world():
    await delay(1)
    return "Hello World!"

async def main():
    message = await hello_world()
    one_plus_one = await add_one(3)
    print(one_plus_one)
    print(message)

asyncio.run(main())