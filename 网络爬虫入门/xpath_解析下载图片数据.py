#!/usr/bin/env python3

import os
import requests
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
url = 'http://pic.netbian.com/4kqiche/'
response = requests.get(url=url, headers=headers)
# 手动设定响应数据的编码
# response.encoding = 'utf-8'
page_text = response.text

# 数据解析：src的属性值，alt的属性值
# 解析数据后进行持久化存储
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="slist"]/ul/li')
if not os.path.exists('picLibs'):
    os.mkdir('picLibs')
for li in li_list:
    img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
    img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
    img_name = img_name.encode('iso-8859-1').decode('gbk')
    img_data = requests.get(url=img_src, headers=headers).content
    img_path = 'picLibs/' + img_name
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(img_name, '下载成功！')
