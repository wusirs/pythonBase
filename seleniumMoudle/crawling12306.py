from selenium import webdriver
from selenium.webdriver import ActionChains
import time

'''
    12306 滑动验证
    驱动路径：
      Ⅰ.驱动文件在python安装目录下<不需要添加路径>
      Ⅱ.驱动文件和代码放在一起<不需要添加路径>
    如果出现这个报错（ValueError: Timeout value connect was <object object at 0x000002384F574540>, but it must be an int, float or None.）
    检查selenium 版本和urllib3版本，可安装一下这两个版本的selenium和urllib3:
    pip install selenium==3.141.0
    pip install urllib3==1.26.2
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
