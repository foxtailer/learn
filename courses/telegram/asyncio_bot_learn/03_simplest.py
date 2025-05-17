from aiogram import Bot
import asyncio


TOKEN = ""

bot = Bot(TOKEN)



async def echo():
    #await bot.send_message(msg.from_user.id, msg.text)
    await bot.send_message(6338958823, 'ff')



if __name__ == '__main__':
    asyncio.run(echo())
    