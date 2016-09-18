import scrapy
from scraping.items import WikiItem
import re

class Imdb(scrapy.Spider):
    name='imdb'
    start_urls = [
            'http://www.imdb.com/movies-coming-soon/'
            ]

    def parse(self, response):
        for title in response.xpath('//h4[@itemprop="name"]/a/text()').extract():
                item = WikiItem()	
                m = re.match(r'( )(.*) (\(\d\d\d\d\))', title)
                item['title'] = m.group(2)
                yield item
