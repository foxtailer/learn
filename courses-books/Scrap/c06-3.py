import re
import random
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


pages = set()


def getArticles(url: str, article: str): 

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    req = Request(url + article, headers=headers)
    resp = urlopen(req)
    bs = BeautifulSoup(resp, 'lxml')

    try:
        print('-' * 30, article, bs.h1.get_text(), sep='\n')
        print()

        if (p1 := bs.find('div', {'id': 'mw-content-text'}).find('p')):
            print(p1.get_text())

        print(bs.find(id='ca-edit').find('a').attrs['href'],
              '-' * 30, sep='\n')
    except:
        print('This page is missing something! Continuing.')

    for article in bs.find('div', {'id':'bodyContent'}).find_all(
            'a', href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in article.attrs:
            if (art := article.attrs['href']) not in pages:
                pages.add(art)
                getArticles(url, art)
                


url = 'https://en.wikipedia.org'
article = '/wiki/Kevin_Bacon'


while len(links := getArticles(url, article)) > 0:
    print(article)
    article = random.choice(links).attrs['href']

