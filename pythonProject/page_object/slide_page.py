'''
    滑动页面的实现
'''
# 导入所需要包
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Chromewebdriver路径
driver= webdriver.Chrome()

# url地址
url = 'https://baidu.com'

# 访问地址
driver.get(url)

# 获取文本输入框对象
input_button = driver.find_element(by='xpath', value='//input[@id="kw"]')

# 暂缓时间输入
time.sleep(2)

# 向文本输入框输入内容
# 这里可暂缓时间方便查看，也可不暂缓时间
input_button.send_keys('龙龙自动化测试')

# 获取百度一下按钮
submit = driver.find_element(by='xpath', value='//input[@id="su"]')

# 点击百度一下按钮
submit.click()

# ***这里需要一个时间暂缓***(=>1即可)
time.sleep(3)

# 滑动到最底部
js_button = 'document.documentElement.scrollTop=100000'

#方法一：直接执行js，滑动到最底部
#driver.execute_script(js_button)

#方法二：使用JavaScript脚本将滚动条拖动到指定地方
target = driver.find_element(By.ID,'rs_new')  # 需要将滚动条拖动至的指定的元素对象定位
driver.execute_script("arguments[0].scrollIntoView();", target)  # 将滚动条拖动到元素可见的地方

# 暂缓时间，点击下一页
time.sleep(2)

# 获取下一页对象
next_page = driver.find_element(by='xpath', value='//a[@class="n"]')

# 点击下一页
next_page.click()

# 暂缓时间
time.sleep(2)

# 返回上一页
driver.back()

# 暂缓时间
time.sleep(2)

# 回去
driver.forward()

# 暂缓时间
time.sleep(3)

# 最后退出
driver.quit()
