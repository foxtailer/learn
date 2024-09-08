#pip install aiohttp-socks
from aiogram.client.session.aiohttp import AiohttpSession

session = AiohttpSession(proxy='http://proxy.server:3128')

bot = Bot('', session=session)