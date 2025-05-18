import asyncio
import os
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware, Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


class CounterMiddleware(BaseMiddleware):
     def __init__(self) -> None:
         self.counter = 0
     async def __call__(
         self,
         handler: Callable[[types.TelegramObject, Dict[str, Any]], Awaitable[Any]],
         event: types.TelegramObject,
         data: Dict[str, Any]
     ) -> Any:
         self.counter += 1
         data['counter'] = self.counter
         return await handler(event, data)
     

bot = Bot(token=os.getenv('TOKEN'),
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
dp.update.middleware(CounterMiddleware())


@dp.message()
async def echo_message(msg: types.Message, counter):
    await msg.answer(f'>>> counter: {counter}')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


asyncio.run(main())
