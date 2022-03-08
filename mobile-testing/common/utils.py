import time
from time import sleep


def wait_for_element_presence():
    sleep(10)


def change_context(context, contexto, typeAction):
    time.sleep(5)
    oldContext = context.driver.context
    context.driver.switch_to.context(contexto)
    context.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="'
    +typeAction+'"]').click()
    context.driver.switch_to.context(oldContext)