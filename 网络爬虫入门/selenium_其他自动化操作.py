#!/usr/bin/env python3

from selenium import webdriver
from time import sleep

bro = webdriver.Firefox(executable_path='C:\\Program Files\\Mozilla Firefox\\geckodriver.exe')

# 发起第一组请求
bro.get('https://www.taobao.com/')

# 定位到搜索框对应的标签
search_input = bro.find_element_by_id('q')
# 标签交互
search_input.send_keys('iPhone')
# 执行一组JS程序
bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')
sleep(2)
# 点击搜索按钮
btn = bro.find_element_by_css_selector('.btn-search')
btn.click()

# 发起另一组请求
bro.get('https://www.baidu.com')
sleep(2)

# 回退
bro.back()
sleep(2)

# 前进
bro.forward()

sleep(5)
bro.quit()
