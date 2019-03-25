 # -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


#scraped data -> itme container -> json/files
#scraped data  ---> item container ---> pipeline ->SQL DB

class BankdataPipeline(object):

    def process_item(self, item, spider):


        print ("Pipeline :" + item['title'][0])

        return item






