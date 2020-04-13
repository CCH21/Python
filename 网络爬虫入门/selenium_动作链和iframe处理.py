#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

bro = webdriver.Firefox(executable_path='C:\\Program Files\\Mozilla Firefox\\geckodriver.exe')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# iframe标签定位
bro.switch_to.frame('iframeResult')        # 切换浏览器标签定位的作用域
div = bro.find_element_by_id('draggable')

# 动作链
# 实例化动作链对象
action = ActionChains(bro)
# 点击长按指定的标签
action.click_and_hold(div)
# 拖拽操作
for i in range(5):
    action.move_by_offset(17, 0).perform()    # perform表示立即执行动作链操作
    sleep(0.3)
# 释放动作链
action.release()

sleep(3)
bro.quit()
