import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'

headers = {
    "User-Agent": "Mozilla/5.0"
}

req = Request(url, headers=headers)
resp = urlopen(req)
bs = BeautifulSoup(resp, 'lxml')

'''
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
'''

for link in bs.find('div', {'id':'bodyContent'}).find_all(
        'a', href=re.compile('^(/wiki/)((?!:).)*$')):
    print(link.attrs['href'])

