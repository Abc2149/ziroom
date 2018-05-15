# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZiroomItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    area = scrapy.Field()
    face = scrapy.Field()
    house_ty = scrapy.Field()
    floor = scrapy.Field()
    price = scrapy.Field()
    crawled = scrapy.Field()
    spider = scrapy.Field()
