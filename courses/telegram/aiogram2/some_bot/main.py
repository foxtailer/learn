import asyncio

from aiogram import Bot, Dispatcher

from src.handlers import routers_list

async def main():

    bot = Bot(token='')
    dp = Dispatcher()
    dp.include_routers(*routers_list)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
