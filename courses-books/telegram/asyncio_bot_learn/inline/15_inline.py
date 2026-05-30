import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart

from handlers import common, inline_mode, save_images, save_text
    

bot = Bot('7823944712:AAFXzyloveTSPp1fCILkyi3WVX5K4-3oofI')
dp = Dispatcher()
dp.include_routers(
    save_images.router,
    save_text.router,
    common.router,
    inline_mode.router,
)


@dp.message(CommandStart())
async def command_start_handler(message) -> None:
    await message.answer("Hello!")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
