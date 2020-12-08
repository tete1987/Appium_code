#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/4 14:04 
# @Author : TETE
# @File : test_wait.py
import time

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
        '''
        1.打开“我的”
        2.点击“账号密码登录”
        3.输入账号和密码
        4.点击登录
        :return:
        '''
        self.driver.find_element_by_android_uiautomator('new UiSelector().'
                                                        'resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("帐号密码登录")').click()
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().'
                                                        'resourceId("com.xueqiu.android:id/login_account")').send_keys("123455")
        self.driver.find_element_by_android_uiautomator('new UiSelector().'
                                                        'resourceId("com.xueqiu.android:id/login_password")').send_keys(
            "123455")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_text").text("推荐")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("腾讯云").instance(0));').click()


if __name__ == '__main__':
        pytest.main()
