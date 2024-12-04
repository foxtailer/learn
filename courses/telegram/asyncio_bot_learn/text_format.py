from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command


TOKEN = ""


bot = Bot(TOKEN)
dp = Dispatcher()


# Если не указать фильтр F.text, 
# то хэндлер сработает даже на картинку с подписью /test,
# но пока нам это не важно и рассматриваем только текстовые сообщения
@dp.message(Command("test"))
async def any_message(message: types.Message):
    await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
    await message.answer("Hello, *world*\!", parse_mode="MarkdownV2")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())