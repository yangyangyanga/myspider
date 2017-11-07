from scrapy.linkextractors import LinkExtractor
import scrapy
import time
from myspider.items import IfengItem

class SinaSpider(scrapy.Spider):
    name = 'sina'
    start_urls = ['http://www.sina.com.cn/']

    def parse(self, response):
        # 使用LinkExtractor过滤新浪网的一些链接
        new_link_list = LinkExtractor(allow=r'news.sina.com').extract_links(response)
        sports_link_list = LinkExtractor(allow=r'sports.sina.com.cn/nba/').extract_links(response)

        # 每个得到的是个类对象
        for new_link in new_link_list:
            print(new_link.url)
            print(new_link.text)
            # print(type(new_list.text))
        for sport_list in sports_link_list:
            print(sport_list.url)
            print(sport_list.text)
        # print(response.text)

class IfengSpider(scrapy.Spider):
    name = 'ifeng'
    start_urls = ['http://www.ifeng.com/']
    custom_settings = {
        'ITEM_PIPELINES': {'myspider.pipelines.IfengPipeline': 100},
    }

    item = IfengItem()
    def parse(self, response):
        # 使用LinkExtractor过滤新浪网的一些链接
        new_link_list = LinkExtractor(allow=r'news.ifeng.com/a').extract_links(response)
        tech_link_list = LinkExtractor(allow=r'tech.ifeng.com/a').extract_links(response)

        # 每个得到的是个类对象
        for new_link in new_link_list:
            print(new_link.url)
            print(new_link.text)
            yield scrapy.Request(new_link.url, callback=self.download_data_new)

        for tech_link in tech_link_list:
            print(tech_link.url)
            print(tech_link.text)
            yield scrapy.Request(tech_link.url, callback=self.download_data_tech)

    def download_data_new(self, response):
        title = ''.join(response.xpath("//div[@class='yc_tit']/h1/text()").extract())
        print(title)
        print(type(title))
        text = ''.join(response.xpath("//div[@id='yc_con_txt']//text()").extract())
        print(text)
        # item = IfengItem()
        if title.strip():
            self.item['title'] = title.strip()
            self.item['content'] = title.strip()
            yield self.item
        print("new============================================")
        time.sleep(2)
    def download_data_tech(self, response):
        title = ''.join(response.xpath("//h1[@id='artical_topic']/text()").extract())
        print(title)
        print(type(title))
        text = ''.join(response.xpath("//div[@id='main_content']//text()").extract())
        print(text)

        if title.strip():
            self.item['title'] = title.strip()
            self.item['content'] = title.strip()
            yield self.item
        print("tech============================================")
        time.sleep(2)