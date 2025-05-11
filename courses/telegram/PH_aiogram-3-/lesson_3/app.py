import asyncio
import os

from dotenv import find_dotenv, load_dotenv
from aiogram import Bot, Dispatcher
from handlers.user_private import user_private_router


ALLOWED_UPDATES = ['message, edited_message']

load_dotenv(find_dotenv())
token = os.getenv('TOKEN')

bot = Bot(token)
dp = Dispatcher()
dp.include_router(user_private_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())
