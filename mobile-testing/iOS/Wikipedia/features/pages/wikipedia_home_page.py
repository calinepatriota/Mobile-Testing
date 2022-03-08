import os
import sys
from appium.webdriver.common.mobileby import MobileBy


PARENT_PATH = os.path.abspath("../../..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
from common.common_methods import Common_Methods


class WikipediaHomePage(Common_Methods):

    BUTTON_SKIP = (MobileBy.XPATH,'//XCUIElementTypeButton[@name="Skip"]')


    def button_skip(self):
        super().click(self.BUTTON_SKIP)


    def scroll_to(self):
        super().scroll_down()