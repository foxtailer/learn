from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command
from aiogram import html
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from aiogram.utils.markdown import hide_link

TOKEN = ""


bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command("hidden_link"))
async def cmd_hidden_link(message: types.Message):
    await message.answer(
        f"{hide_link('https://telegra.ph/file/562a512448876923e28c3.png')}\n"
        f"Документация Telegram: *существует*\n"
        f"Пользователи: *не читают документацию*\n"
        f"Груша:"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())