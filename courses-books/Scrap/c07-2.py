import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

'''
Dont work for modern websites, maby use  Playwright or Selenium.
'''

class Content:
    """
    Common base class for all articles/pages
    """

    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.title = title
        self.body = body
        self.url = url

    def print(self):
        """
        Flexible printing function controls output
        """
        print(f'New article found for topic: {self.topic}')
        print(f'URL: {self.url}')
        print(f'TITLE: {self.title}')
        print(f'BODY:\n{self.body}')


class Website:
    """
    Contains information about website structure
    """

    def __init__(self, name, url, searchUrl, resultListing, 
            resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name  # Brookings
        self.url = url  # https://www.brookings.edu
        self.searchUrl = searchUrl  # https://www.brookings.edu/?s=
        # search results location
        self.resultListing = resultListing  # div.article-info
        # search result URL location
        self.resultUrl = resultUrl  # h4.title a
        # Whether it's a relative URL or not
        self.absoluteUrl = absoluteUrl  # True
        # HTML tag containing the title of an article
        self.titleTag = titleTag  # h1
        # HTML tag containing the body of an article
        self.bodyTag = bodyTag  # div.core-block


class Crawler:
    def __init__(self, website):
        self.site = website
        self.found = {}

    def getPage(url):
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            req = Request(url, headers=headers)
            resp = urlopen(req)
        except Exception as e:
            print(f'Page dont exist: {url}')
            return None
        return BeautifulSoup(resp, 'lxml')

    def safeGet(bs, selector):
        """
        Utilty function used to get a content string from a 
        Beautiful Soup object and a selector. Returns an empty string
        if no object is found for the given selector
        """
        selectedElems = bs.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        print('Selector not found')
        return ''

    def getContent(self, topic, url):
        """
        Extract content from a given page URL
        """
        bs = Crawler.getPage(url)
        if bs is not None:
            title = Crawler.safeGet(bs, self.site.titleTag)
            body = Crawler.safeGet(bs, self.site.bodyTag)
            return Content(topic, url, title, body)
        return Content(topic, url, '', '')

    def search(self, topic):
        """
        Searches a given website for a given topic and records all 
        pages found
        """
        bs = Crawler.getPage(self.site.searchUrl + topic)

        if bs:
            searchResults = bs.select(self.site.resultListing)

            for result in searchResults:
                url = result.select(self.site.resultUrl)[0].attrs['href']
                # Check to see whether it's a relative or an absolute URL
                url = url if self.site.absoluteUrl else self.site.url + url
                if url not in self.found:
                    self.found[url] = self.getContent(topic, url)
                self.found[url].print()



siteData = [
    [
        'Reuters', 
        'https://www.reuters.com',
        'https://www.reuters.com/site-search/?query=',
        'div.search-result-indiv',
        'h3.search-result-title a',
        False, 'h1', 'div.ArticleBodyWrapper'
    ],
    [
        'Brookings',
        'https://www.brookings.edu',
        'https://www.brookings.edu/?s=',
        'div.article-info',
        'h4.title a',
        True,
        'h1',
        'div.core-block'
    ]
]


sites = []
for name, url, search, rListing, rUrl, absUrl, tt, bt in siteData:
    sites.append(
            Website(name, url, search, rListing, rUrl, absUrl, tt, bt)
    )


crawlers = [Crawler(site) for site in sites]
topics = ['python', 'data%20science']


for topic in topics:
    for crawler in crawlers:
        crawler.search(topic)

