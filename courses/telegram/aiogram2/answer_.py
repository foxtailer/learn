import asyncio

from aiogram import Bot, types, Dispatcher


bot = Bot('')
dp = Dispatcher()
input_file = types.URLInputFile("https://picsum.photos/seed/groosha/400/300")


@dp.message()
async def echo_message(msg: types.Message):
    await msg.answer(msg.text)

    #? animation="CgACAgIAAxkBAAEDcqNilOf-bZLcNgyJb1mySjg6gGQuwAAC8AYAAlBaAUnG2zvAb3PTAyQE"
    await msg.answer_animation(animation=input_file)
    await msg.answer_photo(photo=input_file)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
