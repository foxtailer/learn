import asyncio

from aiogram import Bot, types, Dispatcher
from aiogram import html
from aiogram import F


TOKEN = ""

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(F.text)
async def extract_data(message: types.Message):
    data = {
        "url": "<N/A>",
        "email": "<N/A>",
        "code": "<N/A>"
    }
    entities = message.entities or []

    for item in entities:
        if item.type in data.keys():
            # Неправильно
            # data[item.type] = message.text[item.offset : item.offset+item.length]
            # Правильно
            data[item.type] = item.extract_from(message.text)
            
    await message.reply(
        "Вот что я нашёл:\n"
        f"URL: {html.quote(data['url'])}\n"
        f"E-mail: {html.quote(data['email'])}\n"
        f"Пароль: {html.quote(data['code'])}"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())