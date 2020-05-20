#!/usr/bin/env python3

import json
import pandas as pd
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}

url = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoGlobalStatis,FAutoContinentStatis,' \
      'FAutoGlobalDailyList,FAutoCountryConfirmAdd'
response = requests.get(url=url, headers=headers)
data1 = response.text

# 解析JSON
data2 = json.loads(data1)
data3 = data2['data']
data4 = data3['FAutoGlobalDailyList']

# 用列表存储数据
date = []               # 日期
confirm = []            # 确诊人数
dead = []               # 死亡人数
heal = []               # 治愈人数
newAddConfirm = []      # 新增确诊人数
deadRate = []           # 死亡率
healRate = []           # 治愈率
for i in data4:
    date.append('2020.' + str(i['date']))
    confirm.append(i['all']['confirm'])
    dead.append(i['all']['dead'])
    heal.append(i['all']['heal'])
    newAddConfirm.append(i['all']['newAddConfirm'])
    deadRate.append(i['all']['deadRate'])
    healRate.append(i['all']['healRate'])

# 将存储的数据制作为数据框
data5 = pd.DataFrame({
    '日期': date,
    '确诊人数': confirm,
    '死亡人数': dead,
    '治愈人数': heal,
    '新增确诊人数': newAddConfirm,
    '死亡率': deadRate,
    '治愈率': healRate
})

# 持久化存储
data5.to_csv('./数据/20200515海外疫情情况.csv', index=0, encoding='gbk')
