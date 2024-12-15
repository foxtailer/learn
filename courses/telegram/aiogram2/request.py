import requests


END_POINT = "https://api.telegram.org/bot"
TOKEN = ""

METHOD1 = '/getMe'
METHOD2 = '/getUpdates'
METHOD3 = '/sendMessage'


# /getMe
updates = requests.get(END_POINT + TOKEN + METHOD1).json()
print(updates)
"""
{
    'ok': True,
    'result': {
        'id': 1690656566,
        'is_bot': True,
        'first_name': 'FoxtailerBot',
        'username': 'Foxtailerbot',
        'can_join_groups': True,
        'can_read_all_group_messages': False,
        'supports_inline_queries': False,
        'can_connect_to_business': False,
        'has_main_web_app': False
    }
}
"""


# /getUpdates
print('@')
updates = requests.get(END_POINT + TOKEN + METHOD2).json()
print(updates)
"""
{
    'ok': True,
    'result': [{
        'update_id': 321800935,
        'message': {
            'message_id': 9901,
            'from': {
                'id': 6338958823,
                'is_bot': False,
                'first_name': 'Yaroslav',
                'username': 'drbeakant',
                'language_code': 'en'
            },
            'chat': {
                'id': 6338958823,
                'first_name': 'Yaroslav',
                'username': 'drbeakant',
                'type': 'private'
            },
            'date': 1733828021,
            'text': 'Hello World!'
        }
    }]
}
"""


# /sendMessage
print('@')
message = updates['result'][0]['message']
chat_id = message['from']['id']
text = message['text']

response = requests.post(END_POINT + TOKEN + METHOD3,
                         data={'chat_id': chat_id,
                               'text': '>>> ' + text}
                        )
print( response)
"""
<Response [200]>
"""
