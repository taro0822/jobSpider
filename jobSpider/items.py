# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobspiderItem(scrapy.Item):
    # define the fields for your item here like:
    keyword = scrapy.Field()
    title = scrapy.Field()
    salary = scrapy.Field()
    link = scrapy.Field()
    city = scrapy.Field()
    edu = scrapy.Field()
    experience = scrapy.Field()
    company = scrapy.Field()
    # description = scrapy.Field()