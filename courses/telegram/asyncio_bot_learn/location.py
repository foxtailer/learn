import asyncio

from aiogram import Bot, types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters.command import Command

import sys; sys.path.append('/home/zoy/vscode')
import deps


TOKEN = deps.T

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: types.Message):
    location_button = KeyboardButton(text='Share your location', request_location=True)
    keyboard = ReplyKeyboardMarkup(keyboard=[[location_button]], resize_keyboard=True)

    await message.answer("Please share your location:", reply_markup=keyboard)

# Handler to receive location data
@dp.message()
async def handle_location(message: types.Message):
    if message.location:
        latitude = message.location.latitude
        longitude = message.location.longitude
        await message.reply(f"Your location is:\nLatitude: {latitude}\nLongitude: {longitude}")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    