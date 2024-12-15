from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command
import string

TOKEN = ""


bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message()
async def echo_message(msg: types.Message):
    # msg.text - text without formating
    # message.html_text / message.md_text can be used
    await bot.send_message(msg.from_user.id, msg.text)
    await msg.reply(string.ascii_letters)
    await msg.delete()

#  Another way of register hendler, without decorator. Dont work(
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")
dp.message.register(cmd_test2, Command("test2"))

async def main():
    await dp.start_polling(bot, on_startup=cmd_start)


if __name__ == '__main__':
    asyncio.run(main())