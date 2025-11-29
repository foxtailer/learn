from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiohttp import web


# Create instances of Bot and Dispatcher
API_TOKEN = ''
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message()
async def echo_message(msg):
    await bot.send_message(msg.from_user.id, msg.text)


# Create a SimpleRequestHandler instance
webhook_handler = SimpleRequestHandler(
    dispatcher=dp,
    bot=bot,
    handle_in_background=True,  # Respond immediately without waiting for the handler
    secret_token=None           # Optional, used for validating incoming requests
)


# Create and set up the aiohttp web application
app = web.Application()
webhook_handler.register(app, path='/webhook')


# Run the aiohttp application
if __name__ == '__main__':
    web.run_app(app, port=88)
