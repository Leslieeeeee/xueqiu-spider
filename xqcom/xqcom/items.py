# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    symbol = scrapy.Field()
    url = scrapy.Field()

class CommandItem(scrapy.Item):
    #stockname = scrapy.Field()
    id = scrapy.Field()
    command = scrapy.Field()
    time = scrapy.Field()
    user_id = scrapy.Field()
    count = scrapy.Field()

