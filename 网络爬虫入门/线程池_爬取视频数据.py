#!/usr/bin/env python3

import re
import requests
from lxml import etree
from multiprocessing.dummy import Pool

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
url = 'https://www.pearvideo.com/category_5'
page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
urls = []    # 存储所有视频的链接和名称
for li in li_list:
    detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    # 对详情页的url发起请求
    detail_page_text = requests.get(url=detail_url, headers=headers).text
    # 解析出视频的url
    ex = 'srcUrl="(.*?)",vdoUrl'
    video_url = re.findall(ex, detail_page_text)[0]
    dic = {'name': name, 'url': video_url}
    urls.append(dic)


def get_video_data(dic):
    url = dic['url']
    print(dic['name'], '正在下载...')
    data = requests.get(url=url, headers=headers).content
    # 持久化存储
    with open(dic['name'], 'wb') as fp:
        fp.write(data)
        print(dic['name'], '下载成功！')


# 使用线程池对视频数据进行请求
# 线程池原则：处理的是阻塞且耗时的操作
pool = Pool(4)
pool.map(get_video_data, urls)

pool.close()
pool.join()
