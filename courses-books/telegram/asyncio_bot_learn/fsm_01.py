import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import sys; sys.path.append('/home/zoy/vscode')
import deps


bot = Bot(deps.F)
dp = Dispatcher()

kb = KeyboardButton(text='Hello')
rkb = ReplyKeyboardMarkup(keyboard=[[kb]], resize_keyboard=True)


class UserState(StatesGroup):
    name = State()


@dp.message(CommandStart())
async def start(msg: types.Message, state:FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await msg.reply(msg.text, reply_markup=rkb)
        await state.set_state(UserState.name)


@dp.message(UserState.name)
async def name(msg:types.Message, state:FSMContext):
    await state.update_data(name=msg.text.strip())
    data = await state.get_data()
    await msg.reply(f'Name been added!\n{data}', reply_markup=rkb)
    #await state.clear()
    await state.set_state(state=None)


@dp.message()
async def echo(msg:types.Message, state:FSMContext):
    data = await state.get_data()
    await msg.reply(f'{msg.text}\n{data}', reply_markup=rkb)

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
