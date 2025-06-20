import asyncio

from aiogram import Bot, types, Dispatcher
from aiogram.filters.command import Command



bot = Bot('')
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="С пюрешкой")],
        [types.KeyboardButton(text="Без пюрешки")],
        [types.KeyboardButton(text="C макарошками")],
        [types.KeyboardButton(text="С хлебушком")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)


@dp.message(Command("start3"))
async def cmd_start3(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="С пюрешкой"),
            types.KeyboardButton(text="Без пюрешки")
        ],
        [
            types.KeyboardButton(text="C макарошками"),
            types.KeyboardButton(text="С хлебушком")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Выберите способ подачи",
                                         one_time_keyboard=True)
    
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)


@dp.message()
async def handle_order(message: types.Message):
    empty_kb = types.ReplyKeyboardRemove()

    # Check the content of the message and respond accordingly
    if message.text == "С пюрешкой":
        await message.answer("Вы выбрали котлеты с пюрешкой. Спасибо за ваш выбор!", reply_markup=empty_kb)
    elif message.text == "Без пюрешки":
        await message.answer("Вы выбрали котлеты без пюрешки. Спасибо за ваш выбор!", reply_markup=empty_kb)
    else:
        await message.answer("Пожалуйста, выберите один из предложенных вариантов.")


# from aiogram import F

# @dp.message(F.text.lower() == "с пюрешкой")
# async def with_puree(message: types.Message):
#     await message.reply("Отличный выбор!")

# @dp.message(F.text.lower() == "без пюрешки")
# async def without_puree(message: types.Message):
#     await message.reply("Так невкусно!")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
