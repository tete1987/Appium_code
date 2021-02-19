#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/2/19 14:17 
# @Author : TETE
# @File : test_address.py
from Appium.wework.pages.app import App


class TestAdderss:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_add_contact(self):
        add_contact =self.main.goto_address_list().add_member().add_member_by_menul().\
            input_name().input_phone_number().click_save()

        add_contact.get_toast()

        assert '成功' in add_contact.get_toast()
