# -*- coding: utf-8 -*-
import scrapy


class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn/']
    # start_urls = [f'https://www.xicidaili.com/nn/{page}' for page in range(1, 4057)]

    def parse(self, response):
        # 提取数据
        # 提取IP和端口
        # 选择所有的tr标签
        selectors = response.xpath('//tr')
        # 循环遍历tr标签下的td标签
        for selector in selectors:
            ip = selector.xpath('./td[2]/text()').get()
            port = selector.xpath('./td[3]/text()').get()

            items = {
                'ip': ip,
                'port': port
            }

            yield items

        # 翻页操作
        next_page = response.xpath('//a[@class="next_page"]/@href').get()
        if next_page:
            next_url = response.urljoin(next_page)
            # 发出请求
            # callback是回调函数，将请求得到的响应交给自己处理
            yield scrapy.Request(next_url, callback=self.parse)
