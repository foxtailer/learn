from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command
from aiogram.filters import CommandObject
from aiogram import html

TOKEN = ""


bot = Bot(TOKEN)
dp = Dispatcher()

async def on_startup(_):
    print("ololololo")

    
@dp.message(Command("name"))
async def cmd_name(message, command):
    if command.args:
        #await message.answer(f"Привет, <b>{command.args}</b>", parse_mode="HTML")
        await message.answer(f"Привет, {html.bold(html.quote(command.args))}", parse_mode="HTML")
        await message.answer(f"Привет, <b>{command.args}</b>", parse_mode="HTML")
        await bot.send_message(message.from_user.id, f"Привет, <b>{command.args}</b>", parse_mode="HTML")
    else:
        await message.answer("Пожалуйста, укажи своё имя после команды /name!")


async def main():
    #await dp.startup.register(on_startup)
    await dp.start_polling(bot, on_startup=on_startup)


if __name__ == '__main__':
    asyncio.run(main())