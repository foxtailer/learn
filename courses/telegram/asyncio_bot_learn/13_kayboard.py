from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

TOKEN = ""


bot = Bot(TOKEN)
dp = Dispatcher()

# start_btn = KeyboardButton(text="/start")
# help_btn = KeyboardButton(text="/help")
# img_btn = KeyboardButton(text="/img")
# kb = ReplyKeyboardMarkup(keyboard=[[img_btn, help_btn], [start_btn]], resize_keyboard=True, one_time_keyboard=True)

b1 = KeyboardButton(text="1")
b2 = KeyboardButton(text="2")
b3 = KeyboardButton(text="3")
b4 = KeyboardButton(text="4")
b5 = KeyboardButton(text="5")
b6 = KeyboardButton(text="6")
b7 = KeyboardButton(text="7")

b8 = KeyboardButton(text="8")
b9 = KeyboardButton(text="9")
b10 = KeyboardButton(text="10")
b11 = KeyboardButton(text="11")
b12 = KeyboardButton(text="12")
b13 = KeyboardButton(text="13")
b14 = KeyboardButton(text="14")

b15 = KeyboardButton(text="15")
b16 = KeyboardButton(text="16")
b17 = KeyboardButton(text="17")
b18 = KeyboardButton(text="18")
b19 = KeyboardButton(text="19")
b20 = KeyboardButton(text="20")
b21 = KeyboardButton(text="21")

b22 = KeyboardButton(text="22")
b23 = KeyboardButton(text="23")
b24 = KeyboardButton(text="24")
b25 = KeyboardButton(text="25")
b26 = KeyboardButton(text="26")
b27 = KeyboardButton(text="27")
b28 = KeyboardButton(text="28")

b29 = KeyboardButton(text="29")
b30 = KeyboardButton(text="30")
b31 = KeyboardButton(text="31")
b32 = KeyboardButton(text="32")
b33 = KeyboardButton(text="33")
b34 = KeyboardButton(text="34")
b35 = KeyboardButton(text="35")


@dp.message(Command("start"))
async def start_commmand(msg: types.Message):
    await bot.send_message(msg.chat.id, "He-he", reply_markup=kb)

@dp.message(Command("help"))
async def help_commmand(msg: types.Message):
    await bot.send_message(msg.chat.id, "He-he", reply_markup=ReplyKeyboardRemove())

@dp.message(Command("img"))
async def img_commmand(msg: types.Message):
    await bot.send_message(msg.chat.id, "He-he", reply_markup=ReplyKeyboardRemove())

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())