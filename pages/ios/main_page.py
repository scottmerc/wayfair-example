from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
import time
import json
from ..base_page import BasePage

class IOSMainPage(BasePage):
    GUEST = (MobileBy.ACCESSIBILITY_ID, "Continue as Guest")
    NAVBAR = (MobileBy.ACCESSIBILITY_ID, "Navigation.TopNav.SearchBar.View.Aid")
    DROPDOWN = (MobileBy.XPATH, "//XCUIElementTypeApplication[@name=\"Wayfair\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]")
    LIVINGROOM = (MobileBy.XPATH, "//XCUIElementTypeApplication[@name=\"Wayfair\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther[2]")
    PRODUCT = (MobileBy.XPATH, "(//XCUIElementTypeOther[@name=\"UIComponentsCommonLegacy.Components.RedesignedProductComponent.View.Aid\"])[1]/XCUIElementTypeOther/XCUIElementTypeImage")


    def __init__(self, driver):
        super(IOSMainPage, self).__init__(driver)

    def navigate_to_product(self):
        self.wait(self.GUEST).click()
        self.wait(self.NAVBAR).click()
        self.wait(self.NAVBAR).send_keys("Hashtag")
        self.wait(self.DROPDOWN).click()
        time.sleep(5)
        self.driver.execute_script('mobile: scroll', {'direction': 'down'})
        self.wait(self.LIVINGROOM).click()
        self.wait(self.PRODUCT).click()
        time.sleep(2)
        



    
