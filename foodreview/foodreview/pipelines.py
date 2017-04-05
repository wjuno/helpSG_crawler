# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

###  Uncomment if using Postgres ###
# from models import YelpDetailRecord


class FoodreviewPipeline(object):
    def process_item(self, item, spider):

# UNCOMMENT for storage into the database (Postgres)
      # product = YelpDetailRecord(
      #       title=item['title'],
      #       url=item['url'],
      #       img=item['img'],
      #       rating=item['rating'],
      #       cuisine=item['cuisine'],
      #       location=item['location'])
      # product_id = product.save()


      return item
