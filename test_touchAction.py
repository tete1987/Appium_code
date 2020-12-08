#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/7 10:34 
# @Author : TETE
# @File : test_ele_select.py
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


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


    def test_touch(self):
        action =TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height* 4/5)
        y_end = int(height*1/5)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()

    def test_touchAction_unlock(self):
        action =TouchAction(self.driver)
        action.press(x=244, y=374).wait(100).move_to(x=711, y=374).wait(100).\
            move_to(x=1198,y=374).move_to(x=1198,y=865).wait(100).\
            move_to(x=1198, y=1323).wait(100).release().perform()

if __name__ == '__main__':
        pytest.main()
