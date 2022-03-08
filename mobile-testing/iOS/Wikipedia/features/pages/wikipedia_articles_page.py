import os
import sys


PARENT_PATH = os.path.abspath("./../..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
from common.common_methods import Common_Methods


class WikipediaArticlesPage(Common_Methods):

    INITIAL_PARTIAL_LIST = '//XCUIElementTypeApplication[@name="Wikipedia"]/XCUIElementTypeWindow/XCUIElementTypeOther/ \
    XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther \
    /XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell['
    FINAL_PARTIAL_LIST = ']/XCUIElementTypeOther[2]//XCUIElementTypeStaticText'
    FULL_LIST = '//XCUIElementTypeApplication[@name="Wikipedia"]/XCUIElementTypeWindow/XCUIElementTypeOther/ \
    XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/ \
    XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell'


    def print_titles(self):
        size_list = len(super().elements_by_xpath(self.FULL_LIST))
        print()
        i = 1
        while(i<=size_list):
            print('Title '+str(i)+': '+super().element_by_xpath(self.INITIAL_PARTIAL_LIST
            +str(i)+self.FINAL_PARTIAL_LIST).text)
            print()
            i+=1
 
        initial_position = 1
        last_position = size_list
        el1 = super().element_by_xpath(self.INITIAL_PARTIAL_LIST
            +str(initial_position)+self.FINAL_PARTIAL_LIST)
        el2= super().element_by_xpath(self.INITIAL_PARTIAL_LIST
            +str(last_position)+self.FINAL_PARTIAL_LIST)
        super().scroll_long_press(el1,el2)
        
        size_list_end = len(super().elements_by_xpath(self.FULL_LIST))
        while(initial_position<=size_list_end):
            print('Title '+str(last_position+1)+': '+super().element_by_xpath(self.INITIAL_PARTIAL_LIST
            +str(initial_position)+self.FINAL_PARTIAL_LIST).text)
            print()
            initial_position+=1
            last_position+=1