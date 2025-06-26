import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command

from aiogram.utils.keyboard import InlineKeyboardBuilder


TOKEN = ""

bot = Bot(TOKEN,
          default=DefaultBotProperties(
              parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


@dp.message(Command("inline_url"))
async def cmd_inline_url(message: types.Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="GitHub", url="https://github.com")
    )
    builder.row(types.InlineKeyboardButton(
        text="Оф. канал Telegram",
        url="tg://resolve?domain=telegram")
    )

    # Чтобы иметь возможность показать ID-кнопку,
    # У юзера должен быть False флаг has_private_forwards
    user_id = message.from_user.id
    chat_info = await bot.get_chat(user_id)
    if not chat_info.has_private_forwards:
        builder.row(types.InlineKeyboardButton(
            text="Какой-то пользователь",
            url=f"tg://user?id={user_id}")
        )

    await message.answer(
        'Выберите ссылку',
        reply_markup=builder.as_markup(),
    )


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())