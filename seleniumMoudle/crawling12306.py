from selenium import webdriver
from selenium.webdriver import ActionChains
import time

'''
    12306 滑动验证
'''

driver = webdriver.Chrome()
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
})
driver.get('https://kyfw.12306.cn/otn/resources/login.html')
driver.find_element_by_css_selector('#J-userName').send_keys('username')
driver.find_element_by_css_selector('#J-password').send_keys('password')
driver.find_element_by_css_selector('#J-login').click()

#  操作过快元素还没有加载出来就开始查找元素会导致找不到元素
time.sleep(1)
sliding_block = driver.find_element_by_css_selector('#nc_1_n1z')
action = ActionChains(driver)
# perform() 执行操作  click_and_hold(sliding_block) sliding_block（按住这个模块不松）
action.click_and_hold(sliding_block).perform()
action.move_by_offset(85, 0)
action.move_by_offset(85, 0)
action.move_by_offset(85, 0)
action.move_by_offset(85, 0)

# 释放
action.release().perform()
