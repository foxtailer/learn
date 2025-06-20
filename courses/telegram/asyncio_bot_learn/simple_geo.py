import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


TOKEN = ""

bot = Bot(TOKEN,
          default=DefaultBotProperties(
              parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    btn = types.KeyboardButton(text="Отправить.", request_location=True)
    rkb = types.ReplyKeyboardMarkup(keyboard=[[btn]], resize_keyboard=True)

    await message.answer("Welcome to GEO_bot.",
        reply_markup=rkb
    )


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
