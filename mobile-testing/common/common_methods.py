import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from common.driver_manager import DriverManager


class Common_Methods(DriverManager):

    def click(self, element):
        self.wait_for(EC.element_to_be_clickable(element)).click()


    def send_keys(self, element,text):
        self.driver.find_element(*element).clear()
        self.driver.find_element(*element).send_keys(text)


    def element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)


    def elements_by_xpath(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)


    def find_element(self, element):
        return self.driver.find_element(*element)


    def wait_for(self, condition, seconds = 10):
        return WebDriverWait(self.driver, seconds).until(condition)


    def scroll(self, el1, el2):
        action = TouchAction(self.driver)
        action.press(el2).move_to(el1).perform()


    def scroll_long_press(self, el1, el2):
        action = TouchAction(self.driver)
        action.long_press(el2).move_to(el1).perform().release()


    def wait(self, time):
        WebDriverWait(self.driver, time)


    def get_text_element(self,locator):
        return self.find_element(locator).text


    def custom_wait_implicit(self, element):
        i = 0
        state = False
         # verifing if exists elements with idintifier 'element'   
        elementExists = len(self.driver.find_elements(*element))
        # loop validates timeout = 20seconds (40 * 0.5 = 20s) or if element is present, break loop
        while(i <= 40):
            elementExists = len(self.driver.find_elements(*element))
            time.sleep(0.5)
            if(elementExists > 0):
                state = True
                break
            i+=1
        if state == False:
            print("Element "+str(element)+ " not found")


    def custom_wait_explicit_timeout(self, element, timeExplicit):
        i = 0
        state = False
         # verifing if exists elements with idintifier 'element'
        elementExists = len(self.driver.find_elements(*element))
        # loop validates timeout = timeExplicit * 0.5 or if element is present, break loop
        while(i<=timeExplicit):
            elementExists = len(self.driver.find_elements(*element))
            time.sleep(0.5)
            if(elementExists > 0):
                state = True
                break
            i+=1
        if state == False:
            print("Element "+str(element)+ " not found")


    def click_if_element_is_present(self, element):
        elementIsPresent = len(self.driver.find_elements(*element))
        time.sleep(0.5)
        if(elementIsPresent > 0):
            self.driver.find_element(*element).click()


    def scroll_down(self):
        self.driver.execute_script('mobile: scroll', {'direction': 'down'});


    def touch_position(self, posX, posY):
         TouchAction(self.driver).tap(x=posX, y=posY).perform()


    def get_location(self,element):
        location = self.driver.find_element(*element).location
        x = location.get('x')
        y = location.get('y')
        return x, y


    def get_text_by_any_locator(self,element,typeLocator):
        if(typeLocator == 'xpath'):
            text =  self.driver.find_element_by_xpath(element).text
        elif (typeLocator == 'id'):
            text =  self.driver.find_element_by_id(element).text
        elif (typeLocator == 'accessibility_id'):
            text =  self.driver.find_element_by_accessibility_id(element).text
        elif (typeLocator == 'name'):
            text =  self.driver.find_element_by_name(element).text
        elif (typeLocator == 'class'):
            text =  self.driver.find_element_by_class(element).text
        return text