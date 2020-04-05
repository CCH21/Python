#!/usr/bin/env python3

import requests
import json

# 指定url
post_url = 'https://fanyi.baidu.com/sug'

# 进行UA伪装
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}

# post请求参数处理
word = input('请输入要翻译的单词：')
data = {'kw': word}

# 发送请求
response = requests.post(url=post_url, data=data, headers=headers)

# 获取响应数据
# json方法返回的是obj
# 如果确认响应数据是json类型的数据才可以用json方法
dic_obj = response.json()
print(dic_obj)

# 持久化存储
fileName = word + '.json'
fp = open(fileName, 'w', encoding='utf-8')
json.dump(dic_obj, fp=fp, ensure_ascii=False)

print('爬取成功！')
