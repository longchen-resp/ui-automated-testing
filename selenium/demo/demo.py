'''
 selenium基础
'''
from selenium import webdriver


#创建浏览器对象
driver =webdriver.Chrome()
#访问指定的url需要加http://
driver.get('http://www.baidu.com')
#查找指定的元素并输入
driver.find_element('id','kw').send_keys('龙龙自动化测试')
#查找元素点击
driver.find_element('id','su').click()