#!/usr/bin/env python3

import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
urls = ['http://downsc.chinaz.net/Files/DownLoad/jianli/202003/jianli12413.rar',
        'http://downsc.chinaz.net/Files/DownLoad/jianli/202003/jianli12414.rar',
        'http://downsc.chinaz.net/Files/DownLoad/jianli/202003/jianli12413.rar']


def get_content(url):
    print('正在爬取：', url)
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.content


def parse_content(content):
    print('响应数据的长度为：', len(content))


for url in urls:
    content = get_content(url)
    parse_content(content)
