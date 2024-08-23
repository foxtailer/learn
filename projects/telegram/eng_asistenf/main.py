from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import db_functions
import random
import sqlite3

import sys; sys.path.append('/home/zoy/vscode')
import deps


bot = Bot(deps.F)
dp = Dispatcher()

script_dir = db_functions.find_path()
temp = {}

"""
select_day - Select day you want to practice
test - Test throw selected day
test10 - Test with random 10 words
sentense - Guess wond in sentense based on your words
shaffle - Try to guess shaffled word
get_example - Give 5 sentence with word
show - Show dictionary
add - Add new words in dict
del - Deleate word/words
start - Start bot
help - Help/Info
"""


async def play(chat_id, user_name, args):
    global temp
    
    words = temp[chat_id]['day']

    if words:
        answers = []
        word = words.pop()
        answers.append(word)

        if len(words) >= 3:
            answers += random.sample(words, 3)
        else:
            flag = True
            while flag:
                fake_words = await db_functions.get_word(script_dir, user_name, 3)
                if word not in fake_words:
                    flag = False
            
            answers += fake_words
        random.shuffle(answers)

        for_kb = []
        mod = 1
        
        if 'e' in args:
            mod = 2

        if 'w' not in args:
            for answer in answers:
                btn_data = answer[mod], 'True' if answer[mod]==word[mod] else 'False'
                for_kb.append(btn_data)

            ibtn1 = InlineKeyboardButton(text=f"{for_kb[0][0]}",callback_data=f"{for_kb[0][1]}")
            ibtn2 = InlineKeyboardButton(text=f"{for_kb[1][0]}", callback_data=f"{for_kb[1][1]}")
            ibtn3 = InlineKeyboardButton(text=f"{for_kb[2][0]}",callback_data=f"{for_kb[2][1]}")
            ibtn4 = InlineKeyboardButton(text=f"{for_kb[3][0]}", callback_data=f"{for_kb[3][1]}")
            ikb = InlineKeyboardMarkup(inline_keyboard=[[ibtn1,ibtn2],[ibtn3,ibtn4]])

            if 's' in args:
                text = word[3].replace(word[1], '****')
                test_msg = await bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=ikb)
            else:
                test_msg = await bot.send_message(chat_id, word[2 if mod == 1 else 1], parse_mode="HTML", reply_markup=ikb)
        else:
            ...  # TODO Write mode.

        if temp[chat_id].get('test_msg'):
            await asyncio.sleep(2)
            await bot.delete_message(chat_id=chat_id, message_id=temp[chat_id]['test_msg'])

        temp[chat_id]['test_msg'] = test_msg.message_id

    else:
        amount = temp[chat_id]['day_size']
        right_answer = temp[chat_id]['day_answers']

        await bot.send_message(chat_id, text=f"Test is over!\nNice job!\n{right_answer}/{amount}")


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
    if await db_functions.check_user(msg.from_user.first_name, script_dir):
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
    global temp
    list_of_chunks = []
    chunk_msg = ""

    #TODO print only selected words by pass arg to command

    connection = sqlite3.connect(f"{script_dir}/{db_functions.DB_NAME}")
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {msg.chat.first_name}')
    curent_dict = cursor.fetchall()
    connection.close()
    
    longest_word = len(max(curent_dict, key=lambda x: len(x[1]))[1])

    if sort == "Alphabet":
        curent_dict.sort(key=lambda x: x[1])

        for i in curent_dict:
            if len(chunk_msg) < 2500:
                chunk_msg += f"<code>{i[1].capitalize()}</code>: <pre>{' '*longest_word + i[2]}</pre>\n"
            else:
                list_of_chunks.append(chunk_msg)
                chunk_msg = ""
                chunk_msg += f"<code>{i[1].capitalize()}</code>: <pre>{' '*longest_word + i[2]}</pre>\n"

        list_of_chunks.append(chunk_msg)

    elif sort == "Examples":
        for i in curent_dict:
            if len(chunk_msg) < 2500:
                chunk_msg += f"<code>{i[1].capitalize()}</code>: {i[2]} <pre>{i[3]}</pre>\n"
            else:
                list_of_chunks.append(chunk_msg)
                chunk_msg = ""
                chunk_msg += f"<code>{i[1].capitalize()}</code>: {i[2]} <pre>{i[3]}</pre>\n"

        list_of_chunks.append(chunk_msg)

    else:
        temp_date = ""
        day_count = 1

        for i in curent_dict:
            if i[4] != temp_date:
                chunk_msg += '.'" "*10 + i[4] + f" ({day_count})" + "\n"
                temp_date = i[4]
                day_count += 1
            if len(chunk_msg) < 2500:
                chunk_msg += f"{i[0]}. <code>{i[1].capitalize()}</code>:  {'  '*(longest_word-len(i[1]))}{i[2]}\n"
            else:
                list_of_chunks.append(chunk_msg)
                chunk_msg = ""
                chunk_msg += f"{i[0]}. <code>{i[1].capitalize()}</code>:  {'  '*(longest_word-len(i[1]))}{i[2]}\n"

        list_of_chunks.append(chunk_msg)

    ibtn1 = InlineKeyboardButton(text="Alphabet",callback_data=f"Alphabet")
    ibtn2 = InlineKeyboardButton(text="Time", callback_data=f"Time")
    ibtn3 = InlineKeyboardButton(text="Close", callback_data=f"Close")
    ibtn4 = InlineKeyboardButton(text="Examples", callback_data=f"Examples")
    ikb = InlineKeyboardMarkup(inline_keyboard=[[ibtn1,ibtn2],[ibtn4],[ibtn3]])
    
    for chunk in list_of_chunks:
        show_msg = await bot.send_message(msg.chat.id, 
                                        chunk, 
                                        parse_mode="HTML", 
                                        reply_markup=ikb)
    
    # BUG  Deleate only last msg
    if msg.chat.id in temp:
        temp[msg.chat.id].update({'show':{'to_close': show_msg.message_id}})
    else:
        temp[msg.chat.id] = {'show':{'to_close': show_msg.message_id}}

    await msg.delete()


