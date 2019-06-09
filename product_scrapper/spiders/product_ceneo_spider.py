import scrapy
import re
from scrapy.selector import Selector
from product_scrapper.items import ProductItem

class ProductCeneoSpider(scrapy.Spider):
    name = "product_ceneo"
    start_urls = [
        'https://www.ceneo.pl'
    ]
    phrase = ""
    task_id = ""

    def __init__(self, phrase, task_id, *args, **kwargs):
        super(ProductCeneoSpider, self).__init__(*args, **kwargs)
        self.phrase = phrase
        self.task_id = task_id

    def closed(self, reason):
        print("Koniec dzialania")
        # koniec działania spidera
        # zmienić status na zakończone zadanie

    def parse(self, response):
        for category_item in response.css('#categories-menu .cat-item'):
            category_link = category_item.css('a.cat-link::attr(href)').get()
            if category_link is not None:
                category_link = response.urljoin(category_link)
                yield scrapy.Request(category_link, callback=self.parse_category)

    def parse_category(self, response):
        for product in response.xpath('//div[@class="cat-prod-row-body"]'):
            regexp = re.compile(self.phrase)
            product_name = product.xpath('.//strong[@class="cat-prod-row-name"]/a//text()').extract_first()
            if regexp.search(product_name):
                next_page = product.css('.cat-prod-row-name a::attr(href)').get()
                if next_page is not None:
                    next_page = response.urljoin(next_page)
                    yield scrapy.Request(next_page, callback=self.parse_link)

        # przejście do następnej strony - zakomentowane tymczasowo, żeby długo się nie robiło
        # next_page = response.css('.pagination .arrow-next a::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

    def parse_link(self, response):
        product_name = response.xpath('.//h1//text()').extract_first()
        item = ProductItem()
        item['name'] = product_name
        item['description'] = response.xpath('.//div[@class="ProductSublineTags"]//text()').extract_first()
        item['price'] = response.xpath('.//span[@class="value"]//text()').extract_first() + response.xpath('.//span[@class="penny"]//text()').extract_first()
        item['url'] = response.request.url,
        item['task_id'] = self.task_id
        yield item