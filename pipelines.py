# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# importing mongodb library for python
import pymongo

class SamplePipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient(
                'localhost',
                27017
                )
        db = self.conn['quotes']
        self.collection = db['quotes_tb']

    def process_item(self, item, spider):

        self.collection.insert_one(dict(item))

        print('pipelines: '+item['title'][0])
        return item
