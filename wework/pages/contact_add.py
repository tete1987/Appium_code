#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/2/19 14:12 
# @Author : TETE
# @File : contact_add.py
from appium.webdriver.common.mobileby import MobileBy

from Appium.wework.pages.base_page import BasePage


class ContactAdd(BasePage):
    def input_name(self):
        memberName = self.find(MobileBy.XPATH,
                                              "//*[@resource-id='com.tencent.wework:id/b7n' and @text ='姓名　']/..//*[@text='必填']")
        memberName.send_keys('xiaohua3')
        return self

    def input_phone_number(self):
        memberPhone = self.find(MobileBy.XPATH,
                                               "//*[@resource-id='com.tencent.wework:id/b7n' and @text ='手机　']/..//*[@text='必填']")
        memberPhone.send_keys('15809993300')
        return self

    def click_save(self):
        from Appium.wework.pages.manual_invitet import ManualInvite
        self.find(MobileBy.ID, "com.tencent.wework:id/aj_").click()
        return ManualInvite(self._driver)

