from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import sys

from product_scrapper.spiders.product_ceneo_spider import ProductCeneoSpider

process = CrawlerProcess(get_project_settings())
process.crawl('product_ceneo', phrase=sys.argv[1], task_id=sys.argv[2])
process.crawl('product_allegro', phrase=sys.argv[1], task_id=sys.argv[2])
process.start()