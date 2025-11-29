from aiogram import Router

from filter import FirstCharFilter


router1 = Router()
router2 = Router()


@router1.message(FirstCharFilter('^'))
async def echo(msg):
    await msg.answer(msg.text)


@router2.message(FirstCharFilter('&'))
async def echo(msg):
    await msg.answer(msg.text)