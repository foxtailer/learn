import asyncio  # кооперативная многозадачность / однопоточный цикл событий 
from util import delay

async def add_one(number):
    print(number + 1)

async def hello_world():
    await delay(1)
    return "Hello World!"

async def main():
    task1 = asyncio.create_task(hello_world())
    task2 = asyncio.create_task(add_one(1))

    await task1  # In this moment all taskd are started

asyncio.run(main())