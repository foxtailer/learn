from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command
from config_reader import config

# Для записей с типом Secret* необходимо 
# вызывать метод get_secret_value(), 
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()


@dp.message()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())