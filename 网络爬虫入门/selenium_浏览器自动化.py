#!/usr/bin/env python3

from selenium import webdriver
from lxml import etree
from time import sleep

# 实例化一个浏览器对象
bro = webdriver.Firefox(executable_path='C:\\Program Files\\Mozilla Firefox\\geckodriver.exe')

# 让浏览器发起一个指定URL对应的请求
bro.get('http://125.35.6.84:81/xk/')

# 获取浏览器当前页面的源码数据
page_text = bro.page_source

# 解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)
sleep(5)

# 关闭浏览器
bro.quit()
