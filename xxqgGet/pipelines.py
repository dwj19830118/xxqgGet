# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import time
import os.path
import re
class XxqggetPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        fileName = today + '.txt'
        #开始格式化处理问题和答案
        outStr = '\r\n'.join(item["question"].split('^'))
        with codecs.open(fileName,'a',encoding='utf-8') as fp:
                fp.write(outStr)
        time.sleep(1)
        return item
