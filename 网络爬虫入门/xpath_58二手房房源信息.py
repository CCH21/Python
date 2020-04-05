#!/usr/bin/env python3

import requests
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
url = 'https://tj.58.com/ershoufang/'
page_text = requests.get(url=url, headers=headers).text

# 数据解析
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
fp = open('58.txt', 'w', encoding='utf-8')
for li in li_list:
    title = li.xpath('./div[2]/h2/a/text()')[0]
    print(title)
    fp.write(title + '\n')
