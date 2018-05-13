import json
import time
import os
import hashlib
import requests
BASEPATH = r'D:\KUAISHOU'
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


def md5(content):
    m = hashlib.md5()
    m.update(content)
    return m.hexdigest()
def download(content):
    filename = os.path.join(BASEPATH, md5(content) + '.mp4')
    if os.path.exists(filename):
        pass
    else:
        f = open(filename, 'wb')
        f.write(content)
        f.close()
        print('{} done'.format(filename))

while True:
    r  = requests.post(url=START_URL,data=FORMDATA)
    time.sleep(1)
    if r.status_code == 200:
        # print('xxx')
        res = r.json()
        l = res['feeds']
        for dic in l:
            if dic.get('main_mv_urls'):
                mv_urls = dic.get('main_mv_urls')
                for mv_dic in mv_urls:
                    mv_url = mv_dic.get('url')
                    # yield scrapy.Request(url=mv_url, callback=self.parse_detail)
                    r = requests.get(mv_url)
                    download(r.content)
