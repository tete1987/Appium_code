
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2021/2/19 14:07 
# @Author : TETE
# @File : manual_invitet.py
from appium.webdriver.common.mobileby import MobileBy

from Appium.wework.pages.base_page import BasePage


class ManualInvite(BasePage):
    def add_member_by_menul(self):
        from Appium.wework.pages.contact_add import ContactAdd
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return  ContactAdd(self._driver)

    def get_toast(self):
        toast = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return toast


