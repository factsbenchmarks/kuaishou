# -*- coding: utf-8 -*-
import scrapy
import json
import time
import os
import hashlib
from scrapy.spidermiddlewares.httperror import IgnoreRequest
BASEPATH = r'D:\KUAISHOU'
# from kuaishou.items import *
START_URL = 'http://api.gifshow.com/rest/n/feed/hot?mod=samsung(SM-G9350)&lon=121.490427&country_code=cn&did=ANDROID_3009047844075821&app=0&net=WIFI&oc=360APP&ud=0&c=360APP&sys=ANDROID_5.1.1&appver=5.6.4.6054&ftt=&language=zh-cn&iuid=&lat=31.241868&ver=5.6&max_memory=192'
FORMDATA = {
    'type': '7',
    'page': '2',
    'coldStart': 'false',
    'count': '20',
    'pv': 'false',
    'id': '3',
    'refreshTimes': '2',
    'pcursor': '1',
    'source': '1',
    'extInfo': '',
    'client_key': '3c2cd3f3',
    'os': 'android',
    'sig': '7fc50a5744346b5f3242329cec7ce4c8',

}
class KuaiSpider(scrapy.Spider):
    name = 'kuai'
    # allowed_domains = ['www.kuai.com']
    # start_urls = ['http://www.kuai.com/']
    def start_requests(self):
        print('11111111')
        yield scrapy.FormRequest(url=START_URL,formdata=FORMDATA)
    def parse(self, response):
        res = json.loads(response.text)
        l = res['feeds']
        for dic in l:
            if dic.get('main_mv_urls'):
                mv_urls = dic.get('main_mv_urls')
                for mv_dic in mv_urls:
                    mv_url = mv_dic.get('url')
                    yield scrapy.Request(url=mv_url,callback=self.parse_detail)
        time.sleep(2)
        print('2222')
        yield scrapy.FormRequest(url=START_URL,formdata=FORMDATA,dont_filter=True,headers={'referer':None})
    def parse_detail(self,response):
        content = response.body
        filename = os.path.join(BASEPATH, self.md5(content) + '.mp4')
        if os.path.exists(filename):
            pass
        else:
            f = open(filename,'wb')
            f.write(content)
            f.close()
            print('{} done'.format(filename))
    def md5(self,content):
        m = hashlib.md5()
        m.update(content)
        return m.hexdigest()
