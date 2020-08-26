from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
import time
import json
from ..base_page import BasePage

class AndroidMainPage(BasePage):

    CANCEL = (MobileBy.ID, "com.google.android.gms:id/cancel")
    GUEST = (MobileBy.ID, "com.wayfair.wayfair:id/continue_as_guest")
    DISMISS = (MobileBy.ID, "com.wayfair.wayfair:id/acquisition_no_thanks")
    SEARCH_BAR = (MobileBy.ID, "com.wayfair.wayfair:id/tv_tabbedmain_searchbar")
    EDIT_TEXT = (MobileBy.ID, "com.wayfair.wayfair:id/search_edit_text")
    OPTION = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]")
    #LIVING_ROOM = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView')
    LIVING_ROOM = (MobileBy.XPATH, '"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.GridLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView"')
    PRODUCT = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout")
    #TouchAction(driver)   .press(x=562, y=1424)   .move_to(x=562, y=857)   .release()   .perform()
    LOGO = (MobileBy.ID, 'com.wayfair.wayfair:id/logo_image')

    def __init__(self, driver):
        super(AndroidMainPage, self).__init__(driver)

    def navigate_to_product(self):
        try:
            self.wait(self.CANCEL).click()
        except:
            pass
        try:
            self.wait(self.DISMISS).click()
        except:
            self.wait(self.GUEST).click()
        self.wait(self.SEARCH_BAR).click()
        self.wait(self.EDIT_TEXT).send_keys("Hashtag")
        self.wait(self.OPTION).click()
        time.sleep(7)
        #self.swipe(562, 1424, 562, 857)
        self.wait(self.LOGO)
        self.swipe(361, 1097, 346, 170)
        self.swipe(361, 1097, 346, 500)
        self.wait(self.LIVING_ROOM).click()
        # self.wait(self.PRODUCT).click()
        time.sleep(2)
