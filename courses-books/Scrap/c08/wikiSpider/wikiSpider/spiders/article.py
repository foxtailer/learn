from scrapy import Spider

#  scrapy runspider wikiSpider/spiders/articles.py
class ArticleSpider(Spider):
    name = 'article'

    start_urls = [
        'https://en.wikipedia.org/wiki/Python_%28programming_language%29',
        'https://en.wikipedia.org/wiki/Functional_programming',
        'https://en.wikipedia.org/wiki/Monty_Python'
    ]

    def parse(self, response):
        url = response.url
        title = response.css('.mw-page-title-main::text').get()

        print(f'URL is: {url}')
        print(f'Title is: {title}')
