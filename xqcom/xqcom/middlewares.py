# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
from scrapy import signals
from fake_useragent import UserAgent
#from xqcom.settings import IPPOOL

class XqcomSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class RandomUserAgentMiddlware(object):
    #随机更换user_agent

    def __init__(self, crawler):
        super(RandomUserAgentMiddlware, self).__init__()
        self.ua = UserAgent()



    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        return cls(crawler)

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', self.ua.random)
        return None


class ProxyMiddleware(object):
    def __init__(self):
        self.count = 200
    proxyList = ['36.250.69.4:80',
                 '58.18.52.168:3128',
                 '58.253.238.243:80',
                 '60.191.164.22:3128',
                 '60.191.167.93:3128',
                 '61.129.70.131:8080',
                '61.152.81.193: 9100',
                '120.204.85.29: 3128',
                '219.228.126.86: 8123',
                '61.152.81.193: 9100',
                '218.82.33.225: 5385',
                '122.72.32.72: 80',
                '111.155.116.247: 8123',
                '171.38.26.233: 8123',
                '110.72.25.32: 8123',
                '110.73.4.136: 8123',
                '110.73.5.53: 8123',
                '182.88.129.185: 8123',
    ]

    def process_request(self, request, spider):
        # Set the location of the proxy
        pro_adr = random.choice(self.proxyList)
        print ("USE PROXY -> " + pro_adr)
        request.meta['proxy'] = "http://" + pro_adr

