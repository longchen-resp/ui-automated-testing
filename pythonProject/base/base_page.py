'''
    BasePage类是POM中的基类，主要用于提供常用的函数，为页面对象类进行服务
'''
from time import sleep
from selenium import webdriver

class BasePage:
    #构造函数
    def __init__(self,driver):
        self.driver=driver
    #访问url
    def visit(self):
        self.driver.get(self.url)

    #元素定位
    def locator(self,loc):
        return self.driver.find_element(*loc)

    #输入
    def input(self,loc,txt):
        self.locator(loc).send_keys(txt)

    #点击
    def click(self,loc):
        self.locator(loc).click()
    #等待
    def wait(self,time):
        sleep(time)
