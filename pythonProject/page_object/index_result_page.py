'''
    index_result_page页面对象，实现攻略搜索结果页面选择攻略加载的流程
'''
from selenium import webdriver

from base.base_page import BasePage


class IndexResultPage(BasePage):
    #核心元素
    url='http://localhost:8080/search?kw='+'txt'
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