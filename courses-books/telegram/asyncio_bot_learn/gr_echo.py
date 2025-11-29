from aiogram import Bot, types, Dispatcher
import asyncio


TOKEN = ""


bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message()
async def echo_message(msg: types.Message):
    #await msg.answer(msg.text)
    await bot.send_message(msg.chat.id, msg.text)
    await bot.send_location(msg.chat.id, latitude=55, longitude=66)
    await msg.delete()


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())