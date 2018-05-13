import os
from scrapy.utils.request import request_fingerprint
from scrapy.dupefilters import RFPDupeFilter

class Myfilter(RFPDupeFilter):

    def request_seen(self, request):
        print('xxx',request.url)
        if request.url == 'http://api.gifshow.com/rest/n/feed/hot?mod=samsung(SM-G9350)&lon=121.490427&country_code=cn&did=ANDROID_3009047844075821&app=0&net=WIFI&oc=360APP&ud=0&c=360APP&sys=ANDROID_5.1.1&appver=5.6.4.6054&ftt=&language=zh-cn&iuid=&lat=31.241868&ver=5.6&max_memory=192':
            return False
        print('xxxxxxxxxxxxxx')
        fp = self.request_fingerprint(request)
        if fp in self.fingerprints:
            return True
        self.fingerprints.add(fp)
        if self.file:
            self.file.write(fp + os.linesep)


