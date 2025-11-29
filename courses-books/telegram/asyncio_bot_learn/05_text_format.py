import asyncio

from aiogram import Bot, types, Dispatcher, html
from aiogram.filters.command import Command
from aiogram.utils.formatting import Text, Bold
from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section, as_key_value, HashTag
)


TOKEN = ""

bot = Bot(TOKEN)
dp = Dispatcher()


# Если не указать фильтр F.text, 
# то хэндлер сработает даже на картинку с подписью /test,
# но пока нам это не важно и рассматриваем только текстовые сообщения
@dp.message(Command("test"))
async def any_message(message: types.Message):
    await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
    await message.answer("Hello, *world*\!", parse_mode="MarkdownV2")
    await message.answer("Сообщение без <s>какой-либо разметки</s>", parse_mode=None)
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
        parse_mode="HTML"
    )
   
    html.underline(f"Создано в ...")   # Создаём подчёркнутый текст
    html.quote(message.from_user.full_name)  # prevent treating text as html

    # message.test return raw text, we can use: message.html_text или message.md_text to get formated text


@dp.message(Command("hello"))
async def cmd_hello(message):
    content = Text(
        "Hello, ",
        Bold(message.from_user.full_name)
    )

    # конструкция **content.as_kwargs() вернёт аргументы text, entities, parse_mode и подставит их в вызов answer().
    await message.answer(**content.as_kwargs())  


@dp.message(Command("advanced_example"))
async def cmd_advanced_example(message):
    content = as_list(
        as_marked_section(
            Bold("Success:"),
            "Test 1",
            "Test 3",
            "Test 4",
            marker="✅ ",
        ),
        as_marked_section(
            Bold("Failed:"),
            "Test 2",
            marker="❌ ",
        ),
        as_marked_section(
            Bold("Summary:"),
            as_key_value("Total", 4),
            as_key_value("Success", 3),
            as_key_value("Failed", 1),
            marker="  ",
        ),
        HashTag("#test"),
        sep="\n\n",
    )
    await message.answer(**content.as_kwargs())


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())