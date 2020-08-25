import pytest
import time
import os
import json
from appium import webdriver
from pages.ios.main_page import IOSMainPage
from pages.android.main_page import AndroidMainPage

class TestWayfair(object):

    def test_android_wayfair(self, android_driver):
        android_test = AndroidMainPage(android_driver)
        android_test.navigate_to_product()
    
    def test_ios_wayfair(self, ios_driver):
        ios_test = IOSMainPage(ios_driver)
        ios_test.navigate_to_product()
        



