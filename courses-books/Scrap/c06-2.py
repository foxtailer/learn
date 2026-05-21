import re
import random
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


def getArticles(url: str, article: str): 

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    req = Request(url + article, headers=headers)
    resp = urlopen(req)
    bs = BeautifulSoup(resp, 'lxml')

    return bs.find('div', {'id':'bodyContent'}).find_all(
        'a', href=re.compile('^(/wiki/)((?!:).)*$'))


url = 'https://en.wikipedia.org'
article = '/wiki/Kevin_Bacon'


while len(links := getArticles(url, article)) > 0:
    print(article)
    article = random.choice(links).attrs['href']

