# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FoodreviewItem(scrapy.Item):
    
    # define the fields for your item to crawl
    title = scrapy.Field()
    url = scrapy.Field() 
    img = scrapy.Field()
    rating = scrapy.Field()
    cuisine = scrapy.Field()
    location = scrapy.Field()

    pass





