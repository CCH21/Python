#!/usr/bin/env python3

import requests
import json

url = 'https://www.mcdonalds.com.cn/ajaxs/search_by_point'
data = {'point': '117.314324,39.086569', 'type': ''}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}

response = requests.post(url=url, data=data, headers=headers)
dic_obj = response.json()

fileName = 'McDonalds_天津市.json'
fp = open(fileName, 'w', encoding='utf-8')
json.dump(dic_obj, fp=fp, ensure_ascii=False)

print('爬取数据结束')
