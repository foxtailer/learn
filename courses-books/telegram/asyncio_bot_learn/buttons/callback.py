import asyncio
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder


TOKEN = ""

bot = Bot(TOKEN,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(Command("random"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.as_markup()
    )


@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.answer(
        text="Спасибо, что воспользовались ботом!",
        show_alert=True
    )
    # или просто await callback.answer()
    # await callback.message.answer(str(random.randint(1, 10)))

    original = "AgACAgQAAxkDAAImsmdYI-vDlG3IioDWnBeKndQa6hvAAALbrzEbaTktUKLSKLKM4YNpAQADAgADcwADNgQ"
    shuffled = ''.join(random.sample(original, len(original)))
    shuffled[:-4] += 'DNgQ'
    await callback.message.answer(shuffled)
    # await bot.send_photo(chat_id=callback.message.chat.id,
    #                                photo='AgACAgIAAxkBAAIyqmgjH6ku53IRqywJcHzsD-HTpWsGAAJV9TEbv5sYSTH7PllEvOM1AQADAgADeQADNgQ')
    # await bot.send_photo(chat_id=callback.message.chat.id,
    #                                photo='AgACAgQAAxkDAAImsmdYI-vDlG3IioDWnBeKndQa6hvAAALbrzEbaTktUKLSKLKM4YNpAQADAgADcwADNgQ')
    await bot.send_photo(chat_id=callback.message.chat.id,
                                   photo=f'{shuffled}')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())