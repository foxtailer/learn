import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from aiogram.utils.callback_answer import CallbackAnswer


TOKEN = ""

bot = Bot(TOKEN,
          default=DefaultBotProperties(
              parse_mode=ParseMode.HTML)
)
dp = Dispatcher()
#dp.callback_query.middleware(CallbackAnswerMiddleware())
dp.callback_query.middleware(
    CallbackAnswerMiddleware(
        pre=True, text="Готово!", show_alert=True
    )
)


@dp.message(Command("dom"))
async def cmd_dom(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="dom_value")
    )
    await message.answer(
        "Нажмите на кнопку",
        reply_markup=builder.as_markup()
    )


@dp.callback_query()
async def my_handler(callback: CallbackQuery, callback_answer: CallbackAnswer):
    ... # тут какой-то код
    if <everything is ok>:
        callback_answer.text = "Отлично!"
    else:
        callback_answer.text = "Что-то пошло не так. Попробуйте позже"
        callback_answer.cache_time = 10
    ... # тут какой-то код

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
