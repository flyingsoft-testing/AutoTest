# -*- coding:utf-8 -*-
__author__ = 'Tester03'


from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #调用键盘按键模块
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r'F:\option\aaa.html')  # 运行网址

# checkbox复选框
driver.find_element_by_xpath('//input[@value="cv1"]').click()  # 点击选中
driver.find_element_by_xpath('//input[@value="cv2"]').send_keys(Keys.SPACE)  # 发送空格取消选中
sleep(3)

# 判断checkbox是否被选中
if driver.find_element_by_xpath('//input[@value="cv2"]').is_selected():
    print u'选项被选中'
else:
    print u'选项没有被选中'

sleep(3)

# radio单选框
driver.find_element_by_xpath('//input[@value="rv1"]').send_keys(Keys.SPACE)  # 发送空格选中
sleep(1)
driver.find_element_by_xpath('//input[@value="rv2"]').click()  # 点击选中另一项
sleep(3)

# 判断radio是否被选中
if driver.find_element_by_xpath('//input[@value="rv1"]').is_selected():
    print u'选项被选中'
else:
    print u'选项没有被选中'

sleep(3)

driver.quit()


