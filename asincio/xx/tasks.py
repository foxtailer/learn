import asyncio
import api

async def main():
    task = asyncio.create_task(
        api.fetch_data()
    )

    task.cancel()
    await asyncio.sleep(1)

    if task.cancelled():
        print(task.cancelled())

    try:
        result = await task
        print(result)
    except asyncio.CancelledError:
        print("CANCELLED: Request was cancelled...")
    except asyncio.TimeoutError:
        print("TIMEOUT: Request took too long...")


if __name__ == '__main__':
    asyncio.run(main())
