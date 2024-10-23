from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command
import string

import sys; sys.path.append('/home/zoy/vscode')
import deps

TOKEN = deps.T

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message()
async def echo_message(msg: types.Message):
    #await bot.send_message(msg.from_user.id, msg.text)
    await bot.send_message(msg.from_user.id, f"{msg.from_user.id}")
    await msg.reply(string.ascii_letters)
    await msg.delete()

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    