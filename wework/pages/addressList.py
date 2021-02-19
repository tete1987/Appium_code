#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/2/19 14:03 
# @Author : TETE
# @File : addressList.py
from appium.webdriver.common.mobileby import MobileBy

from Appium.wework.pages.base_page import BasePage
from Appium.wework.pages.manual_invitet import ManualInvite


class AddressList(BasePage):
    def add_member(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return ManualInvite(self._driver)

    def my_client(self):
        pass
