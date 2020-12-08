#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/4 14:04 
# @Author : TETE
# @File : test_wait.py
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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
        5.获取这只香港 阿里巴巴的股价，并判断股价的价格>170
        6.增加显示等待
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_banner").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        locator = (MobileBy.XPATH,"//*[@text='09988']/../../..//*"
                                                               "[@resource-id='com.xueqiu.android:id/current_price']")
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        ele = WebDriverWait(self.driver,10).until(lambda x:x.find_element(*locator))
        # ele = self.driver.find_element(*locator)
        print(ele.text)
        current_price=float(ele.text)
        expect_price = 170
        assert current_price > expect_price


if __name__ == '__main__':
        pytest.main()
