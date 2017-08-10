# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CommandItem(scrapy.Item):
    #stockname = scrapy.Field()
    id = scrapy.Field()
    command = scrapy.Field()
    time = scrapy.Field()
    user_id = scrapy.Field()
