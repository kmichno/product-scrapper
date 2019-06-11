import scrapy
from product_scrapper.items import ProductItem
from scrapy.utils.markup import replace_tags

class ProductAllegroSpider(scrapy.Spider):
    name = 'product_allegro'

    task_id = ""

    def __init__(self, phrase, task_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = ['http://allegro.pl/listing?string=%s' % phrase]
        self.task_id = task_id

    def parse(self, response):
        selector = scrapy.Selector(response)

        articles = selector.xpath(
            '/html/body/div[2]/div[3]/div/div/div/div/div/div[2]/div[1]/div[3]'
            '/div/div/div/div[2]/div[1]/div/section[2]/section/article/*')

        for a in articles:
            name = a.xpath('./div/div[2]/div[1]/h2/a/text()').get()
            description_with_tags = a.xpath('./div/div[2]/div[1]/div[2]/dl').get()
            description = ""
            if description_with_tags is not None:
                description = replace_tags(description_with_tags, " ")
            price = a.xpath('./div/div[2]/div[2]/div[1]/div/span/span/text()').get()
            url = a.xpath('./div/div[2]/div[1]/h2/a/@href').get()
            item = ProductItem()
            item['name'] = name
            item['price'] = price
            item['description'] = description
            item['url'] = url
            item['task_id'] = self.task_id
            yield item