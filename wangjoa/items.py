# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WangjoaItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    location = scrapy.Field()
    location_detail = scrapy.Field()
    date = scrapy.Field()
    excerpt = scrapy.Field()
