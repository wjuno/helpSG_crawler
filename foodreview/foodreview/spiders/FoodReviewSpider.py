# coding: utf-8
# -*- coding: utf-8 -*-
import scrapy
import urllib2  
from foodreview.items import FoodreviewItem

import bs4
import string
from scrapy import Request
from scrapy.selector import HtmlXPathSelector
from random import randint
import re



class FoodReviewSpider(scrapy.Spider):
    name = 'yelppy'
    allowed_domains = ['https://www.yelp.com.sg']


    start_urls = 'https://www.yelp.com.sg/search?find_loc=Singapore&start={page}0&cflt=restaurants'
  
    def start_requests(self):
        index = 0
        while True:
            yield Request(self.start_urls.format(page=index))
            index +=1


    def parse(self, response):


        XPATH_OUTER_DIV = '//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]/li/div'
        divs = response.xpath(XPATH_OUTER_DIV)


        XPATH_IMAGE = '//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]/li/div/div[1]/div[1]/div/div[1]/div/a/img/@src'

        XPATH_TITLE = '//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]/li/div/div[1]/div[1]/div/div[2]/h3/span/a/span/text()'

        XPATH_URL = '//div[@class="search-result natural-search-result"]/div[2]/div[@class="media-story"]/p/a/@href'

        XPATH_CUISINE = '//div[@class="price-category"]/span[@class="category-str-list"]'

        XPATH_RATING = '//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]/li/div/div[1]/div[1]/div/div[2]/div[1]/div/@title'


        XPATH_LOCATION = '//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]/li/div/div[1]/div[2]'

       


        count = 0
        for div in divs:
            RAW_IMG = div.xpath(XPATH_IMAGE).extract()[count]
            RAW_TITLE = div.xpath(XPATH_TITLE).extract()[count]
            RAW_URL = div.xpath(XPATH_URL).extract()[count]
            RAW_RATING = div.xpath(XPATH_RATING).extract()[count]
            RAW_CUISINE = div.xpath(XPATH_CUISINE).extract()[count]
            RAW_LOCATION = div.xpath(XPATH_LOCATION).extract()[count]
            

            IMG = ' '.join(''.join(RAW_IMG).encode('utf-8').split()) if RAW_IMG else None
            TITLE = ' '.join(''.join(RAW_TITLE).encode('utf-8').split()) if RAW_TITLE else None
            URL = ' '.join(''.join(RAW_URL).encode('utf-8').split()) if RAW_URL else None
            RATING = ' '.join(''.join(RAW_RATING).encode('utf-8').split()) if RAW_RATING else None
            RATING = RATING.replace(' star rating','')

            CUISINE = ' '.join(''.join(RAW_CUISINE).encode('utf-8').split()) if RAW_CUISINE else None
            CUISINE = CUISINE.replace('<span class=\"category-str-list\">','')
            CUISINE = CUISINE.replace('</span>','')
            CUISINE = CUISINE.replace('</a>','')
            CUISINE = re.sub('<a href[^>]*>', '', CUISINE)

            LOCATION = ' '.join(''.join(RAW_LOCATION).encode('utf-8').split()) if RAW_LOCATION else None
            LOCATION = re.sub('<[^>]*>', '', LOCATION)



            
            domain = 'https://www.yelp.com.sg'
            items = FoodreviewItem()
            items['title'] = TITLE
            items['url'] = domain + URL
            items['img'] = IMG
            items['rating'] = RATING
            items['cuisine'] = CUISINE
            items['location'] = LOCATION

     
            count += 1
            yield items

           
