# coding = utf-8
from selenium import webdriver
import os, time
import selenium.webdriver.support.ui as ui
chromedriver ="C:\\Users\chengxue\AppData\Local\Google\Chrome\Application\chromedriver.exe"



#调动webdriver
#os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

#浏览百度浏览器（等待10秒）
driver.set_page_load_timeout(10)
print()

#打开百度网页
driver.get('https://www.baidu.com/')
time.sleep(5)
print(222)

#将网页最大化
driver.maximize_window()
print(333)
time.sleep(3)

#在百度搜索狂输入selenium
input_box = driver.find_element_by_xpath('//*[@id="kw"]')
input_box.send_keys('selenium')
time.sleep(3)
print('yes')

#点击百度一下
driver.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(3)
print('click ok')

#点击selenium的连接
driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
time.sleep(10)
#driver.save_screenshot('perpic/original.png')
print('selenium connect ok')

#点击下载
wait = ui.WebDriverWait(driver,10)
wait.until(lambda driver: driver.find_element_by_xpath('//*[@id="menu_download"]/a'))
driver.find_element_by_xpath('//*[@id="menu_download"]/a').click()
time.sleep(15)
print('download click ok')



# driver.find_element_by_xpath('//*[@id="mainContent"]/p[7]/a[2]')
# time.sleep(10)
# print('okokk')


#关闭浏览器
# driver.quit()










