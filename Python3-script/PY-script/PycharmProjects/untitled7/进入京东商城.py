# -*- coding:utf-8 -*-
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
import os
import time

WEBDRIVER_URL = 'C:\\Users\chengxue\AppData\Local\Google\Chrome\Application\chromedriver.exe'
BAIDU_URL = 'https://www.baidu.com'

#调用chrome浏览器
driver = webdriver.Chrome(WEBDRIVER_URL)
driver.implicitly_wait(8)
print('driver ok')

#打开百度页面
driver.get(BAIDU_URL)
driver.save_screenshot('perpic/original.png')
driver.implicitly_wait(10)
print(driver.title)

#浏览器页面最大化
driver.maximize_window()
print ('window maximize ok')

#在百度输入框中输入搜索的关键字
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('京东商城')
driver.implicitly_wait(10)
print('send keys input ok')

#点击百度搜索
driver.find_element_by_xpath('//*[@id="su"]').submit()
driver.save_screenshot('picture\tag.png')
driver.implicitly_wait(10)
print('click baidu ok')

#点击京东百科
driver.find_element_by_link_text('京东商城_百度百科').send_keys(Keys.ENTER)
driver.implicitly_wait(25)
time.sleep(15)
print(driver.title)

driver.find_elements_by_css_selector('xcxc').pop().click()


#返回上一个页面
# print('now %s'%(BAIDU_URL))
# driver.back()
# driver.implicitly_wait(12)
# print('back ok')





