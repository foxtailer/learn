import asyncio

from aiogram import Bot, Dispatcher

from midlware import UserInternalIdMiddleware, HappyMonthMiddleware
from handlers import router


async def main():

    bot = Bot(token='')
    dp = Dispatcher()
    dp.update.outer_middleware(UserInternalIdMiddleware())
    router.message.middleware(HappyMonthMiddleware())
    dp.include_routers(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
