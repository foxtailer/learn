from aiogram import Bot, types, Dispatcher
import asyncio


bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, f"{msg.from_user.id}: {msg.text}")

# dp.message.register(cmd_test2, Command("test2"))

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    