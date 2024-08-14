from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command
import string

TOKEN = ""


bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
#####################################
      


#####################################
async def main():
    await dp.start_polling(bot, on_startup=cmd_start)


if __name__ == '__main__':
    asyncio.run(main())