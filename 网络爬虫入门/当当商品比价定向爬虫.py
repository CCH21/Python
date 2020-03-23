#!/usr/bin/env python3

import re
import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"price_n\">&yen;[\d\.]*', html)
        tlt = re.findall(r'name=\"title\" ><a title=\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(';')[1])
            title = eval(tlt[i].split('title=')[1])
            ilt.append([price, title])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = '华为'
    depth = 3
    url = 'http://search.dangdang.com/?key=' + goods + '&act=input'
    infoList = []
    for i in range(depth):
        try:
            html = getHTMLText(url)
            parsePage(infoList, html)
            url = url + '&page_index=' + str(i)
        except:
            continue
    printGoodsList(infoList)


if __name__ == '__main__':
    main()
