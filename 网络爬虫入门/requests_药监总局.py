#!/usr/bin/env python3

import requests
import json

# 批量获取并存储不同企业的ID
url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
id_list = []
for page in range(1, 21):
    page = str(page)
    data = {'on': 'true', 'page': page, 'pageSize': '15', 'productName': '', 'conditionType': '1', 'applyname': '',
            'applysn': ''}
    json_ids = requests.post(url=url, data=data, headers=headers).json()
    for dic in json_ids['list']:
        id_list.append(dic['ID'])

# 获取企业详情数据
all_data_list = []
post_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
for id in id_list:
    data = {'id': id}
    detail_json = requests.post(url=url, data=data, headers=headers).json()
    all_data_list.append(detail_json)

# 持久化存储
fp = open('CFDA_all_data.json', 'w', encoding='utf-8')
json.dump(all_data_list, fp=fp, ensure_ascii=False)
print('爬取数据完成！')
