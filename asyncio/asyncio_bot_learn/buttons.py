from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command

import sys; sys.path.append('/home/zoy/vscode')
import deps
TOKEN = deps.F


bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="С пюрешкой")],
        [types.KeyboardButton(text="Без пюрешки")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)


@dp.message()
async def handle_order(message: types.Message):
    empty_kb = types.ReplyKeyboardRemove()

    # Check the content of the message and respond accordingly
    if message.text == "С пюрешкой":
        await message.answer("Вы выбрали котлеты с пюрешкой. Спасибо за ваш выбор!", reply_markup=empty_kb)
    elif message.text == "Без пюрешки":
        await message.answer("Вы выбрали котлеты без пюрешки. Спасибо за ваш выбор!", reply_markup=empty_kb)
    else:
        await message.answer("Пожалуйста, выберите один из предложенных вариантов.")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
