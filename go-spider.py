from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from product_scrapper.spiders.product_ceneo_spider import ProductCeneoSpider


process = CrawlerProcess(get_project_settings())
process.crawl('product_ceneo', phrase='Brother', task_id='1')
process.start()
