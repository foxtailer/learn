from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command
from aiogram import html
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile

TOKEN = ""


dp = Dispatcher()
bot = Bot(TOKEN)

@dp.message(Command("give"))
async def give_commond(msg: types.Message, bot):
    await bot.send_sticker(msg.from_user.id, sticker='CAACAgIAAxUAAWUv-fYPmNiUPDa4Jut0vZhrDjjXAAIoAAMNttIZ7BnFlMNiInkwBA')
    await msg.delete()

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())