#!/usr/bin/env python3

import re
import requests
from pyecharts import Line
from bs4 import BeautifulSoup

# 爬取天气网天津2020-04-16至2020-04-30的最高和最低气温
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
url = 'https://www.tianqi.com/tianjin/15/'
response = requests.get(url=url, headers=headers)
page_text = response.text

# 筛选出所需数据
soup = BeautifulSoup(page_text, 'html.parser')
div_list = soup.find_all(class_='box_day')
table_day_list = div_list[0].find_all(class_='table_day')
low_temp = []
high_temp = []
for i in range(len(table_day_list)):
    li = table_day_list[i].find(class_='temp').text
    # print(li)
    low = eval(re.search(r'(\d*)~', li).group()[:-1])
    low_temp.append(low)
    high = eval(re.search(r'~(\d*)', li).group()[1:])
    high_temp.append(high)

# 数据可视化
attr = ['2020-04-16', '2020-04-17', '2020-04-18', '2020-04-19', '2020-04-20', '2020-04-21', '2020-04-22', '2020-04-23',
        '2020-04-24', '2020-04-25', '2020-04-26', '2020-04-27', '2020-04-28', '2020-04-29', '2020-04-30']
line = Line('天津未来15天的气温走势', '日期：2020-04-16至2020-04-30')
line.add('日最低气温', attr, low_temp, mark_point=['min'], mark_line=['average'])
line.add('日最高气温', attr, high_temp, is_smooth=False, mark_point=['max'], mark_line=['average'])
line.render('天津未来15天气温走势图.html')
