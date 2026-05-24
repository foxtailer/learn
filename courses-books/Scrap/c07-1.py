import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup



def get_soup(url: str): 

    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    req = Request(url, headers=headers)
    resp = urlopen(req)
    bs = BeautifulSoup(resp, 'lxml')

    return bs
    

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
    def print(self):
        print(f'TITLE: {self.title}')
        print(f'URL: {self.url}')
        print(f'BODY:\n {self.body}') 


def scrape_cnn(url):
    bs = get_soup(url)
    title = bs.find('h1').text
    body = bs.find('div', {'class': 'article__content'}).text
    return Content(url, title, body)


def scrape_brookings(url):
    bs = get_soup(url)
    title = bs.find('h1').text
    body = bs.find('div', {'class': ['byo-block', '-narrow']}).text
    return Content(url, title, body)


brookings, cnn = (
    'https://www.brookings.edu/research/robotic-rulemaking/',
    'https://www.cnn.com/2023/04/03/investing/\
dogecoin-elon-musk-twitter/index.html',
)

contents = (scrape_cnn(cnn), scrape_brookings(brookings))

for content in contents:
    content.print()

