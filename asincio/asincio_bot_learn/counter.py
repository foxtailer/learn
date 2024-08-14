from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


TOKEN = ""

bot = Bot(TOKEN)
dp = Dispatcher()

number = 0

def get_ikb():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Increase',callback_data='_inc'), InlineKeyboardButton(text='Decrease',callback_data='_dec')]
    ])
    return ikb

@dp.message(Command("start"))
async def help_commmand(msg: types.Message):
    await msg.answer(text=f"{number}", reply_markup=get_ikb())

@dp.callback_query(lambda callback_query: callback_query.data.startswith('_'))
async def ikb_handler(callbak):
    global number
    if callbak.data == "_inc":
        number += 1
        await callbak.message.edit_text(f"{number}", reply_markup=get_ikb())
    elif callbak.data == "_dec":
        number -= 1
        await callbak.message.edit_text(f"{number}", reply_markup=get_ikb())


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())