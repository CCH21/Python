#!/usr/bin/env python3

from lxml import etree
from pyecharts import Map
import re
import requests

# 爬取百度百科上第六次全国人口普查的页面
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
url = 'https://zhidao.baidu.com/question/374334864.html'
response = requests.get(url=url, headers=headers)
page_text = response.text

# 获取并处理数据
tree = etree.HTML(page_text)
p_list = tree.xpath('//div[@id="best-content-3111290021"]/p')
p_list.pop(0)
for i in range(5):
    p_list.pop(-1)
province_names = []
numbers = []
for p in p_list:
    text = p.xpath('./text()')[0]
    text = text.encode('iso-8859-1').decode('gbk')
    num = eval(re.search(r'(\d+\.?\d*)万', text).group()[:-1])
    numbers.append(num)
    province_name = re.search(r'、.*?\d', text).group()[1:-1]
    province_names.append(province_name)

# 数据可视化
map_ = Map('第六次全国人口普查（单位：万人）\n普查以2010年11月1日零时为标准时点进行，公告显示中国总人口截至当时为1370536875人',
           width=1200, height=600)
map_.add('', province_names, numbers, maptype='china',
         is_visualmap=True,
         visual_text_color='#000',
         is_label_show=True,
         visual_range=[0, 12000]
         )
map_.render('第六次全国人口普查_百度知道.html')
