from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from wikiSpider.items import Article

# scrapy runspider wikiSpider/spiders/articles.py --loglevel ERROR
# scrapy crawl articleItems -o articles.csv --loglevel ERROR
class ArticleSpider(CrawlSpider):
    name = 'articleItems'
    allowed_domains = ['wikipedia.org']

    start_urls = [
        'https://en.wikipedia.org/wiki/Benevolent_dictator_for_life'
    ]

    rules = (
        Rule(
            LinkExtractor(
                allow=r'/wiki/',
                deny=(
                    r'/wiki/Special:',
                    r'/wiki/Help:',
                    r'/wiki/File:',
                    r'/wiki/Category:',
                    r'/wiki/Talk:',
                )
            ),
            callback='parse_items',
            follow=True
        ),
    )

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css('span.mw-page-title-main::text').get()
        article['title'] = response.css('div.mw-content-ltr.mw-parser-output p::text').getall()
        # article['text'] = response.xpath('//div[@id=''"mw-content-text"]//text()').extract()
        lastUpdated = response.css('li#footer-info-lastmod::text'
).extract_first()
        article['lastUpdated'] = lastUpdated.replace('This page was '
'last edited on ', '')
        return article



"""
    def parse_items(self, response):
        url = response.url

        title = response.css(
            'span.mw-page-title-main::text'
        ).get()

        text = response.xpath(
            '//div[@id="mw-content-text"]//text()'
        ).getall()

        last_updated = response.css(
            'li#footer-info-lastmod::text'
        ).get()

        if last_updated:
            last_updated = last_updated.replace(
                'This page was last edited on ',
                ''
            ).strip()

        print(f'URL is: {url}')
        print(f'Title is: {title}')
        print(f'Text length: {len(text)}')
        print(f'Last updated: {last_updated}')
        print('-' * 50)
"""

