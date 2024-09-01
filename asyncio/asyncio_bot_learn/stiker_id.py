from aiogram import Bot, Dispatcher, types
import asyncio

bot = Bot("")
dp = Dispatcher()

@dp.message()
async def stiker_id(msg: types.Message):
    await msg.answer(msg.sticker.file_id)

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
