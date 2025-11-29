from aiogram import Bot, types, Dispatcher
import asyncio
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

import sys; sys.path.append('/home/zoy/vscode')
import deps
TOKEN = deps.F


bot = Bot(TOKEN)
dp = Dispatcher()

btn1 = KeyboardButton(text="/help")
btn2 = KeyboardButton(text="/vote")
kb = ReplyKeyboardMarkup(keyboard=[[btn1, btn2]], resize_keyboard=True)  # , one_time_keyboard=True

ibtn1 = InlineKeyboardButton(text="Yes!",callback_data="like")
ibtn2 = InlineKeyboardButton(text="No!", callback_data="dislike")
ikb = InlineKeyboardMarkup(inline_keyboard=[[ibtn1,ibtn2]])

user_vote_message_ids = {}


@dp.message(Command("start"))
async def start_commmand(msg: types.Message):
    await bot.send_message(chat_id=msg.chat.id, text="He-he", reply_markup=kb)


@dp.message(Command("vote"))
async def vote_command(msg: types.Message):
    global vote_message_id
    vote_message = await bot.send_photo(chat_id=msg.chat.id, 
                                        photo="https://th.bing.com/th/id/OIP.SrPnbwpnOKAffgZjeR2qWgHaKz?rs=1&pid=ImgDetMain",
                                        caption="Do you like this image?", 
                                        reply_markup=ikb)
    user_vote_message_ids[msg.from_user.id] = vote_message.message_id
    await msg.delete()


@dp.callback_query()
async def vote_callback(callback_data: types.CallbackQuery):
    user_id = callback_data.from_user.id

    if callback_data.data == "like":
        await callback_data.answer(text="Cool!")
    await callback_data.answer(text=":P")

    if user_id in user_vote_message_ids:
        vote_message_id = user_vote_message_ids[user_id]
        await bot.delete_message(chat_id=callback_data.message.chat.id, message_id=vote_message_id)
        del user_vote_message_ids[user_id]  # Remove the entry after deletion


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
