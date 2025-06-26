import asyncio
import requests
from aiogram import Bot, types, Dispatcher


TOKEN = ''

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message()
async def photo_message(msg: types.Message):

    # Download the photo
    response = requests.get('https://upload.wikimedia.org/wikipedia/en/3/3f/Ghost_in_the_Shell_S.A.C._2nd_GIG_Motoko_Kusanagi.png')
    response.raise_for_status()  # Ensure the download was successful
    
    # Save to a temporary file or pass the content
    with open("temp_photo.jpg", "wb") as file:
        file.write(response.content)

    photo = '???'  # InputFile

    message = await bot.set_chat_photo(chat_id=msg.chat.id,
                                       photo=photo)
    # print(message.model_dump()) ???


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

