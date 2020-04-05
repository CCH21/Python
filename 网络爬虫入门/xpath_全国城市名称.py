#!/usr/bin/env python3

import requests
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
url = 'https://www.aqistudy.cn/historydata/'
page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
all_city_names = []
city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
for li in city_names_list:
    city_name = li.xpath('./a/text()')[0]
    all_city_names.append(city_name)
