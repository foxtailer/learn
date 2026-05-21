import re
import random
from urllib.request import urlopen, Request
from urllib.parse import urlparse 
from bs4 import BeautifulSoup



def get_random_external_link(url: str): 

    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    req = Request(url, headers=headers)
    resp = urlopen(req)
    bs = BeautifulSoup(resp, 'lxml')
    
    external_links = get_external_links(bs, url)                       

    if not len(external_links):                                              
        print('No external links, looking around the site for one')         
        internal_links = get_internal_links(bs, url)                  
        return get_random_external_link(random.choice(internal_links))          
    else:                                                                   
        return random.choice(external_links)


def get_internal_links(bs, url: str):
    netloc = urlparse(url).netloc
    scheme = urlparse(url).scheme
    links = set()

    for link in bs.find_all('a'):
        if not link.get('href'):
            continue
        parsed = urlparse(link.attrs['href'])

        if parsed.netloc == '':
            links.add(
                f'{scheme}://{netloc}/{link.attrs["href"].strip("/")}'
            )
        elif parsed.netloc == netloc:
            links.add(link.attrs['href'])

    return list(links)
        


def get_external_links(bs, url):
    netloc = urlparse(url).netloc
    links = set()

    for link in bs.find_all('a'):
        if not link.attrs.get('href'):
            continue

        parsed = urlparse(link.attrs['href'])

        if parsed.netloc != '' and parsed.netloc != netloc:
            links.add(link.attrs['href'])

    return list(links)


def follow_external_only(url):
    external_link = get_random_external_link(url)
    print(f'Random external link is: {external_link}')
    follow_external_only(external_link)


url = 'https://en.wikipedia.org'


follow_external_only(url)

