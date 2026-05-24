import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


class Website:
    def __init__(self, name, url, targetPattern, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.targetPattern = targetPattern  # link_pattern
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag  # content_title
        self.bodyTag = bodyTag  # content_body


class Content:
    def __init__(self, url, author, quote):
        self.url = url
        self.author = author
        self.quote = quote

    def print(self):
        print(f'URL: {self.url}')
        print(f'AUTHOR: {self.author}')
        print(f'QUOTE:\n{self.quote}')


class Crawler:
    def __init__(self, website):
        self.site = website
        self.visited = {}

    def getPage(url):
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            req = Request(url, headers=headers)
            resp = urlopen(req)
        except Exception as e:
            print(f'Page dont exist: {url}')
            return None
        return BeautifulSoup(resp, 'lxml')

    def getText(bs, selector):
        selectedElems = bs.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    def getContent(self, url):
        """
        Extract content from a given page URL
        """
        bs = Crawler.getPage(url)
        paga_qotes = []
        if bs is not None:
            qotes = bs.select('div.wrap-block')
            for qote in qotes:
                author = Crawler.getText(qote, self.site.titleTag)
                quote = Crawler.getText(qote, self.site.bodyTag)
                paga_qotes.append(Content(url, author, quote))
        return paga_qotes

    def crawl(self):
        """
        Get pages from website home page
        """
        bs = Crawler.getPage(self.site.url)
        targetPages = bs.findAll('a', href=re.compile(self.site.targetPattern))

        # Crawl only one page?
        for targetPage in targetPages:
            url = targetPage.attrs['href']
            if url:
                url = url if self.site.absoluteUrl else \
                    f'{self.site.url}{url}'
            else:
                continue
            if url not in self.visited:
                self.visited[url] = self.getContent(url)
                for q in self.visited[url]:
                    q.print()

brookings = Website(
    'Brookings',
    'https://www.azquotes.com',
    '\/(author|quotes\/topics)\/',
    False,
    'div.author',
    'a.title'
)
crawler = Crawler(brookings)
crawler.crawl()