#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/2/19 13:57 
# @Author : TETE
# @File : app.py
from appium import webdriver

from Appium.wework.pages.base_page import BasePage
from Appium.wework.pages.main import Main


class App(BasePage):
    def start(self):
        if self._driver is None:
            caps = {"platformName": "android",
                    "deviceName": "127.0.0.1:7555",
                    "appPackage": "com.tencent.wework",
                    "appActivity": "com.tencent.wework.launch.WwMainActivity",
                    "noReset": "true",
                    "skipDeviceInitialization": "true",
                    "unicodeKeyBoard": "true",
                    "resetKeyBoard": "true",
                    "skipServerInstallation": True,
                    "skipDeviceInintialization": True
                    }

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(10)

        return self

    def restart(self):
        pass

    def stop(self):
        self._driver.quit()

    def main(self) -> Main:
        return Main(self._driver)
