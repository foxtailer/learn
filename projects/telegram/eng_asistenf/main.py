from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import bot_functions
import random
import sqlite3

import sys; sys.path.append('/home/zoy/vscode')
import deps

bot = Bot(deps.T)
dp = Dispatcher()

import json
import codecs


script_dir = bot_functions.find_path()
show_msg_store = {}

"""
select_day - Select day you want to practice
test - Test throw selected day
test10 - Test with random 10 words
examples - Test with examples of selected day
examples10 - Test with examples of random words
sentense - Guess wond in sentense based on your words
shaffle - Try to guess shaffled word
get_example - Give 5 sentence with word
show - Show dictionary
add - Add new words in dict
del - Deleate word/words
start - Start bot
help - Help/Info
"""


@dp.message(Command("help"))
async def help_commmand(msg: types.Message):
    message = """
Bot can hold your dictionary and play games with you based on words in this dictionary.

<code>1) Cat:Кот (My beautiful cat.).\n2) Dog:Собака (Wery big dog.).</code>

(Слово,Перевод,Пример)
...like this:)

Команда:
<code>/add</code> <i>Help,Помощь,I need help.</i>
Добавит в словарь новую строку:
<code>3) Help:Помощь (I need help.)</code>

Запятых в предложении примере быть<b>не</b> должно! Попытка добавить уже существующее в \
словаре слово, перезапишет его. Так можно исправить ошибку.

Команда:
<code>/del</code> <i>1,2,3</i>
Удаляет одно или несколько слов по номеру в списке.

Each game-command has 'w' atribute, mean 'write mode', If passed bot dont give
you a variants of right answer. You need write it by hand.
    """
    await bot.send_message(msg.chat.id, message, parse_mode="HTML")
    await msg.delete()
 

@dp.message(Command("start"))
async def start_commmand(msg: types.Message):
    
    n = "We hope our bote can help you learn watever you want:)"
    if await bot_functions.check_user(msg.from_user.first_name, script_dir):
        await bot.send_message(msg.chat.id, 
                               f"Hello {msg.from_user.first_name}!\n{n}\n<code>/help</code> for more details.", 
                               parse_mode="HTML")
    else:
        await bot.send_message(msg.chat.id, 
                               f"Welcome {msg.from_user.first_name}!\n{n}\n<code>/help</code> for more details.", 
                               parse_mode="HTML")
    await msg.delete()


@dp.message(Command("show"))
async def show_commmand(msg: types.Message, command=None, sort="Time"):
    global show_msg_store
    connection = sqlite3.connect(f"{script_dir}/{bot_functions.DB_NAME}")
    cursor = connection.cursor()
    list_msg = ""

    #TODO print only selected words by pass arg to command

    cursor.execute(f'SELECT * FROM {msg.chat.first_name}')
    curent_dict = cursor.fetchall()
    longest_word = len(max(curent_dict, key=lambda x: len(x[1]))[1])

    if sort == "Alphabet":
        curent_dict.sort(key=lambda x: x[1])

        for i in curent_dict:
            list_msg += f"<code>{i[1].capitalize()}</code>: <pre>{' '*longest_word}{i[2]}</pre>\n"
    else:
        temp_date = ""
        day_count = 1
        for i in curent_dict:
            if i[4] != temp_date:
                list_msg += '.'" "*10 + i[4] + f" ({day_count})" + "\n"
                temp_date = i[4]
                day_count += 1
            list_msg += f"{i[0]}. <code>{i[1].capitalize()}</code>:  {'  '*(longest_word-len(i[1]))}{i[2]}\n"

    ibtn1 = InlineKeyboardButton(text="Alphabet",callback_data=f"Alphabet")
    ibtn2 = InlineKeyboardButton(text="Time", callback_data=f"Time")
    ibtn3 = InlineKeyboardButton(text="Close", callback_data=f"Close")
    ikb = InlineKeyboardMarkup(inline_keyboard=[[ibtn1,ibtn2],[ibtn3]])

    show_msg = await bot.send_message(msg.chat.id, 
                                      list_msg, 
                                      parse_mode="HTML", 
                                      reply_markup=ikb)
    
    show_msg_store[msg.chat.id] = show_msg.message_id
    await msg.delete()
    connection.close()


