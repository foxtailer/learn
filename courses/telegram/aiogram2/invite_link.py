import asyncio
from aiogram import Bot, types, Dispatcher


TOKEN = ''

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message()
async def invite_link_message(msg: types.Message):
    inv_link = await bot.export_chat_invite_link(chat_id=msg.chat.id)

    await bot.send_message(chat_id=msg.chat.id,
                                     text=inv_link)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
