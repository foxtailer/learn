import random
import asyncio

from aiogram import Bot, types, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import sys; sys.path.append('/home/zoy/vscode')
import deps


multiplication_results = {
    2: [4, 6, 8, 10, 12, 14, 16, 18],
    3: [6, 9, 12, 15, 18, 21, 24, 27],
    4: [8, 12, 16, 20, 24, 28, 32, 36],
    5: [10, 15, 20, 25, 30, 35, 40, 45],
    6: [12, 18, 24, 30, 36, 42, 48, 54],
    7: [14, 21, 28, 35, 42, 49, 56, 63],
    8: [16, 24, 32, 40, 48, 56, 64, 72],
    9: [18, 27, 36, 45, 54, 63, 72, 81],
}

MULTIPLICATION_RESULTS = [4, 6, 8, 9, 10,
                          12, 14, 15, 16, 18,
                          20, 21, 24, 25, 27,
                          28, 30, 32, 35, 36,
                          40, 42, 45, 48, 49,
                          54, 56, 63, 64, 72,
                          81]

TOKEN = deps.T

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def play(msg: types.Message, chat_id=None):
    if msg:
        chat_id = msg.chat.id

    question = f'{random.randint(2, 9)} * {random.randint(2, 9)}'
    answer = eval(question)
    fake_answers = random.sample([x for x in MULTIPLICATION_RESULTS if x != answer], 5)

    for_buttons = []

    for_buttons.append((answer, True))

    for i in fake_answers:
        for_buttons.append((i, False))

    random.shuffle(for_buttons)

    ibtn1 = InlineKeyboardButton(text=f"{for_buttons[0][0]}", callback_data=f"{for_buttons[0][1]}")
    ibtn2 = InlineKeyboardButton(text=f"{for_buttons[1][0]}", callback_data=f"{for_buttons[1][1]}")
    ibtn3 = InlineKeyboardButton(text=f"{for_buttons[2][0]}", callback_data=f"{for_buttons[2][1]}")
    ibtn4 = InlineKeyboardButton(text=f"{for_buttons[3][0]}", callback_data=f"{for_buttons[3][1]}")
    ibtn5 = InlineKeyboardButton(text=f"{for_buttons[4][0]}", callback_data=f"{for_buttons[4][1]}")
    ibtn6 = InlineKeyboardButton(text=f"{for_buttons[5][0]}", callback_data=f"{for_buttons[5][1]}")
    ikb = InlineKeyboardMarkup(inline_keyboard=[[ibtn1,ibtn2,ibtn3],[ibtn4,ibtn5, ibtn6]])
    
    await bot.send_message(chat_id, question, reply_markup=ikb)


@dp.callback_query()
async def choice_callback(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id

    if callback.data == "True":
        await callback.message.answer(text=f"✅")
        await play(None, chat_id)

    elif callback.data == "False": 
        await callback.message.answer(text=f"❌")
        await play(None, chat_id)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    