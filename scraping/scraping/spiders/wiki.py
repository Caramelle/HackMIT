import scrapy
from scraping.items import WikiItem

class Wiki(scrapy.Spider):
    name='wiki'
    start_urls = [
            'https://en.wikipedia.org/wiki/List_of_American_films_of_2012',
            'https://en.wikipedia.org/wiki/List_of_American_films_of_2013',
            'https://en.wikipedia.org/wiki/List_of_American_films_of_2014',
            'https://en.wikipedia.org/wiki/List_of_American_films_of_2015'
            ]

    def parse(self, response):
        for title in response.xpath('//tr/td//i[1]/a/text()').extract():
            item=WikiItem()
            item['title']=title
            yield item

