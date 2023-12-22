# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# from scrapy.exceptions import DropItem
# from scrapy import logformatter
from pymongo import MongoClient


# Create MongoDB pipeline
class MongoDBPipeline:
   # Initialize the pipeline
   def __init__(self, mongo_url, mongo_db):
      self.mongo_uri = mongo_url
      self.mongo_db = mongo_db

   # Create MongoDB pipeline from crawler
   @classmethod
   def from_crawler(cls, crawler):
      return cls(
         mongo_url=crawler.settings.get('MONGO_URI'),
         mongo_db=crawler.settings.get('MONGO_DATABASE')
      )

   def open_spider(self, spider):
      self.client = MongoClient(self.mongo_uri)
      self.db = self.client[self.mongo_db]

   def close_spider(self, spider):
      self.client.close()

   def process_item(self, item, spider):
      self.db['scrapy_data'].insert_one(dict(item))
      return item

# Close the client









