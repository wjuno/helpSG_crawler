# coding: utf-8
# -*- coding: utf-8 -*-
import scrapy
import urllib2  
from foodreview.items import FoodreviewItem
import re




import bs4
import string
from scrapy import Request
from scrapy.selector import Selector
from random import randint



class FoodReviewSpider(scrapy.Spider):
    name = 'yelppyDetails_review'
    allowed_domains = ['www.yelp.com.sg']

    start_urls = []



    with open("yelp_url.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]




    def parse(self, response):


        # list of reviews
        XPATH_OUTER_REVIEW = '//*[@class="review-content"]/p[text()]'
        reviews = response.xpath(XPATH_OUTER_REVIEW)

      
        count = 0

        XPATH_REVIEW = '//*[@class="review-content"]/p'


        XPATH_TITLE = '//*[@id="wrap"]/div[4]/div/div[1]/div/div[3]/div[1]/div[1]/h1/text()'
      

        for rev in reviews:
            RAW_REVIEW = rev.xpath(XPATH_REVIEW).extract()[count]
            REVIEW = ' '.join(''.join(RAW_REVIEW).split()) if RAW_REVIEW else None
            REVIEW = REVIEW.replace('<p lang=\"en\">','')
            REVIEW = REVIEW.replace('</p>','')
            REVIEW = REVIEW.replace('<br>','')
            REVIEW = re.sub('<[^>]*>', '', REVIEW)

          


            RAW_TITLE = response.xpath(XPATH_TITLE).extract()
            TITLE = ' '.join(''.join(RAW_TITLE).encode('utf-8').split()) if RAW_TITLE else None
         
            URL = response.url.strip()

             
            items = FoodreviewItem()
            items['title'] = TITLE
            items['review'] = REVIEW
            items['url'] = URL
       

            count += 1   
            yield items



        NEXT_PAGE_SELECTOR = '//div[@class="arrange_unit"]/a[@class="u-decoration-none next pagination-links_anchor"]/@href'

        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract()
        next_page = ' '.join(''.join(next_page).encode('utf-8').split()) if next_page else None
        
    
        if next_page:
            yield scrapy.Request(
                next_page,
                callback=self.parse
            )



        

      




      


        
        
        

        
        
   





        

        

           
