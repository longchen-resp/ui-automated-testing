'''
    index_page页面对象，实现首页中关于攻略搜索的流程
'''
from selenium import webdriver

from base.base_page import BasePage


class IndexPage(BasePage):
    #核心元素
    url='http://localhost:8080/'
    search_input=('name','kw')
    search_button=('xpath','//*[@id="header_user"]/li[1]/form/div/button/i')
    #核心业务流
    def search(self,txt):
        self.visit()
        self.input(self.search_input,txt)
        self.click(self.search_button)

#调试
# if __name__=='__main__':
#     driver=webdriver.Chrome()
#     txt='柳江'
#     ip=IndexPage(driver)
#     ip.search(txt)