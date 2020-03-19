# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from ca_covid_county_spiders.utils.markdown import markdownIt


# Items

class CaCovidCountySpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ContentItem(scrapy.Item):
    spider = scrapy.Field()
    hash = scrapy.Field()
    uri = scrapy.Field()
    time = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    





# Item Loaders

class ContentLoader(ItemLoader):
    default_item_class = ContentItem
    default_output_processor = TakeFirst()
    
    title_in = MapCompose(markdownIt, str.lstrip, str.rstrip)
    content_in = MapCompose(markdownIt, str.lstrip, str.rstrip)
    
    
    
    
    
