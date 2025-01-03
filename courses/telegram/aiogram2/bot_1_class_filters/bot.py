import asyncio

from aiogram import Bot, Dispatcher

from handlers import group_games, usernames


async def main():
    bot = Bot(token="")
    dp = Dispatcher()
    dp.include_router(group_games.router)
    dp.include_router(usernames.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())