# -*- coding: utf-8 -*-

# 抓取雪球股票评论

import json
import time
import motor.motor_tornado
from scrapy.http import Request
from xqtest.items import CommandItem
from xqtest.pipelines import StockComPipeline
from scrapy.conf import settings
import pymongo
from scrapy.spiders import CrawlSpider
headers = {
    'Cookie':'aliyungf_tc=AQAAADbt5i4VGAUAQoFyyjO+M0UZVVvf; xq_a_token.sig=ePJ2E1I4Vs61a-ca9_QGMPXk7lQ; xq_r_token.sig=QT8O3-NHYfv1eUBoxGfbDDgEaNU; device_id=692046735d6054c556cb0b211a780225; Hm_lvt_1db88642e346389874251b5a1eded6e3=1500458400; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1500460270; s=f514l1b4u2; bid=e9a323e481ca9d25fbb151d80071ff7d_j5au9ixp; xq_a_token=f7c7f5dc15c224878fcddd7709ef732ffb156b21; xq_r_token=66993cd1844f111397b0cc222d2d3546bee7d595; u=6272194048; remember=1; remember.sig=K4F3faYzmVuqC0iXIERCQf55g2Y; xq_is_login=1; xq_is_login.sig=J3LxgPVPUzbBg3Kee_PquUfih7Q; u.sig=0PtlEgOiOEI4j8B9JhoFXLVCZn8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0',
}

class Myspider2(CrawlSpider):


    def __init__(self):
        self.num = 1

    name = 'stockcom'

    allowed_domains = ["xueqiu.com"]

    start_urls =["https://xueqiu.com/statuses/search.json?count=10&comment=0&symbol=SH603612&hl=0&source=all&sort=alpha&page=1"]


    def make_requests_from_url(self, url):
        request = Request(url, dont_filter=True, headers=headers)
        request.meta["start_urls"] = url
        return request

    """
    def start_requests(self):
        return [scrapy.Request('https://xueqiu.com/snowman/login', headers=headers, callback=self.login)]

    def login(self, response):
        response_text = response.text
        post_url = "https://xueqiu.com/snowman/login"
        post_data = {
            'username':'1105638842@qq.com',
            'password':'521llxzldjy',
            'remember_me':'false',
            }

        return [scrapy.FormRequest(
                url = post_url,
                formdata = post_data,
                headers=headers,
                callback=self.get_url,
            )]

    def get_url(self, response):
        # 验证服务器的返回数据判断是否成功
        start_urls = [
            "https://xueqiu.com/statuses/search.json?count=10&comment=0&symbol=SH603612&hl=0&source=all&sort=alpha&page=2"]

        for url in start_urls:
            request = Request(url, dont_filter=True, headers=headers)
            #request.meta["start_urls"] = url
            # print(request)
            return request

"""

    def parse(self, response):

        try:
            for com in json.loads(response.body.decode())["list"]:

                #print(com)
                item = CommandItem()
                item['id'] = com['id']
                item['user_id'] = com['user_id']
                item['time'] = com['timeBefore']
                item['command'] = com['text']
                #print(item)
                yield item

            client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
            db = client[settings['MONGO_DB']]  # 获得数据库的句柄
            coll = db[settings['MONGO_COLL']]

            urls = coll.find({}, {"url": 1, "_id": 0}).skip(self.num).limit(1)
            # print(urls)
            for url_list in urls:
                url = url_list["url"]
                print(url)

            if self.num < 528001:
                #count = count + 1
                self.num = self.num + 1
                yield Request(url, callback=self.parse, headers=headers, dont_filter=True)


        except:
            print('获取失败，准备重新获取')
            time.sleep(2)
    """
    @staticmethod
    def get_url(self):

        client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        db = client[settings['MONGO_DB']]  # 获得数据库的句柄
        coll = db[settings['MONGO_COLL']]
        urls = coll.find({}, {"url": 1, "_id": 0}).skip(self.num).limit(1)
        # print(urls)
        for url_list in urls:
            urlname = url_list["url"]
            #print(urlname)
            #print(type(urlname))
        #return urlname


    def parse(self, response):
        try:
            #stockid= json.loads(response.body.decode())["symbol"]

            for com in json.loads(response.body.decode())["list"]:

                item = CommandItem()
                item['count'] = com['count']
                print(item['count'])
                #item['stockname'] = stockid
                item['id'] = com['id']
                print(item['id'])
                item['user_id'] = com['user_id']
                print(item['user_id'])
                item['time'] = com['timeBefore']
                print(item['time'])
                item['command'] = com['text']
                print(item['text'])
                yield item
                #for num in range(0,10):
                #    urls = self.db.xqcom.find({}, {"url": 1}).skip(num).limit(1)
                #   url = json.loads(urls)["url"]
                #  yield Request(url, callback=self.parse, headers=headers)

        except:
            print('获取失败，准备重新获取')
            time.sleep(2)
"""
