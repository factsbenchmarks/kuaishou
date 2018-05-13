# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import time
import os
BASEPATH = r'D:\KUAISHOU'
class KuaishouPipeline(object):
    def process_item(self, item, spider):
        # mv_url = item.get('url')
        # r = requests.get(url=mv_url)
        # filename = os.path.join(BASEPATH,str(time.time())+'.mp4')
        # f = open(filename,'wb')
        # f.write(r.content)
        # f.close()
        #
        pass
