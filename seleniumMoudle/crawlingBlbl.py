"""
    bilibili 点选验证
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.bilibili.com/')
driver.find_element_by_css_selector('.header-login-entry').click()

time.sleep(1)

driver.find_element_by_css_selector('.tab__form div:nth-child(1) input').send_keys('username')
driver.find_element_by_css_selector('.tab__form div:nth-child(3) input').send_keys('password')
driver.find_element_by_css_selector('div.btn_primary').click()


'''
对接打码平台  --> 超级鹰 
'''

