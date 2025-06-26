import logging
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton

from aiogram_calendar import SCCallback, SimpleCalendar, DCCallback, DialogCalendar


API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

btn1 = KeyboardButton(text='Navigation Calendar')
btn2 = KeyboardButton(text='Dialog Calendar')
start_kb = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[[btn1], [btn2]])


# starting bot when user sends `/start` command, answering with inline calendar
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.reply('Pick a calendar', reply_markup=start_kb)


@dp.message(F.text == 'Navigation Calendar')
async def nav_cal_handler(message: Message):
    await message.answer("Please select a date: ", reply_markup=await SimpleCalendar().start_calendar())


@dp.callback_query(SCCallback.filter())
async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selected:
        await callback_query.message.answer(
            f'You selected {date.strftime("%d/%m/%Y")}',
            reply_markup=start_kb
        )


@dp.message(F.text == 'Dialog Calendar')
async def simple_cal_handler(message: Message):
    await message.answer("Please select a date: ", reply_markup=await DialogCalendar().start_calendar())


# dialog calendar usage
@dp.callback_query(DCCallback.filter())
async def process_dialog_calendar(callback_query: CallbackQuery, callback_data: dict):
    selected, date = await DialogCalendar().process_selection(callback_query, callback_data)
    if selected:
        await callback_query.message.answer(
            f'You selected {date.strftime("%d/%m/%Y")}',
            reply_markup=start_kb
        )


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, 
                           allowed_updates=["message", "edited_message", "callback_query", "inline_query"],
                           polling_timeout=20)


if __name__ == '__main__':
    asyncio.run(main())