@dp.message(Command("add"))
async def add_commmand(msg: types.Message, command):
    if command.args:
        if await bot_functions.add_to_udb(msg.from_user.first_name, command.args, script_dir):
            await bot.send_message(msg.chat.id, 
                               f"Sucsess!",)
        else:
            await bot.send_message(msg.chat.id, 
                               f"Wrong sintax!",)
    else:
        await bot.send_message(msg.chat.id, 
                               f"Pls tipe words you want to add after <b>/add</b> command.\n\n \
<code>/add eng,rus,exsample</code>\n\n\
Example can be empty but ',' stil nesesary. To add multiple sets of words, just conect them by coma.\
Inside example simbol '<b>,</b>' is forbiden!", 
                               parse_mode="HTML")


@dp.message(Command("del"))
async def del_commmand(msg: types.Message, command):
    if command.args and command.args.replace(',', '').isdigit():
        if await bot_functions.del_from_udb(msg.from_user.first_name, command.args, script_dir):
            await bot.send_message(msg.chat.id, "Sucsess.")
        else:
            await bot.send_message(msg.chat.id, "Failure.")
    else:
        await bot.send_message(msg.chat.id, "Need number argument! Like this:\n/del 5\nor\n/del 5,7,12")
    await msg.delete()


done = 0
wrong =0
@dp.message(Command("test"))
async def play_test(msg, command):
    global startp, done, wrong
   
    curent_item = list(my_dict.keys())[startp]
    startp += 1
    for_for_btns = []

    random.shuffle(ansvers)
    wrong_answers = ansvers[:3]
    random.shuffle(wrong_answers)
    for_for_btns.append((wrong_answers[0], "False"))
    for_for_btns.append((wrong_answers[1], "False"))
    for_for_btns.append((wrong_answers[2], "False"))
    for_for_btns.append((my_dict[curent_item][0], "True"))
    random.shuffle(for_for_btns)
    for_btns = dict(for_for_btns)

    ibtn1 = InlineKeyboardButton(text=f"{list(for_btns.keys())[0]}",callback_data=f"{for_btns[list(for_btns.keys())[0]]}")
    ibtn2 = InlineKeyboardButton(text=f"{list(for_btns.keys())[1]}", callback_data=f"{for_btns[list(for_btns.keys())[1]]}")
    ibtn3 = InlineKeyboardButton(text=f"{list(for_btns.keys())[2]}",callback_data=f"{for_btns[list(for_btns.keys())[2]]}")
    ibtn4 = InlineKeyboardButton(text=f"{list(for_btns.keys())[3]}", callback_data=f"{for_btns[list(for_btns.keys())[3]]}")
    ikb = InlineKeyboardMarkup(inline_keyboard=[[ibtn1,ibtn2],[ibtn3,ibtn4]])

    

    await bot.send_message(msg.chat.id, f"{done}/{wrong}\n{curent_item}", reply_markup=ikb)
    await msg.delete()


@dp.callback_query()
async def choice_callback(callback: types.CallbackQuery):
    global done, wrong, show_msg_store
    user_id = callback.from_user.id
    
    if callback.data == "True":
        await callback.answer(text="✅")
        #await callback_data.message.answer("/dict")
        await play_test(callback.message, None)
        done += 1
    elif callback.data == "False":
        await callback.answer(text="❌", show_alert=True)
        wrong += 1

    if callback.data == "Close":
        if user_id in show_msg_store:
            show_msg_id = show_msg_store[user_id]
            await bot.delete_message(chat_id=callback.message.chat.id, message_id=show_msg_id)
            del show_msg_store[user_id]
    elif callback.data == "Alphabet":
        await show_commmand(callback.message, sort="Alphabet")
    elif callback.data == "Time":
        await show_commmand(callback.message)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, 
                           allowed_updates=["message", "edited_message", "callback_query", "inline_query"])

if __name__ == '__main__':
    asyncio.run(main())