#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/2/19 14:02 
# @Author : TETE
# @File : main.py
from appium.webdriver.common.mobileby import MobileBy

from Appium.wework.pages.addressList import AddressList
from Appium.wework.pages.base_page import BasePage


class Main(BasePage):
    def goto_message(self):
        pass

    def goto_address_list(self):
        self.find(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/en5' and @text='通讯录']").click()
        return AddressList(self._driver)

    def goto_work_bench(self):
        pass

    def goto_profile(self):
        pass
