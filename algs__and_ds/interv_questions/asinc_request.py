import aiohttp
import asyncio
import json

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch(session, url))
        return await asyncio.gather(*tasks)

async def main():
    base_url = "https://jsonplaceholder.typicode.com/posts/"
    urls = [f"{base_url}{i}" for i in range(1, 11)]

    results = await fetch_all(urls)

    with open('result.json', 'w') as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    asyncio.run(main())