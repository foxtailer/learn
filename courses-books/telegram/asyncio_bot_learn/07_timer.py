import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

TOKEN = ""

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command("settimer"))
async def cmd_settimer(
        message: types.Message,
        command: types.CommandObject
):
    # Если не переданы никакие аргументы, то
    # command.args будет None
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы"
        )
        return
    # Пробуем разделить аргументы на две части по первому встречному пробелу
    try:
        delay_time, text_to_send = command.args.split(" ", maxsplit=1)
    # Если получилось меньше двух частей, вылетит ValueError
    except ValueError:
        await message.answer(
            "Ошибка: неправильный формат команды. Пример:\n"
            "/settimer <time> <message>"
        )
        return
    await message.answer(
        "Таймер добавлен!\n"
        f"Время: {delay_time}\n"
        f"Текст: {text_to_send}"
    )



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())