# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ProductItem(Item):
    name = Field()
    url = Field()
    image_url = Field()
    description = Field()
    price = Field()
    task_id = Field()
