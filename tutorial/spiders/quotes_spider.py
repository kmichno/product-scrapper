import scrapy
import re
from scrapy.selector import Selector


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.ceneo.pl/Biuro_i_firma',
    ]

    def parse(self, response):
        phrase = "Brother Ton"
        for quote in response.xpath('//div[@class="cat-prod-row-body"]'):
            regexp = re.compile(phrase)
            product_name = quote.xpath('.//strong[@class="cat-prod-row-name"]/a//text()').extract_first()
            if regexp.search(product_name):
                yield {
                    'text': product_name, 
                    'price': quote.xpath('.//span[@class="value"]//text()').extract_first() + quote.xpath('.//span[@class="penny"]//text()').extract_first(),
                    'link': quote.xpath('.//strong[@class="cat-prod-row-name"]/a/@href').extract_first()
                }

        next_page = response.css('.pagination .arrow-next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
