import asyncio
from aiogram import Bot, types, Dispatcher


TOKEN = ''

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message()
async def invite_link_message(msg: types.Message):
    # Bot must be admin in group
    inv_link = await bot.export_chat_invite_link(chat_id=msg.chat.id)

    await bot.send_message(chat_id=msg.chat.id,
                                     text=inv_link)
    
    # Or
    get_chat = await bot.get_chat(chat_id=msg.chat.id)
    print(get_chat.model_dump())


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


# Get Chat
"""
{
    'id': 6338958823,
    'type': 'private',
    'title': None,
    'username': 'drbeakant',
    'first_name': 'Yaroslav',
    'last_name': None,
    'is_forum': None,
    'accent_color_id': 1,
    'active_usernames': ['drbeakant'],
    'available_reactions': None,
    'background_custom_emoji_id': None,
    'bio': None,
    'birthdate': None,
    'business_intro': None,
    'business_location': None,
    'business_opening_hours': None,
    'can_set_sticker_set': None,
    'custom_emoji_sticker_set_name': None,
    'description': None,
    'emoji_status_custom_emoji_id': None,
    'emoji_status_expiration_date': None,
    'has_aggressive_anti_spam_enabled': None,
    'has_hidden_members': None,
    'has_private_forwards': True,
    'has_protected_content': None,
    'has_restricted_voice_and_video_messages': None,
    'has_visible_history': None,
    'invite_link': None,
    'join_by_request': None,
    'join_to_send_messages': None,
    'linked_chat_id': None,
    'location': None,
    'message_auto_delete_time': None,
    'permissions': None,
    'personal_chat': None,
    'photo': None,
    'pinned_message': None,
    'profile_accent_color_id': None,
    'profile_background_custom_emoji_id': None,
    'slow_mode_delay': None,
    'sticker_set_name': None,
    'unrestrict_boost_count': None,
    'max_reaction_count': 11,
    'can_send_paid_media': None
}
"""