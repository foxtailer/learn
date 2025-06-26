from typing import Optional

# В реальной жизни здесь должна быть нормальная СУБД.
# Но для примера нам будет достаточно показать на обычном словаре.
# Учтите, что он сбрасывается при перезапуске бота.
data = dict()


def add_link(
        telegram_id: int,
        link: str,
        title: str,
        description: Optional[str]
):
    """
    Сохраняет ссылку в словарь

    :param telegram_id: ID юзера в Telegram
    :param link: текст ссылки
    :param title: заголовок ссылки
    :param description: (опционально) описание ссылки
    """
    data.setdefault(telegram_id, dict())
    data[telegram_id].setdefault("links", dict())
    data[telegram_id]["links"][link] = {
        "title": title,
        "description": description
    }

def add_photo(
        telegram_id: int,
        photo_file_id: str,
        photo_unique_id: str
):
    """
    Сохраняет изображение в словарь

    :param telegram_id: ID юзера в Telegram
    :param photo_file_id: file_id изображения
    :param photo_unique_id: file_unique_id изображения
    """
    data.setdefault(telegram_id, dict())
    data[telegram_id].setdefault("images", [])
    if photo_file_id not in data[telegram_id]["images"]:
        data[telegram_id]["images"].append((photo_file_id, photo_unique_id))

def get_links_by_id(telegram_id: int) -> dict:
    """
    Получает сохранённые ссылки пользователя

    :param telegram_id: ID юзера в Telegram
    :return: если по юзеру есть данные, то словарь со ссылками
    """
    if telegram_id in data and "links" in data[telegram_id]:
        return data[telegram_id]["links"]
    return dict()

def get_images_by_id(telegram_id: int) -> list[str]:
    """
    Получает сохранённые изображения пользователя

    :param telegram_id: ID юзера в Telegram
    :return:
    """
    if telegram_id in data and "images" in data[telegram_id]:
        return [item[0] for item in data[telegram_id]["images"]]
    return []

def delete_link(telegram_id: int, link: str):
    """
    Удаляет ссылку

    :param telegram_id: ID юзера в Telegram
    :param link: ссылка
    """
    if telegram_id in data:
        if "links" in data[telegram_id]:
            if link in data[telegram_id]["links"]:
                del data[telegram_id]["links"][link]

def delete_image(telegram_id: int, photo_file_unique_id: str):
    """
    Удаляет изображение

    :param telegram_id: ID юзера в Telegram
    :param photo_file_unique_id: file_unique_id изображения для удаления
    """
    if telegram_id in data and "images" in data[telegram_id]:
        for index, (_, unique_id) in enumerate(data[telegram_id]["images"]):
            if unique_id == photo_file_unique_id:
                data[telegram_id]["images"].pop(index)

#######################3####

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, PhotoSize
from aiogram import Bot, types, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.fsm.state import StatesGroup, State

############################

class SaveCommon(StatesGroup):
    waiting_for_save_start = State()


class TextSave(StatesGroup):
    waiting_for_title = State()
    waiting_for_description = State()


############################

from typing import Union, Dict, Any


class HasLinkFilter(BaseFilter):
    async def __call__(self, message: Message) -> Union[bool, Dict[str, Any]]:
        # Если entities вообще нет, вернётся None,
        # в этом случае считаем, что это пустой список
        entities = message.entities or []

        # Если есть хотя бы одна ссылка, возвращаем её
        for entity in entities:
            if entity.type == "url":
                return {"link": entity.extract_from(message.text)}

        # Если ничего не нашли, возвращаем None
        return False
    

###################################

import asyncio


bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(SaveCommon.waiting_for_save_start, F.text, HasLinkFilter())
async def save_text_has_link(message: Message, link: str, state: FSMContext):
    await state.update_data(link=link)
    await state.set_state(TextSave.waiting_for_title)
    await message.answer(
        text=f"Окей, я нашёл в сообщении ссылку {link}. "
             f"Теперь отправь мне заголовок (не больше 30 символов)"
    )

@dp.message(SaveCommon.waiting_for_save_start, F.text)
async def save_text_no_link(message: Message):
    await message.answer(
        text="Эмм.. я не нашёл в твоём сообщении ссылку. "
             "Попробуй ещё раз или нажми /cancel, чтобы отменить."
    )

@dp.message(TextSave.waiting_for_title, F.text)
@dp.message(TextSave.waiting_for_description, F.text)
async def text_too_long(message: Message):  # бывш. too_long_title()
    await message.answer("Слишком длинный заголовок. Попробуй ещё раз")
    return

# Эта функция должна быть ПЕРЕД text_too_long() !
@dp.message(TextSave.waiting_for_description, F.text.func(len) <= 30)
@dp.message(TextSave.waiting_for_description, Command("skip"))
async def last_step(
        message: Message,
        state: FSMContext,
        command: Optional[CommandObject] = None
):
    if not command:
        await state.update_data(description=message.text)
    # Сохраняем данные в нашу ненастоящую БД
    data = await state.get_data()
    add_link(message.from_user.id, data["link"], data["title"], data["description"])

    await message.answer("Ссылка сохранена!")
    await state.clear()

@dp.message(SaveCommon.waiting_for_save_start, F.photo[-1].as_("photo"))
async def save_image(message: Message, photo: PhotoSize, state: FSMContext):
    add_photo(message.from_user.id, photo.file_id, photo.file_unique_id)
    await message.answer("Изображение сохранено!")
    await state.clear()


@dp.inline_query(F.query == "links")
async def show_user_links(inline_query: InlineQuery):

    # Эта функция просто собирает текст, который будет
    # отправлен при нажатии на вариант в инлайн-режиме
    def get_message_text():
        # эта вложенная функция описана выше ↑

    results = []
    for link, link_data in get_links_by_id(inline_query.from_user.id).items():
        # В итоговый массив запихиваем каждую запись
        results.append(InlineQueryResultArticle(
            id=link,  # ссылки у нас уникальные, потому проблем не будет
            title=link_data["title"],
            description=link_data["description"],
            input_message_content=InputTextMessageContent(
                message_text=get_message_text(
                    link=link,
                    title=link_data["title"],
                    description=link_data["description"]
                ),
                parse_mode="HTML"
            )
        ))
    # Важно указать is_personal=True!
    await inline_query.answer(results, is_personal=True)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
