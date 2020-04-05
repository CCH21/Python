#!/usr/bin/env python3

import requests
import json

url = 'https://movie.douban.com/j/chart/top_list'
params = {'type': '24', 'interval_id': '100:90', 'action': '', 'start': '0', 'limit': '20'}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}

response = requests.get(url=url, params=params, headers=headers)

list_data = response.json()

fp = open('douban.json', 'w', encoding='utf-8')
json.dump(list_data, fp=fp, ensure_ascii=False)

print('爬取成功！')
