from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import bot_functions
import random
import sqlite3

import sys; sys.path.append('/home/zoy/vscode')
import deps

bot = Bot(deps.F)
dp = Dispatcher()

import json
import codecs


script_dir = bot_functions.find_path()

"""
test - Play test
show - Show dictionary
add - Add new line in dict
addm - Add meny lines
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
    connection = sqlite3.connect(f"{script_dir}/{bot_functions.DB_NAME}")
    cursor = connection.cursor()
    list_msg = ""

    #TODO print only selected words by pass arg to command

    cursor.execute(f'SELECT * FROM {msg.chat.first_name}')
    curent_dict = cursor.fetchall()

    if sort == "Alphabet":
        curent_dict.sort(key=lambda x: x[1])

        for i in curent_dict:
            list_msg += f"{i[1]} {i[2]}\n"
 
    else:
        for i in curent_dict:
            list_msg += f"{i[1]} {i[2]}\n"

    ibtn1 = InlineKeyboardButton(text="Alphabet",callback_data=f"Alphabet")
    ibtn2 = InlineKeyboardButton(text="Time", callback_data=f"Time")
    ibtn3 = InlineKeyboardButton(text="Close", callback_data=f"Close")
    ikb = InlineKeyboardMarkup(inline_keyboard=[[ibtn1,ibtn2],[ibtn3]])

    await bot.send_message(msg.chat.id, list_msg, parse_mode="HTML", reply_markup=ikb)
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
    if command.args:
        await bot_functions.del_from_udb(msg.from_user.first_name, command.args, script_dir)
    else:
        await bot.send_message(msg.chat.id, "Need argument!")


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



# @dp.message(Command("test"))   
# async def play_test(msg, command):

#     connection = sqlite3.connect(f"{_path}{msg.chat.first_name}.db")
#     cursor = connection.cursor()

#     if command and command.args:
#         test_days = command.args.strip()
#         cursor.execute(f'DELETE FROM {msg.chat.first_name}_test')
#         cursor.execute(f'INSERT OR IGNORE INTO {msg.chat.first_name}_test (test_days) VALUES (?)', (test_days,))
#         connection.commit()

#     cursor.execute(f'SELECT test_days FROM {msg.chat.first_name}_test')
#     test_days = cursor.fetchall()[0][0].split(",")
#     print(test_days)
#     if test_days == ['0']:
#         cursor.execute(f'SELECT * FROM {msg.chat.first_name}')
#         curent_dict = cursor.fetchall()
#     else:
#         placeholders = ','.join(['?' for _ in test_days])
#         cursor.execute(f'SELECT * FROM {msg.chat.first_name} WHERE day IN ({placeholders})', test_days)
#         curent_dict = cursor.fetchall()

#     connection.commit()
#     connection.close()    

#     curent_item = random.choice(curent_dict)
#     for_for_btns = []

#     curent_dict.remove(curent_item)
#     wrong_answers = [item[1] for item in curent_dict]
#     random.shuffle(wrong_answers)
#     for_for_btns.append((wrong_answers[0], "False"))
#     for_for_btns.append((wrong_answers[1], "False"))
#     for_for_btns.append((wrong_answers[2], "False"))
#     for_for_btns.append((curent_item[1], "True"))
#     random.shuffle(for_for_btns)
#     for_btns = dict(for_for_btns)

#     ibtn1 = InlineKeyboardButton(text=f"{list(for_btns.keys())[0]}",callback_data=f"{for_btns[list(for_btns.keys())[0]]}")
#     ibtn2 = InlineKeyboardButton(text=f"{list(for_btns.keys())[1]}", callback_data=f"{for_btns[list(for_btns.keys())[1]]}")
#     ibtn3 = InlineKeyboardButton(text=f"{list(for_btns.keys())[2]}",callback_data=f"{for_btns[list(for_btns.keys())[2]]}")
#     ibtn4 = InlineKeyboardButton(text=f"{list(for_btns.keys())[3]}", callback_data=f"{for_btns[list(for_btns.keys())[3]]}")
#     ikb = InlineKeyboardMarkup(inline_keyboard=[[ibtn1,ibtn2],[ibtn3,ibtn4]])

#     if isinstance(curent_item[3], str):
#         answer = f"{curent_item[2].title()}:\n{curent_item[3].replace(curent_item[1], '*'*len(curent_item[1])).capitalize()}"
#     else:
#         answer = f"{curent_item[2].title()}:"

#     await bot.send_message(msg.chat.id, answer, reply_markup=ikb)
#     await msg.delete()


@dp.callback_query()
async def choice_callback(callback: types.CallbackQuery):
    global done, wrong
    if callback.data == "Close":
        callback.message.delete()
    if callback.data == "True":
        await callback.answer(text="✅")
        #await callback_data.message.answer("/dict")
        await play_test(callback.message, None)
        done += 1
    elif callback.data == "Alphabet":
        await show_commmand(callback.message, sort="Alphabet")
    elif callback.data == "Time":
        await show_commmand(callback.message)
    else:
        await callback.answer(text="❌", show_alert=True)
        wrong += 1


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())