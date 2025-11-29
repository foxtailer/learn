import asyncio

from aiogram import Bot, types, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


TOKEN = ""

bot = Bot(TOKEN)
dp = Dispatcher()

ibtn1 = InlineKeyboardButton(text="open",url=r"https://www.google.com/search?client=firefox-b-e&q=aiogram.exceptions.TelegramBadRequest%3A+Telegram+server+says+-+Bad+Request%3A+inline+keyboard+button+URL+%27gggg%27+is+invalid%3A+Wrong+HTTP+URL")
ibtn2 = InlineKeyboardButton(text="open2",url=r"https://www.google.com/search?client=firefox-b-e&q=aiogram.exceptions.TelegramBadRequest%3A+Telegram+server+says+-+Bad+Request%3A+inline+keyboard+button+URL+%27gggg%27+is+invalid%3A+Wrong+HTTP+URL")

ikb = InlineKeyboardMarkup(inline_keyboard=[[ibtn1,ibtn1]])


@dp.message(Command("start"))
async def help_commmand(msg: types.Message):
    await bot.send_message(chat_id=msg.chat.id, text="He-he", reply_markup=ikb)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
