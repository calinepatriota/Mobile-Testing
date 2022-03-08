import os
import sys
from appium.webdriver.common.mobileby import MobileBy


PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
from common.utils import wait_for_element_presence
PARENT_PATH = os.path.abspath("../..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
from common.common_methods import Common_Methods
from common.utils import change_context


class WikipediaMainPage(Common_Methods):
    HOME_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Wikipedia')
    LABEL_SEARCH = (MobileBy.XPATH,'//XCUIElementTypeSearchField[@name="Search Wikipedia"]')
    READ_ALL_TOPICS_LINK = (MobileBy.XPATH,'//XCUIElementTypeStaticText[@name="All top read articles"]')
    SEARCH_TITLE = (MobileBy.XPATH,'//XCUIElementTypeApplication[@name="Wikipedia"]/XCUIElementTypeWindow[1]/ \
    XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/ \
    XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/ \
    XCUIElementTypeCell[1]/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[1]')
    SEARCH_SUBTITLE = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="Wikipedia"]/XCUIElementTypeWindow[1]/ \
    XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/ \
    XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/ \
    XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]')


    def search(self,text,context):
        super().custom_wait_implicit(self.LABEL_SEARCH)
        super().click(self.LABEL_SEARCH)
        super().send_keys(self.LABEL_SEARCH,text)
        wait_for_element_presence()
        change_context(context,"NATIVE_APP", 'Search')
        wait_for_element_presence()


    def scroll_to_all_top_read_articles(self):
        i = 0
        while(i < 2):
            super().scroll_down()
            i+=1
        self.click(self.READ_ALL_TOPICS_LINK)


    def get_text_title_search(self):
        return super().get_text_element(self.SEARCH_TITLE)


    def get_text_subtitle_search(self):
        return super().get_text_element(self.SEARCH_SUBTITLE)


    def get_text_title_home(self):
        return super().get_text_element(self.HOME_TITLE)