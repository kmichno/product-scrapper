import scrapy
import re
from tutorial.items import ProductItem
from scrapy.selector import Selector

class ProductCeneoSpider(scrapy.Spider):
    name = "product_ceneo"
    start_urls = [
        'https://www.ceneo.pl/59096052',
        'https://www.ceneo.pl/44279952',
        'https://www.ceneo.pl/26740026'
    ]

    def parse(self, response):
        product_name = response.xpath('.//h1//text()').extract_first()
        item = ProductItem()
        item['name'] = product_name
        item['description'] = response.xpath('.//div[@class="ProductSublineTags"]//text()').extract_first()
        item['price'] = response.xpath('.//span[@class="value"]//text()').extract_first() + response.xpath('.//span[@class="penny"]//text()').extract_first()
        item['url'] = response.xpath('.//strong[@class="cat-prod-row-name"]/a/@href').extract_first()
        yield item

