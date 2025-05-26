import requests


url = 'http://natas4.natas.labs.overthewire.org/'

headers = {
    "User-Agent": "MyApp/1.0",
    "Authorization": "QryZXc2e0zahULdHrtHxzyYkj59kUxLQ",
    "Content-Type": "application/json",
    'Referer': 'http://natas5.natas.labs.overthewire.org/'
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)