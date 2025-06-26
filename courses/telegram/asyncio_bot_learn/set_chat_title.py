import asyncio
from aiogram import Bot, types, Dispatcher


TOKEN = ''

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message()
async def set_chat_title(msg: types.Message):
    # Can not change private chat title
    # Bot must be admin of group
    message = await bot.set_chat_title(chat_id=msg.chat.id,
                                       title='New Title')

    print(message)  # True


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())