from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command
from datetime import datetime

import sys; sys.path.append('/home/zoy/vscode')
import deps
TOKEN = deps.F


bot = Bot(TOKEN)
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
mylist = [2,4,5]


@dp.message(Command("add_to_list"))
async def cmd_add_to_list(message: types.Message, mylist: list): 
    mylist.append(7)
    await message.answer("Добавлено число 7")


@dp.message(Command("show_list"))
async def cmd_show_list(message: types.Message, mylist: list):
    await message.answer(f"Ваш список: {mylist}")


@dp.message(Command("info"))
async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"Бот запущен {started_at}")
    

async def main():
    await dp.start_polling(bot, mylist=mylist)


if __name__ == '__main__':
    asyncio.run(main())