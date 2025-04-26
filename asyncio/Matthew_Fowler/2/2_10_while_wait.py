import asyncio
from util import delay

async def hello_every_second():
    #for _ in range(4):
    while True:
        await asyncio.sleep(1)
        print("I'm running other code while I'm waiting")

async def main():
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(5))
    await asyncio.wait_for(hello_every_second(), timeout=10)
    print(':P')
    # await first_delay
    # await second_delay

asyncio.run(main())