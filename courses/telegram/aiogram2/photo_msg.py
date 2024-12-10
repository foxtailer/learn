import asyncio
from aiogram import Bot, types, Dispatcher


TOKEN = ''

bot = Bot(TOKEN)
dp = Dispatcher()
tmp = []


@dp.message()
async def photo_message(msg: types.Message):
    """
    'file_unique_id' - Common for all chats in tg unique image hash.
    can not be used for sanding """\

    message = await bot.send_photo(chat_id=msg.chat.id,
                                   photo='https://upload.wikimedia.org/wikipedia/en/3/3f/Ghost_in_the_Shell_S.A.C._2nd_GIG_Motoko_Kusanagi.png')
    # Notise 'file_unique_id' field
    print(message.model_dump())
    print(message.photo[-1].file_unique_id)
    
    if message.photo[-1].file_unique_id in tmp:
        print('Boring:(')

    tmp.append(message.photo[-1].file_unique_id)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


"""
{
    'message_id': 9906,
    'date': 1733829611,
    'chat': {
        'id': 6338958823,
        'type': 'private',
        'title': None,
        'username': 'drbeakant',
        'first_name': 'Yaroslav',
        'last_name': None,
        'is_forum': None,
        'accent_color_id': None,
        'active_usernames': None,
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
        'has_private_forwards': None,
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
        'unrestrict_boost_count': None
    },
    'message_thread_id': None,
    'from_user': {
        'id': 1690656566,
        'is_bot': True,
        'first_name': 'FoxtailerBot',
        'last_name': None,
        'username': 'Foxtailerbot',
        'language_code': None,
        'is_premium': None,
        'added_to_attachment_menu': None,
        'can_join_groups': None,
        'can_read_all_group_messages': None,
        'supports_inline_queries': None,
        'can_connect_to_business': None,
        'has_main_web_app': None
    },
    'sender_chat': None,
    'sender_boost_count': None,
    'sender_business_bot': None,
    'business_connection_id': None,
    'forward_origin': None,
    'is_topic_message': None,
    'is_automatic_forward': None,
    'reply_to_message': None,
    'external_reply': None,
    'quote': None,
    'reply_to_story': None,
    'via_bot': None,
    'edit_date': None,
    'has_protected_content': None,
    'is_from_offline': None,
    'media_group_id': None,
    'author_signature': None,
    'text': None,
    'entities': None,
    'link_preview_options': None,
    'effect_id': None,
    'animation': None,
    'audio': None,
    'document': None,
    'paid_media': None,
    'photo': [{
        'file_id': 'AgACAgQAAxkDAAImsmdYI-vDlG3IioDWnBeKndQa6hvAAALbrzEbaTktUKLSKLKM4YNpAQADAgADcwADNgQ',
        'file_unique_id': 'AQAD268xG2k5LVB4',
        'width': 90,
        'height': 49,
        'file_size': 1228
    }, {
        'file_id': 'AgACAgQAAxkDAAImsmdYI-vDlG3IioDWnBeKndQa6hvAAALbrzEbaTktUKLSKLKM4YNpAQADAgADbQADNgQ',
        'file_unique_id': 'AQAD268xG2k5LVBy',
        'width': 320,
        'height': 173,
        'file_size': 14342
    }, {
        'file_id': 'AgACAgQAAxkDAAImsmdYI-vDlG3IioDWnBeKndQa6hvAAALbrzEbaTktUKLSKLKM4YNpAQADAgADeAADNgQ',
        'file_unique_id': 'AQAD268xG2k5LVB9',
        'width': 430,
        'height': 232,
        'file_size': 22394
    }],
    'sticker': None,
    'story': None,
    'video': None,
    'video_note': None,
    'voice': None,
    'caption': None,
    'caption_entities': None,
    'show_caption_above_media': None,
    'has_media_spoiler': None,
    'contact': None,
    'dice': None,
    'game': None,
    'poll': None,
    'venue': None,
    'location': None,
    'new_chat_members': None,
    'left_chat_member': None,
    'new_chat_title': None,
    'new_chat_photo': None,
    'delete_chat_photo': None,
    'group_chat_created': None,
    'supergroup_chat_created': None,
    'channel_chat_created': None,
    'message_auto_delete_timer_changed': None,
    'migrate_to_chat_id': None,
    'migrate_from_chat_id': None,
    'pinned_message': None,
    'invoice': None,
    'successful_payment': None,
    'refunded_payment': None,
    'users_shared': None,
    'chat_shared': None,
    'connected_website': None,
    'write_access_allowed': None,
    'passport_data': None,
    'proximity_alert_triggered': None,
    'boost_added': None,
    'chat_background_set': None,
    'forum_topic_created': None,
    'forum_topic_edited': None,
    'forum_topic_closed': None,
    'forum_topic_reopened': None,
    'general_forum_topic_hidden': None,
    'general_forum_topic_unhidden': None,
    'giveaway_created': None,
    'giveaway': None,
    'giveaway_winners': None,
    'giveaway_completed': None,
    'video_chat_scheduled': None,
    'video_chat_started': None,
    'video_chat_ended': None,
    'video_chat_participants_invited': None,
    'web_app_data': None,
    'reply_markup': None,
    'forward_date': None,
    'forward_from': None,
    'forward_from_chat': None,
    'forward_from_message_id': None,
    'forward_sender_name': None,
    'forward_signature': None,
    'user_shared': None
}
"""