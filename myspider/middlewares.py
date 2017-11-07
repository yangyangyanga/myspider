# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random

PROXY_IP = [
    '122.224.227.202:3128',
    '183.23.74.63:9000',
    '163.125.241.147:9999',
    '183.23.74.63:9000',
    '180.173.52.202:53281',
    '118.178.124.33:3128',
    '202.38.92.100:3128',
    '119.90.63.3:3128',
    '122.72.18.34:80',
    '124.232.148.7:3128',
    '180.168.179.193:8080',
    '122.72.18.61:80',
    '118.31.103.7:3128',
    '139.224.24.26:8888',
    '222.82.248.74:53281',
    '116.25.103.102:9999',
    '113.247.107.110:8080',
    '121.43.178.58:3128',
    '222.221.187.26:9999',
    '110.52.8.109:53281',
    '121.8.170.53:9797',
    '218.56.132.156:8080',
]

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) ',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)" ',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
]
'''
class MyspiderSpiderMiddleware(object):
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

'''
class ProxyMiddleware(object):
    # def process_request(self, request, spider):
    #     user_agent = random.choice(USER_AGENTS)
    #     ip = 'http://' + random.choice(PROXY_IP)
    #     print('user_agent ====================' + user_agent)
    #     request.headers.setdefault("User-Agent", user_agent)
    #     request.meta['proxy'] = ip

    def process_response(self, request, response, spider):
        print('process_response ======================')
        # print(request.headers)
        # print(request.meta)
        # print(response.text)
        return response
    def process_exception(self, request, exception, spider):
        print('process_exception ===========================')
        print(exception)