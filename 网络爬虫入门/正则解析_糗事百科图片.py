#!/usr/bin/env python3

import os
import re
import requests

# 创建用来保存图片的文件夹
if not os.path.exists('qiutuLibs'):
    os.mkdir('qiutuLibs')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}

# 设置一个通用的url模板
url = 'https://www.qiushibaike.com/imgrank/page/%d/'
for pageNum in range(1, 6):
    # 生成对应页码的url
    new_url = format(url % pageNum)

    # 使用通用爬虫对整张页面进行爬取
    page_text = requests.get(url=new_url, headers=headers).text

    # 使用聚焦爬虫对页面图片进行解析
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex, page_text, re.S)

    for src in img_src_list:
        # 拼接出完整的图片url
        src = 'https:' + src
        # 请求图片的二进制数据
        img_data = requests.get(url=src, headers=headers).content
        # 生成图片名称
        img_name = src.split('/')[-1]
        # 生成图片存储路径
        img_path = 'qiutuLibs/' + img_name
        # 持久化存储
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功！')
