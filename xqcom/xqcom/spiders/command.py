# -*- coding: utf-8 -*-

# 抓取雪球股票评论

import json
import time
import random
from scrapy.http import Request
from xqcom.items import CommandItem
from xqcom import settings
import pymongo
from scrapy.spiders import CrawlSpider

headers = {
    'Host': "xueqiu.com",
    'Accept-Language': "en,zh-CN;q=0.8,zh;q=0.6",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/json;charset=UTF-8",
    'Connection': "keep-alive",
    'Cookie': "s=eu117etaa8; device_id=3610b97cf70102885b289bf37db37b9f; bid=e9a323e481ca9d25fbb151d80071ff7d_j4js6s57; Hm_lvt_63c1867417313f92f41e54d6ef61187d=1498822597; aliyungf_tc=AQAAANnkrU+IEAQApJNgtnM3aaXtZzFX; snbim_minify=true; xq_a_token=0a52c567442f1fdd8b09c27e0abb26438e274a7e; xq_a_token.sig=dR_XY4cJjuYM6ujKxH735NKcOpw; xq_r_token=43c6fed2d6b5cc8bc38cc9694c6c1cf121d38471; xq_r_token.sig=8d4jOYdZXEWqSBXOB9N5KuMMZq8; u=371499308556711; __utmt=1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1498549773,1498549780,1498812257,1499307901; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1499309150; __utma=1.99999208.1498822017.1499060218.1499307901.3; __utmb=1.8.10.1499307901; __utmc=1; __utmz=1.1498822017.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    #'Referer': "https://xueqiu.com/5964068708",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

}

class Myspider2(CrawlSpider):

    name = 'stockcom'
    allowed_domains = ["xueqiu.com"]

    #client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
    #db = client[settings['MONGO_DB']]  # 获得数据库的句柄
    #coll = db[settings['MONGO_COLL1']]

    start_urls =["https://xueqiu.com/statuses/search.json?count=10&comment=0&symbol=SZ000975&hl=0&source=user&page=1"]



    def make_requests_from_url(self, url):

        request = Request(url, dont_filter=True, headers=headers)
        request.meta["start_urls"] = url
        print(request)
        return request

    def parse(self, response):
        try:
            for com in json.loads(response.body.decode())["list"]:
                item = CommandItem()
                item['id'] = com['id']
                item['user_id'] = com['user_id']
                item['time'] = com['time']
                item['command'] = com['text']
                yield item
        except:
            print('获取失败，准备重新获取')
            time.sleep(2)

"""
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
                #   yield Request(url, callback=self.parse, headers=headers)

        except:
            print('获取失败，准备重新获取')
            time.sleep(2)
"""