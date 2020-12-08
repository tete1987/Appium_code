#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/4 14:04 
# @Author : TETE
# @File : test_wait.py
import pytest
from appium import webdriver
class TestAppSearch:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:62001"
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

    def test_search(self):
        print("搜索测试用例")
        '''
        1.打开 雪球 app
        2.点击搜索输入框
        3.向搜索输入框里输入“阿里巴巴”
        4.在搜索结果里面选择“阿里巴巴”，然后进行点击
        5.获取这只香港 阿里巴巴的股价，并判断股价的价格>200
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_banner").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price =float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price >200


if __name__ == '__main__':
        pytest.main()
