import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


TOKEN = ""

bot = Bot(TOKEN,
          default=DefaultBotProperties(
              parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
