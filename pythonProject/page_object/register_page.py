'''
    RegisterPage类：专门用于实现注册页面对象的文件
    主体内容包含：
        1.核心的页面元素
            账户、密码、确认密码、提交
        2.核心的业务流程：
            用户注册行为
'''
from selenium import webdriver

from base.base_page import BasePage


class RegisterPage(BasePage):
    #核心元素
    url='http://localhost:8080/register'
    user=('id','username')
    password=('id','password')
    password2=('id','password2')
    register_button=('xpath','//*[@id="submitForm"]/button')
    #核心业务流
    def register(self,user,password,password2):
        self.visit()
        self.input(self.user,user)
        self.input(self.password,password)
        self.input(self.password2,password2)
        self.click(self.register_button)
#调试
if __name__ == '__main__':
    driver=webdriver.Chrome()
    user='e1234'
    password='123456'
    password2='123456'
    rp=RegisterPage(driver)
    rp.register(user,password,password2)