@dp.message(Command("add"))
async def add_commmand(msg: types.Message, command):
    if command.args:
        if await db_functions.add_to_udb(msg.from_user.first_name, command.args, script_dir):
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
        if await db_functions.del_from_udb(msg.from_user.first_name, command.args, script_dir):
            await bot.send_message(msg.chat.id, "Sucsess.")
        else:
            await bot.send_message(msg.chat.id, "Failure.")
    else:
        await bot.send_message(msg.chat.id, "Need number argument! Like this:\n/del 5\nor\n/del 5,7,12")
    await msg.delete()


@dp.message(Command("select_day"))
async def select_day(msg: types.Message, command):
    global temp
    
    if command.args and command.args.isdigit():
        day = await db_functions.get_day(script_dir, msg.from_user.first_name,  int(command.args.strip())-1)
       
        if day:
            tmp = {'day': day, 'day_size': len(day), 'day_answers': 0}

            if msg.chat.id in temp:
                temp[msg.chat.id].update(tmp)
            else:
                temp[msg.chat.id] = tmp
        else:
           await bot.send_message(msg.chat.id, 
                                  "Wrong day numder!")
    else:
        await bot.send_message(msg.chat.id, 
                               f"Pls tipe number of day you want to select after command.\n\n \
<code>/select_day 3</code>\n\n\
You can finde day number using <code>/show</code> command.", 
                               parse_mode="HTML")
        
    await msg.delete()


@dp.message(Command("test"))
async def test(msg: types.Message, command):
    global temp 

    if command.args and command.args.strip() in ('e', 'w', 'e w', 'w e', 's'):
        args = command.args.strip().split()
    else:
        args = ()

    user_name = msg.from_user.first_name

    if msg.chat.id in temp and temp[msg.chat.id].get('day'):
        temp[msg.chat.id]['test_mod'] = args
        await play(msg.chat.id, user_name, args)
    else:
        await bot.send_message(msg.chat.id, 'Pls select day.')

    await msg.delete()


