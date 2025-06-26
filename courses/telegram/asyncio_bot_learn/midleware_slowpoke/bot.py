import asyncio

from aiogram import Bot, Dispatcher

from handler import router1, router2
from midlware import SlowpokeMiddleware


bot = Bot('')
dp = Dispatcher()
router1.message.middleware(SlowpokeMiddleware(sleep_sec=5))
router2.message.middleware(SlowpokeMiddleware(sleep_sec=10))
dp.include_router(router1)
dp.include_router(router2)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())