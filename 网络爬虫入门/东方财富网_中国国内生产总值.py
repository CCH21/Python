#!/usr/bin/env python3

from bs4 import BeautifulSoup
import csv
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}

with open('中国国内生产总值.csv', 'w', newline='') as csv_out_file:
    head_list = ['季度', '国内生产总值-绝对值（亿元）', '国内生产总值-同比增长', '第一产业-绝对值（亿元）', '第一产业-同比增长',
            '第二产业-绝对值（亿元）', '第二产业-同比增长', '第三产业-绝对值（亿元）', '第三产业-同比增长']
    filewriter = csv.writer(csv_out_file)
    filewriter.writerow(head_list)

    for page in range(1, 4):
        url = 'http://data.eastmoney.com/cjsj/grossdomesticproduct.aspx?p=' + str(page)
        response = requests.get(url=url, headers=headers)
        page_text = response.text

        soup = BeautifulSoup(page_text, 'html.parser')
        table = soup.find('table', id='tb')
        tr_list = table.find_all('tr')
        tr_list.pop(-1)
        for i in range(2):
            tr_list.pop(0)

        for tr in tr_list:
            info = tr.text.replace(' ', '').replace('\r', '').replace('\n', ' ')
            info = info.lstrip().rstrip()
            info_list = info.split()
            filewriter.writerow(info_list)
