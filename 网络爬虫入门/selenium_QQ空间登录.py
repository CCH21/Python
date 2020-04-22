#!/usr/bin/env python3

from selenium import webdriver
from time import sleep

bro = webdriver.Firefox(executable_path='C:\\Program Files\\Mozilla Firefox\\geckodriver.exe')

bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')

a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()

username_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')

sleep(1)
username_tag.send_keys('2424577199')
sleep(1)
password_tag.send_keys('123456789')
sleep(1)
btn = bro.find_element_by_id('login_button')
btn.click()

sleep(3)
bro.quit()
