# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class GupiaoItem(scrapy.Item):
    xuhao = scrapy.Field()
    jysj = scrapy.Field()
    rz_ye = scrapy.Field()
    rz_mre = scrapy.Field()
    rz_che = scrapy.Field()
    rz_rzjmr = scrapy.Field()
    rq_yl = scrapy.Field()
    rq_mcl = scrapy.Field()
    rq_chl = scrapy.Field()
    rq_rzjmq = scrapy.Field()
    rq_rzrqye = scrapy.Field()

class IfengItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()









