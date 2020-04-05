#!/usr/bin/env python3

import requests
import re


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
        plt = re.findall(r'\"view_price\":\"[\d.]*\"', html)
        tlt = re.findall(r'\"raw_title\":\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
            ilt.append([price, title])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
    print("")


def main():
    goods = "iPhone"
    depth = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(44 * i)
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
                "cookie": "thw=cn; isg=BDAwbVz_GrVG2sX4Sia7WgELAv6CeRTDpdJXhCqARgpf5dKP0426U8WXPW2F7syb; "
                          "cna=VZZIFsKhZyYCAXUg2FBLqKp9; "
                          "l=dBPGoQ4HqDZnqhOzBOfZKJXuB37TeId4zkPr-YAnrICPOwfHQyMfWZfr4A8MCn1VnsNeJ3-Uc"
                          "-eJBmT5VyIqJxpsw3k_J_Amed8h.; tracknick=aries%5Cu7B97%5Cu65E0%5Cu9057%5Cu7B56; "
                          "_cc_=VFC%2FuZ9ajQ%3D%3D; tg=0; "
                          "enc=8M2R1tPAUD5dJ4CqhBUA36s3QYGNCH9FxWdpKN098qb3nRZKgEm4tN"
                          "%2Fm1cXU03jLWAQEsOsZU5xZd4wz1u0Ptw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; "
                          "miid=1626696299948225594; JSESSIONID=7555854B00CE126EB4A3E19291406603; "
                          "birthday_displayed=1; _tb_token_=hlDHwcZTf5b3HaAimgNn; _samesite_flag_=true; "
                          "cookie2=1ba9a76187f513048466814d3ae8e98b; t=d17bdeafbb008264eaec901f811062ea; "
                          "tfstk=cn2lBPMVn7l5WNe3GUM7vmxstzyla21rPJy438uwDlHTAiyq0s0kgCJ2Ui0J6jAC.; "
                          "sgcookie=EgHE5meID2srL4H3sGvWI; unb=2070860423; "
                          "uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=WqG3DMC9Fb5mPLIQoVXj&cookie15"
                          "=UIHiLt3xD8xYTw%3D%3D&existShop=false&pas=0&cookie14=UoTUP2odqjt0Ig%3D%3D; "
                          "uc3=id2=UUjWDi%2B9Qqsw%2Bw%3D%3D&nk2=AmP13bRqfKUjWsM8FA%3D%3D&vt3=F8dBxdAW5W5Shh2VZjE%3D"
                          "&lg2=VT5L2FSpMGV7TQ%3D%3D; csg=0686a75d; lgc=aries%5Cu7B97%5Cu65E0%5Cu9057%5Cu7B56; "
                          "cookie17=UUjWDi%2B9Qqsw%2Bw%3D%3D; dnk=aries%5Cu7B97%5Cu65E0%5Cu9057%5Cu7B56; "
                          "skt=0173f5e1a85910fc; existShop=MTU4NTg4MDY1Nw%3D%3D; "
                          "uc4=id4=0%40U2o0P%2FcrNAEZhhHEZTi5VNc5i0%2FO&nk4=0%40AIjfhT3ycEKoM8DUWktRtJE3YMShKawE; "
                          "_l_g_=Ug%3D%3D; sg=%E7%AD%963d; _nk_=aries%5Cu7B97%5Cu65E0%5Cu9057%5Cu7B56; "
                          "cookie1=VWt%2BB%2FFxMprzfsodtlERVBso18H3rXsbtEvGibVlyhY%3D; mt=ci=4_1; v=0; "
                          "alitrackid=i.taobao.com; lastalitrackid=i.taobao.com "
            }
            html = requests.get(url, headers=headers)
            parsePage(infoList, html.text)
        except:
            continue
    printGoodsList(infoList)


if __name__ == "__main__":
    main()
