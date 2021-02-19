#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/7 10:34 
# @Author : TETE
# @File : test_ele_select.py
import pytest
from appium import webdriver
class TestAppSearch:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] ="com.xueqiu.android"
        caps["appActivity"] ="com.xueqiu.android.common.MainActivity"
        caps["noReset"] ="true"
        caps["skipDeviceInitialization"] ="true"
        caps["unicodeKeyBoard"] ="true"
        caps["resetKeyBoard"] ="true"

        # caps["dontStopAppOnReset"] ="true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.back()
        self.driver.back()
        self.driver.quit()

    def  test_attr(self):
       '''
        1）打开【雪球】应用
        2）定位首页的搜索框
        3）判断搜索框的是否可用，并查看搜索框name属性值
        4）打印搜索框这个元素的左上角坐标和它的宽高
        5）向搜索框输入：alibaba
        6）判断【阿里巴巴】是否可见
        7）如果可见，打印“搜索成功”点击，如果不可见，打印“搜索失败”
       :param self:
       :return:
       '''
       element_search=self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
       search_enable = element_search.is_enabled()
       print(element_search.text)
       print(element_search.location)
       print(element_search.size)
       if search_enable == True:
           element_search.click()
           self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
           alibaba_element = self.driver.find_element_by_xpath(
               "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")

           element_disaply= alibaba_element.get_attribute("displayed")
           #get_attribute 返回值是 字符串‘true’
           if element_disaply == 'true':
               print("搜索成功")
           else:
               print("搜索失败")


if __name__ == '__main__':
        pytest.main()
