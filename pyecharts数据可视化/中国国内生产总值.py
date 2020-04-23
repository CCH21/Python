#!/usr/bin/env python3

import csv
from pyecharts import Line

Quarter = []
GDP = []
Primary_industry = []
Secondary_industry = []
Tertiary_industry = []

with open('中国国内生产总值.csv', 'r', newline='') as csv_in_file:
    filereader = csv.reader(csv_in_file)
    head = next(filereader)
    for row_list in filereader:
        Quarter.append(row_list[0])
        gdp = round(eval(row_list[2][:-1]) / 100, 3)
        GDP.append(gdp)
        pri = round(eval(row_list[4][:-1]) / 100, 3)
        Primary_industry.append(pri)
        sec = round(eval(row_list[6][:-1]) / 100, 3)
        Secondary_industry.append(sec)
        ter = round(eval(row_list[8][:-1]) / 100, 3)
        Tertiary_industry.append(ter)

Quarter = Quarter[::-1]
GDP = GDP[::-1]
Primary_industry = Primary_industry[::-1]
Secondary_industry = Secondary_industry[::-1]
Tertiary_industry = Tertiary_industry[::-1]

line = Line('中国国内生产总值同比增长率', '时间：2006年第1季度-2020年第1季度  数据来源：东方财富网', width=1280, height=720)
line.add('国内生产总值', Quarter, GDP, is_smooth=False, mark_point=['max'], mark_line=['average'], legend_pos='right')
line.add('第一产业', Quarter, Primary_industry, is_smooth=False, mark_point=['max'], mark_line=['average'],
         legend_pos='right')
line.add('第二产业', Quarter, Secondary_industry, is_smooth=False, mark_point=['max'], mark_line=['average'],
         legend_pos='right')
line.add('第三产业', Quarter, Tertiary_industry, is_smooth=False, mark_point=['max'], mark_line=['average'],
         legend_pos='right')
line.render('中国国内生产总值.html')
