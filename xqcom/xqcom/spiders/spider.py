# -*- coding: utf-8 -*-

# 抓取雪球股票
import json
import time
from scrapy.http import Request
from xqcom.items import StockItem,CommandItem
from scrapy.spiders import CrawlSpider
#from xqcom.settings import user_agent_list

#random_index = random.randint(0, len(user_agent_list) - 1 )
#random_agent = user_agent_list[random_index]
headers = {
    'Host': "xueqiu.com",
    'Accept-Language': "en,zh-CN;q=0.8,zh;q=0.6",
    'Accept-Encoding': "gzip, deflate, br",
    'Content-Type': "application/json;charset=UTF-8",
    'Connection': "keep-alive",
    'Cookie': 's=eu117etaa8; device_id=3610b97cf70102885b289bf37db37b9f; bid=e9a323e481ca9d25fbb151d80071ff7d_j4js6s57; webp=1; aliyungf_tc=AQAAAOGrmCaoogIA54FyypglJkcWgbM3; snbim_minify=true; Hm_lvt_63c1867417313f92f41e54d6ef61187d=1498822597,1500012239; Hm_lpvt_63c1867417313f92f41e54d6ef61187d=1500012239; xq_a_token=0a52c567442f1fdd8b09c27e0abb26438e274a7e; xq_r_token=43c6fed2d6b5cc8bc38cc9694c6c1cf121d38471; u=891500368114830; __utmt=1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1500338729,1500338731,1500362595,1500368022; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1500452314; __utma=1.99999208.1498822017.1500383258.1500451689.18; __utmb=1.3.10.1500451689; __utmc=1; __utmz=1.1500368022.16.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    'Referer': "https://xueqiu.com/5964068708",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

}

#STOCK_LIST = []

class Myspider1(CrawlSpider):

    name = 'stocklist'
    allowed_domains = ["xueqiu.com"]

    #global stock_list
    start_urls = ["https://xueqiu.com/stock/cata/stocklist.json?page=" + str(i) + "&size=30&order=desc&orderby=percent&type=11%2C12" for i in range(1, 177)]
    #print(start_urls)

    def make_requests_from_url(self, url):
        request = Request(url, dont_filter=True, headers=headers)
        request.meta["start_urls"] = url
        #print(request)
        return request

    def parse(self, response):
        try:
            for stock in json.loads(response.body.decode())["stocks"]:
                #STOCK_LIST.append(stock['name'])
                #print(stock_list)
                #print(stock)
                for page_id in range(1, 101):
                    item = StockItem()
                    item['symbol'] = stock['symbol']
                    item['url'] = "https://xueqiu.com/statuses/search.json?count=10&comment=0&symbol=" + stock['symbol'] + "&hl=0&source=user&page=" + str(page_id)
                    item['name'] = stock['name']
                    #print(item['name'])
                    yield item

        except:
            print('获取失败，准备重新获取')
            time.sleep(2)
