# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

from scrapy.item import Item, Field


class ProductItem(Item):
    name = Field()
    url = Field()
    image_url = Field()
    description = Field()
    price = Field()
