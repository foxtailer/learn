import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from datetime import datetime

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
#dp.middleware.setup(LoggingMiddleware())

# In-memory storage for storing notes. Replace it with a proper database in production.
notes_storage = {}


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Show Calendar")
    markup.add(item)
    await message.answer("Hi! I am your Calendar Bot. Click 'Show Calendar' to get started.", reply_markup=markup)


@dp.message_handler(lambda message: message.text == "Show Calendar")
async def show_calendar(message: types.Message):
    # Build an inline keyboard with buttons for each month
    markup = InlineKeyboardMarkup(row_width=4)
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    for month in months:
        markup.insert(InlineKeyboardButton(month, callback_data=f"month_{month}"))

    await message.reply("Select a month:", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data.startswith('month_'))
async def process_month_callback(callback_query: types.CallbackQuery):
    month = callback_query.data.split('_')[1]

    # Build an inline keyboard with buttons for each day
    markup = InlineKeyboardMarkup(row_width=7)
    days_in_month = 31  # You may need to adjust this based on the actual days in the selected month
    
    for day in range(1, days_in_month + 1):
        markup.insert(InlineKeyboardButton(str(day), callback_data=f"day_{day}_{month}"))

    await bot.send_message(callback_query.from_user.id, f"Select a day in {month}:", reply_markup=markup)
    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data.startswith('day_'))
async def process_day_callback(callback_query: types.CallbackQuery):
    _, day, month = callback_query.data.split('_')
    user_id = callback_query.from_user.id

    await bot.send_message(user_id, f"You selected {day} {month}.")

    # Allow the user to write a note for the selected day
    await bot.send_message(user_id, "Write a note for this day:")

    # Save the day and note in the in-memory storage (replace this with a database in production)
    notes_storage[user_id] = {
        'day': day,
        'month': month,
        'note': None
    }

    # Update the handler to wait for the user's note
    dp.register_message_handler(process_note, state='*', content_types=types.ContentTypes.TEXT)


async def process_note(message: types.Message):
    user_id = message.from_user.id
    if user_id in notes_storage:
        notes_storage[user_id]['note'] = message.text
        await bot.send_message(user_id, f"Note saved: {message.text}")
    else:
        await bot.send_message(user_id, "Error: No day selected. Please start over.")

    # Unregister the note handler to go back to the main menu
    dp.unregister_message_handler(process_note)
    await send_welcome(message)


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
