# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

### uncomment for postgres database ###
# from models_review import YelpDetailRecord


class FoodreviewPipeline(object):
    def process_item(self, item, spider):

      #### Review #####
      	# product = YelpDetailRecord(
       #      title=item['title'],
       #      review=item['review'],
       #      rating=item['rating'],
       #      url=item['url'])
       #  product_id = product.save()


        return item