@dp.message(Command("shaffle"))
async def shuffle_play(msg, word=None):
    global temp
    user_name = msg.from_user.first_name
    
    if not word:
        words = await db_functions.get_word(script_dir, user_name)
        word = words[0][1]

        shuffle = {'shuffle':{'shuffle_clue': 0, 
                              'shuffle_word': word,
                              'shuffle_rus': words[0][2],
                              'shuffle_ex': words[0][3]}}
        
        if msg.chat.id in temp:
            temp[msg.chat.id].update(shuffle)
        else:
            temp[msg.chat.id] = shuffle
 
    if word:
        clue = temp[msg.chat.id]['shuffle']['shuffle_clue']
        #clue = min(len(word), clue)

        char_list = list(word[clue:])
        random.shuffle(char_list)
        shuffled_word = '_'.join(char_list)

        if clue >= len(word):
            shuffled_word = word[:clue].upper()
        elif clue != 0:
            shuffled_word = word[:clue].upper() + "_" + shuffled_word
    
        ibtn1 = InlineKeyboardButton(text="Help", callback_data="shuffle_help")
        ikb = InlineKeyboardMarkup(inline_keyboard=[[ibtn1]])

        shuffle_msg = await bot.send_message(msg.chat.id, shuffled_word, reply_markup=ikb)
        temp[msg.chat.id]['shuffle']['shuffle_msg'] = shuffle_msg.message_id
    await msg.delete()


@dp.message()
async def listener(msg: types.Message):
    global temp

    if temp.get(msg.chat.id):

        if temp[msg.chat.id].get('shuffle'):
            shuffle_word = temp[msg.chat.id]['shuffle']['shuffle_word']

            if msg.text.lower() == shuffle_word:
                temp[msg.chat.id]['shuffle']['shuffle_word'] = ''
                answer = await msg.answer(text=f"✅\n{temp[msg.chat.id]['shuffle']['shuffle_rus'].capitalize()}\n\
{temp[msg.chat.id]['shuffle']['shuffle_ex'].capitalize()}", 
                                          show_alert=True)
                await asyncio.sleep(2)
                await bot.delete_message(chat_id=msg.chat.id, message_id=temp[msg.chat.id]['shuffle']['shuffle_msg'])
                await bot.delete_message(chat_id=msg.chat.id, message_id=answer.message_id)
            else:
                answer = await msg.answer(text="❌")
                await asyncio.sleep(1)
                await bot.delete_message(chat_id=msg.chat.id, message_id=answer.message_id)

    await msg.delete()


@dp.callback_query()
async def choice_callback(callback: types.CallbackQuery):
    global temp
    user_id = callback.from_user.id
    
    if callback.data == "True":
        temp[user_id]['day_answers'] += 1

        amount = temp[user_id]['day_size']
        right_answer = temp[user_id]['day_answers']

        if temp[user_id].get('x'):
            await temp[user_id]['x'].delete()
        x = await callback.message.answer(text=f"✅ {right_answer}/{amount}", show_alert=True)
        temp[user_id]['x'] = x
        await play(user_id, callback.from_user.first_name, temp[user_id]['test_mod'])

    elif callback.data == "False":
        #await callback.reply(text="❌", show_alert=True)
        amount = temp[user_id]['day_size']
        right_answer = temp[user_id]['day_answers']
        
        if temp[user_id].get('x'):
            await temp[user_id]['x'].delete()
        x = await callback.message.answer(text=f"❌ {right_answer}/{amount}")
        temp[user_id]['x'] = x
        await play(user_id, callback.from_user.first_name, temp[user_id]['test_mod'])

    if callback.data == "Close":
        if user_id in temp:
            show_msg_id = temp[user_id]['show']['to_close']
            await bot.delete_message(chat_id=callback.message.chat.id, message_id=show_msg_id)
            del temp[user_id]['show']['to_close']
            
    elif callback.data == "Alphabet":
        await show_commmand(callback.message, sort="Alphabet")
    elif callback.data == "Examples":
        await show_commmand(callback.message, sort="Examples")
    elif callback.data == "Time":
        await show_commmand(callback.message)

    if callback.data == "shuffle_help":
        temp[user_id]['shuffle']['shuffle_clue'] += 1
        await shuffle_play(callback.message, word=temp[user_id]['shuffle']['shuffle_word'])


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, 
                           allowed_updates=["message", "edited_message", "callback_query", "inline_query"])


if __name__ == '__main__':
    asyncio.run(main())
