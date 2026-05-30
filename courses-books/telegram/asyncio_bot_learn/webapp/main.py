import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters.command import Command

from config import BOT_TOKEN


bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Open Web App",
                web_app=WebAppInfo(url="https://thigh-persecute-studio.ngrok-free.dev")
            )]
        ]
    )
    await message.answer("Open app:", reply_markup=kb)

@dp.message(F.web_app_data)
async def handle_webapp(message: Message):
    await message.answer(message.web_app_data.data)


@dp.message()
async def echo(message: Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
