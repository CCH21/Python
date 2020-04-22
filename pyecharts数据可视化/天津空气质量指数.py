#!/usr/bin/env python3

from bs4 import BeautifulSoup
from pyecharts import Bar, Pie, Grid, Overlap, Page
import requests

# 爬取空气知音网站上天津空气污染的数据
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
url = 'http://www.air-level.com/air/tianjin/'
response = requests.get(url=url, headers=headers)
page_text = response.text

# 清洗并处理数据
soup = BeautifulSoup(page_text, 'html.parser')
info_list = soup.find_all('table', class_='table text-center')
tr_list = info_list[0].find_all('tr')
tr_list.pop(0)
places = []
AQIs = []
PM2_5s = []
PM10s = []
primary_pollutants = []
primary_pollutants_ratio = []
for i in range(len(tr_list)):
    tr = tr_list[i].text.replace('\n', ' ').lstrip().rstrip()
    info = tr.split()
    place = info[0]
    places.append(place)
    AQI = eval(info[1])
    AQIs.append(AQI)
    PM2_5 = eval(info[3])
    PM2_5s.append(PM2_5)
    PM10 = eval(info[5])
    PM10s.append(PM10)
    primary_pollutant = info[7]
    primary_pollutants.append(primary_pollutant)
PM2_5_ratio = primary_pollutants.count('PM2.5') / len(primary_pollutants)
PM_10_ratio = 1 - PM2_5_ratio
primary_pollutants_ratio.append(PM2_5_ratio)
primary_pollutants_ratio.append(PM_10_ratio)

# 数据可视化
page = Page()
bar1 = Bar('各监测点空气污染数据', '日期：2020-04-17 星期五')
bar1.add('AQI', places, AQIs, mark_line=['average'], mark_point=['min', 'max'], is_more_utils=True,
         is_datazoom_show=True, xaxis_interval=0, xaxis_rotate=30)
bar2 = Bar()
bar2.add('PM2.5', places, PM2_5s, mark_line=['average'], mark_point=['min', 'max'], is_more_utils=True,
         yaxis_formatter='μg/m³', is_datazoom_show=True, xaxis_interval=0, xaxis_rotate=30)
bar3 = Bar()
bar3.add('PM10', places, PM10s, mark_line=['average'], mark_point=['min', 'max'], is_more_utils=True,
         yaxis_formatter='μg/m³', is_datazoom_show=True, xaxis_interval=0, xaxis_rotate=30)
overlap = Overlap(width=1280, height=720)
overlap.add(bar1)
overlap.add(bar2, is_add_yaxis=True, yaxis_index=1)
overlap.add(bar3, is_add_yaxis=True, yaxis_index=1)
grid = Grid(width=1280, height=720)
grid.add(overlap, grid_right='20%', grid_bottom='15%')
page.add(grid)

pie = Pie('各监测点主要污染物分布情况', '日期：2020-04-17 星期五', title_pos='left', width=1280, height=720)
pie.add('', ['PM2.5', 'PM10'], primary_pollutants_ratio, radius=[40, 75], is_label_show=True, label_text_color=None,
        legend_orient='vertical', legend_pos='right')
page.add(pie)

page.render('天津各监测点空气污染数据.html')
