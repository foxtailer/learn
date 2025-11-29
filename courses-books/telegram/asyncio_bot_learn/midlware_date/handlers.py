from aiogram import types, Router
from aiogram.filters import Command


router = Router()


@router.message(Command("happymonth"))
async def cmd_happymonth(
        message: types.Message, 
        internal_id: int, 
        is_happy_month: bool
):
    phrases = [f"Ваш ID в нашем сервисе: {internal_id}"]

    if is_happy_month:
        phrases.append("Сейчас ваш счастливый месяц!")
    else:
        phrases.append("В этом месяце будьте осторожнее...")

    await message.answer(". ".join(phrases))
