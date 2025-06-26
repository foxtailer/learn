import asyncio

from aiogram import Bot, types, Dispatcher
from aiogram.filters.command import Command


bot = Bot('')
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, f"{msg.from_user.id}: {msg.text}")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    