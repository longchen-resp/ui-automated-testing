'''
    测试用例的设计
'''
import unittest
from selenium import webdriver
from page_object.register_page import RegisterPage


class TestCase(unittest.TestCase):
    
    def test_1_register(self):
        driver = webdriver.Chrome()
        user='e1234'
        password='123456'
        password2='123456'
        rp=RegisterPage(driver)
        rp.register(user,password,password2)

if __name__=='__main__':
    unittest.main()