import asyncio

from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode


bot = Bot('')
dp = Dispatcher()


# Если не указать фильтр F.text, 
# то хэндлер сработает даже на картинку с подписью /test
@dp.message(F.text, Command("test"))
async def any_message(message: types.Message):
    await message.answer(
        "Hello, <b>world</b>!", 
        parse_mode=ParseMode.HTML
    )
    await message.answer(
        "Hello, *world*\!", 
        parse_mode=ParseMode.MARKDOWN_V2
    )
    await message.answer(
        "Сообщение без <s>какой-либо разметки</s>", 
        parse_mode=None
    )
    await message.answer(
        '<b>bold</b>, <strong>bold</strong>\n\n'
        '<i>italic</i>, <em>italic</em>\n\n'
        '<u>underline</u>, <ins>underline</ins>\n\n'
        '<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>\n\n'
        '<span class="tg-spoiler">spoiler</span>, <tg-spoiler>spoiler</tg-spoiler>\n\n'
        '<b>bold <i>italic bold <s>italic bold strikethrough <span class="tg-spoiler">italic bold strikethrough spoiler</span></s> <u>underline italic bold</u></i> bold</b>\n\n'
        '<a href="http://www.example.com/">inline URL</a>\n\n'
        '<a href="tg://user?id=123456789">inline mention of a user</a>\n\n'
        '<tg-emoji emoji-id="5368324170671202286">👍</tg-emoji>\n\n'
        '<code>inline fixed-width code</code>\n\n'
        '<pre>pre-formatted fixed-width code block</pre>\n\n'
        '<pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>\n\n'
        '<blockquote>Block quotation started\nBlock quotation continued\nThe last line of the block quotation</blockquote>\n\n'
        '<blockquote expandable>Expandable block quotation started\nExpandable block quotation continued\nExpandable block quotation continued\nHidden by default part of the block quotation started\nExpandable block quotation continued\nThe last line of the block quotation</blockquote>\n\n',
        parse_mode=ParseMode.HTML
    )


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
