#!/usr/bin/env python3

import requests
from pyecharts import Map
from bs4 import BeautifulSoup

# 爬取百度百科上第六次全国人口普查的页面，并且处理数据
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
url = 'https://baike.baidu.com/item/%E7%AC%AC%E5%85%AD%E6%AC%A1%E5%85%A8%E5%9B%BD%E4%BA%BA%E5%8F%A3%E6%99%AE%E6%9F%A5' \
      '/5005655?fromtitle=%E7%AC%AC%E5%85%AD%E6%AC%A1%E4%BA%BA%E5%8F%A3%E6%99%AE%E6%9F%A5&fromid=5069655&fr=aladdin '
names = []
person_sums = []
res = requests.get(url=url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
list_ = soup.find_all(class_='wikitable sortable jquery-tablesorter')[1]
lists = list_.find_all('tr')
for i in lists[1:]:
    name = i.find('th').text
    person_sum = eval(i.find(width='30').text.replace(',', ''))
    names.append(name)
    person_sums.append(person_sum)
names.pop(0)
person_sums.pop(0)

# 数据可视化
map_ = Map('第六次全国人口普查（单位：千人）', width=1200, height=600)
map_.add('', names, person_sums, maptype='china',
         is_visualmap=True,
         visual_text_color='#000',
         is_label_show=True,
         visual_range=[0, 110000]
         )
map_.render('第六次全国人口普查_百度百科.html')
