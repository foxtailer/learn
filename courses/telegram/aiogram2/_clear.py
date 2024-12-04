from aiogram import Bot, Dispatcher
import asyncio

TOKEN = ""

bot = Bot(TOKEN)
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())