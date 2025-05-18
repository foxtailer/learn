import asyncio

from aiogram import Bot, types, Dispatcher
from aiogram.filters.command import Command


TOKEN = ""


bot = Bot(TOKEN)
dp = Dispatcher()




async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())