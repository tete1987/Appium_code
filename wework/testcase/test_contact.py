#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/2/18 14:26 
# @Author : TETE
# @File : test_contact.py
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestContactAddMember:
    def setup(self):
        caps = {"platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": "com.tencent.wework.launch.WwMainActivity",
                "noReset": "true",
                "skipDeviceInitialization": "true",
                "unicodeKeyBoard": "true",
                "resetKeyBoard": "true"}

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_add_member(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/en5' and @text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        memberName = self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b7n' and @text ='姓名　']/..//*[@text='必填']")
        memberName.send_keys('xiaohua3')

        memberPhone = self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b7n' and @text ='手机　']/..//*[@text='必填']")
        memberPhone.send_keys('15809993300')

        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/aj_").click()
        sleep(1)

        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")

