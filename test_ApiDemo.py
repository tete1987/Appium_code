#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/8 15:23 
# @Author : TETE
# @File : test_ApiDemo.py
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestApiDemo:
    def setup(self):
        caps = {"platformName": "android",
                "deviceName": "127.0.0.1:62001",
                "appPackage": "com.example.android.apis",
                "appActivity": "com.example.android.apis.view.PopupMenu1",
                "skipDeviceInitialization": "true",
                "unicodeKeyBoard": "true",
                "resetKeyBoard": "true",
                "automationName": "uiautomator2"
                }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_api(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="MAKE A POPUP!"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="Search"]').click()
        # print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)
        #或也可以这样写：
        print(self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"Clicked popup")]').text)


