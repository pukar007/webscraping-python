# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html




#temporary data - temporary container items


import scrapy


class BankdataItem(scrapy.Item):

    # define the fields for your item here like:
    title = scrapy.Field()
    sno = scrapy.Field()
    particulars = scrapy.Field()
    details = scrapy.Field()
    charges = scrapy.Field()

    pass
