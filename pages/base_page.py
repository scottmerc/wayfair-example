from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_actions import PointerActions
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import time

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(driver, 20)
        self._short_wait = WebDriverWait(driver, 3)

    def wait(self, locator, waiter=None):
        if waiter is None:
            waiter = self._wait
        return waiter.until(EC.presence_of_element_located(locator))

    def short_wait(self, locator):
        return self.wait(locator, waiter=self._short_wait)

    def tap_at(self, x, y):
        actions = ActionBuilder(self.driver)
        p = actions.add_pointer_input("touch", "finger")
        p_actions = PointerActions(p)
        p.create_pointer_move(duration=0, x=x, y=y, origin='viewport')
        p_actions.pointer_down()
        p_actions.pause(0.2)
        p_actions.pointer_up()
        actions.perform()

    def tap_el(self, el):
        rect = el.rect
        x = rect['x'] + (rect['width'] / 2)
        y = rect['y'] + (rect['height'] / 2)
        self.tap_at(x, y)

    def swipe(self, x1, y1, x2, y2):
        swipe = TouchAction(self.driver)
        swipe.press(x = x1, y = y1)
        time.sleep(.5)
        swipe.move_to(x = x2, y = y2)
        time.sleep(.5)
        swipe.release()
        swipe.perform()