# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WindyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    t = scrapy.Field()
    p = scrapy.Field()
    h = scrapy.Field()
    a = scrapy.Field()
    rt = scrapy.Field()
    hg = scrapy.Field()
    ag = scrapy.Field()
    st = scrapy.Field()

