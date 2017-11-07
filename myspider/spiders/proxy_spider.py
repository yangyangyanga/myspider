import scrapy

class ProxySpider(scrapy.Spider):
    name = "proxyip"
    start_urls = ["http://ip.filefab.com/index.php"]

    def parse(self, response):
        # //h1[@id='ipd']/span/text()
        # print(response.text)
        print(response.xpath("//h1[@id='ipd']/span/text()").extract())
