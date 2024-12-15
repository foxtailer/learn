import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji


bot = Bot("")
dp = Dispatcher()


@dp.message(Command("dice"))
async def cmd_dice(message: types.Message, bot: Bot):
    # bot pass from dispatcher to handler
    # we can specify ather chat
    await bot.send_dice(message.chat.id, emoji=DiceEmoji.DICE)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
