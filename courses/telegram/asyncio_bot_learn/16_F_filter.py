from aiogram import F

# Здесь F - это message
@router.message(F.photo)
async def photo_msg(message: Message):
    await message.answer("Это точно какое-то изображение!")


# router.message.filter(F.chat.type.in_({"group", "supergroup"}))
# F.content_type.in_({'text', 'sticker', 'photo'})
# F.photo | F.text | F.sticker


from aiogram.types import Message, PhotoSize

@router.message(F.photo[-1].as_("largest_photo"))
async def forward_from_channel_handler(message: Message, largest_photo: PhotoSize) -> None:
    print(largest_photo.width, largest_photo.height)


from aiogram import F
from aiogram.types import Message, Chat

@router.message(F.forward_from_chat[F.type == "channel"].as_("channel"))
async def forwarded_from_channel(message: Message, channel: Chat):
    await message.answer(f"This channel's ID is {channel.id}")


from aiogram.enums import MessageEntityType

@router.message(F.entities[:].type == MessageEntityType.EMAIL)
async def all_emails(message: Message):
    await message.answer("All entities are emails")


@router.message(F.entities[...].type == MessageEntityType.EMAIL)
async def any_emails(message: Message):
    await message.answer("At least one email!")