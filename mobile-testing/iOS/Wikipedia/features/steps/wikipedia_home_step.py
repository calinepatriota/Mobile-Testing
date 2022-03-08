from behave import *
from iOS.Wikipedia.features.pages.wikipedia_home_page import WikipediaHomePage


@Given('App is lunched')
def step_impl(context):
    context.page_object = WikipediaHomePage(context.driver)
    context.page_object.button_skip()