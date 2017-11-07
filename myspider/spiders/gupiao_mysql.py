# -*- coding: utf-8 -*-
import scrapy
import time
from myspider.items import GupiaoItem

class GupiaoSpider(scrapy.Spider):
    name = 'gupiao'
    start_urls = ['http://stock.10jqka.com.cn/']

    custom_settings = {
        'ITEM_PIPELINES': {'myspider.pipelines.GpPipeline': 200},
    }

    # 处理响应函数
    def parse(self, response):
        # print(response.text)
        a_list = response.xpath("//div[@id='rzrq']/table[@class='m-table']/tbody/tr/td[2]/a")
        # 获取股票简称和链接
        for text_href in a_list:
            text_name = text_href.xpath(".//text()").extract()[0]
            href_url = text_href.xpath(".//@href").extract()[0]
            print(href_url)
            time.sleep(3)
            yield scrapy.Request(href_url, callback=self.parse_data,
                                 meta={'text_name':text_name,
                                       'url_base': href_url,
                                       "seindex":1})

    # 对每个股票的数据
    def parse_data(self, response):
        # print(response.meta["text_name"])
        # 想要获得的数据的页数
        seindex = response.meta["seindex"]
        # 获得每个股票的名称
        text_name = response.meta["text_name"]
        # 获得每条数据
        per_data = response.xpath("//table[@class='m-table']/tbody/tr/td/text()").extract()
        print(per_data)
        # 如果没有就退出
        # if not per_data:
        #     return

        # 每一页50条数据
        data_split = []
        index = 0
        while index < len(per_data):
            temp = index + 11
            data_split.append(per_data[index:temp])
            index = temp
        item = GupiaoItem()
        for data in data_split:
            item['xuhao'] = data[0]
            item['jysj'] = data[1].strip()
            item['rz_ye'] = data[2]
            item['rz_mre'] = data[3]
            item['rz_che'] = data[4]
            item['rz_rzjmr'] = data[5]
            item['rq_yl'] = data[6]
            item['rq_mcl'] = data[7]
            item['rq_chl'] = data[8]
            item['rq_rzjmq'] = data[9]
            item['rq_rzrqye'] = data[10]

            print(item)
            yield item
        if seindex >=1:
            return
        # ajax 加载的分页数据链接
        seindex += 1
        more_data_url =  response.meta['url_base']+"/order/desc/page/"+str(seindex)+"/ajax/1/"
        print("index = "+str(seindex))
        yield scrapy.Request(more_data_url, callback=self.parse_data,
                                 meta={"text_name":text_name,
                                       'url_base': response.meta['url_base'],
                                       "seindex":seindex})

