# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class JobspiderPipeline(object):
    def __init__(self):
        # 将爬取到的数据存入python.json文件中
        self.file = open('python.json','wb')

    def process_item(self, item, spider):
        line = str(item)
        self.file.write(line.encode('utf-8') + "\n".encode('utf-8'))
        return item
