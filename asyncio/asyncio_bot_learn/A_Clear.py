from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command
from aiogram import html
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile

TOKEN = ""


bot = Bot(TOKEN)
dp = Dispatcher()




async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())