import pytest
import os
from appium import webdriver
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_token = os.getenv("HS_API_TOKEN")
ios_web_driver_url = "https://us-sf.headspin.io:7004/v0/{}/wd/hub".format(api_token)
android_web_driver_url = "https://de-fra.headspin.io:7018/v0/{}/wd/hub".format(api_token)

def get_android_driver(caps):
    driver = webdriver.Remote(
        command_executor = android_web_driver_url,
        desired_capabilities = caps
    )
    return driver


def get_ios_driver(caps):
    driver = webdriver.Remote(
        command_executor = ios_web_driver_url,
        desired_capabilities = caps
    )
    return driver

@pytest.fixture(scope='function')
def android_driver(android_caps):
    driver = get_android_driver(android_caps)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def ios_driver(ios_caps):
    driver = get_ios_driver(ios_caps)
    yield driver
    driver.quit()


@pytest.fixture()
def ios_caps():
    return {
    "deviceName": "iPhone 7 Plus",
    "udid": "0a61558c1715bae4fe225aedc19c0be8539ca71a",
    "automationName": "XCUITest",
    "platformVersion": "13.4",
    "platformName": "iOS",
    "bundleId": "com.wayfair.WayfairApp",
    "headspin:capture": True
}

@pytest.fixture()
def android_caps():
    return {
    "deviceName": "SM-J510FN",
    "udid": "71fef222",
    "autoAcceptAlerts": "true",
    "appPackage": "com.wayfair.wayfair",
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "appActivity": "com.wayfair.mainactivity.MainActivity",
    "headspin:capture": True
}