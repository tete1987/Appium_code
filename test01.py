#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/12/3 16:07 
# @Author : TETE
# @File : test01.py
from appium import  webdriver

desire_caps ={
    "platformName":"android",
    "deviceName": "127.0.0.1:62001 device",
    "appPackage":"com.xueqiu.android",
    "appActivity":".view.WelcomeActivityAlias",
    "noReset" :True
}
driver=webdriver.Remote("http://localhost:4723/wd/hub", desire_caps)
driver.implicitly_wait(10)
el4 = driver.find_element_by_id("com.xueqiu.android:id/home_search")
el4.click()
el5 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el5.send_keys("alibaba")
el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout")
el6.click()
el7 = driver.find_element_by_id("com.xueqiu.android:id/action_close")
el7.click()

