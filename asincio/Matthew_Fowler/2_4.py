import asyncio

async def add_one(num: int)->int:
    return num+1

async def main():
    step_one = await add_one(1)
    step_too = await add_one(step_one)

    print(step_too)

asyncio.run(main())
