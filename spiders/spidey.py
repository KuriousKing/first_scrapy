import scrapy
from ..items import SampleItem

class quotes(scrapy.Spider):
    name='quote'
    page=2   
    start_urls=[
        'https://quotes.toscrape.com/page/1/'
    ]
    
    def parse(self, response):
        items = SampleItem()

        all_div = response.css('div.quote')

        for quotes in all_div:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tags = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            yield  items

        next_page = f'https://quotes.toscrape.com/page/{str(self.page)}/'


        if self.page<11:
            self.page+=1
            yield response.follow(next_page, callback=self.parse)
