import asyncio

async def gg(n):
    await asyncio.sleep(n)
    print(f"gg{n}")

print(gg(4))