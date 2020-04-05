#!/usr/bin/env python3

import requests

# 指定url
url = 'https://www.sogou.com/'

# 发起请求
# get方法会返回一个响应对象response
response = requests.get(url)

# 获取响应数据
# text方法会返回一个字符串类型的响应数据
page_text = response.text
print(page_text)

# 持久化存储
with open('sogou.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)

print('爬取数据结束')
