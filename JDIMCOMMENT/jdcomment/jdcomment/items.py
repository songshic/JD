# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdcommentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    username = scrapy.Field()
    userid = scrapy.Field()
    userLevelName = scrapy.Field()
    referenceName = scrapy.Field()
    referenceTime = scrapy.Field()
    content = scrapy.Field()
    creationTime = scrapy.Field()
    score = scrapy.Field()


