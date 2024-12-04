import requests

END_POINT = "https://api.telegram.org/bot"
TOKEN = ""

METHOD1 = '/getMe'
METHOD2 = '/getUpdates'
METHOD3 = '/sendMessage'

updates = requests.get(END_POINT + TOKEN + METHOD1).json()
print(updates)

print('@')
updates = requests.get(END_POINT + TOKEN + METHOD2).json()
print(updates)

print('@')
message = updates['result'][0]['message']
chat_id = message['from']['id']
text = message['text']

response = requests.post(END_POINT + TOKEN + METHOD3, data={'chat_id':chat_id,
                                                            'text':'>>> '+text})
print( response)
