import asyncio

from aiogram import Bot, types, Dispatcher
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji


TOKEN = ""

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command("dice"))
async def cmd_dice(message: types.Message, bot: Bot):
    await bot.send_dice(message.from_user.id, emoji=DiceEmoji.DICE)
    await message.answer_dice(emoji=DiceEmoji.BASKETBALL)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())