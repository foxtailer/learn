import api
import asyncio

async def send_data(to: str):
    print(f"Sending data to {to}...")
    await asyncio.sleep(2)
    print(f"Data sent to {to}!")

async def main():
    data = await api.fetch_data()
    print("Data", data)

    await asyncio.gather(send_data("Mario"), send_data("Luigi"))


if __name__ == "__main__":
    asyncio.run(main())
    print("@")