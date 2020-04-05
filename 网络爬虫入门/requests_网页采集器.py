#!/usr/bin/env python3

import requests

# UA伪装，将对应的User-Agent封装到字典中
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}

url = 'https://www.sogou.com/web'

# 处理url携带的参数：封装到字典中
kw = input('请输入关键词：')
param = {'query': kw}

# 对指定的url发起请求
# 对应的url携带参数，且在请求过程中处理了参数
response = requests.get(url=url, params=param, headers=headers)

page_text = response.text

fileName = kw + '.html'
with open(fileName, 'w', encoding='utf-8') as fp:
    fp.write(page_text)

print(fileName, '爬取成功！')
