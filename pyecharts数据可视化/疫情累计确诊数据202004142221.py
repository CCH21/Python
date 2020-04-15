#!/usr/bin/env python3

import csv
from pyecharts import Pie

areas = []
nums = []
with open('疫情累计确诊数据202004142221.csv', 'r', newline='') as csv_in_file:
    filereader = csv.reader(csv_in_file)
    for row_list in filereader:
        areas.append(row_list[0])
        nums.append(int(row_list[1]))
areas = areas[:21]
areas.append('其他地区')
other_areas_num = sum(nums[21:])
nums = nums[:21]
nums.append(other_areas_num)

pie = Pie('新冠肺炎疫情国内外累计确诊数据\n数据更新至2020.04.14 22:21', title_pos='right')
pie.add('', areas, nums,
        radius=[40, 75],
        is_label_show=True,
        label_text_color=None,
        legend_orient='vertical',
        legend_pos='left'
        )
pie.render('疫情累计确诊数据202004142221.html')
