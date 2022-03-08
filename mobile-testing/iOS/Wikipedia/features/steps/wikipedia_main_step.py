from behave import *
from hamcrest import assert_that, is_
from iOS.Wikipedia.features.pages.wikipedia_main_page import WikipediaMainPage


@When('I send the text {country} to search')
def step_impl(context, country):
    context.page_object = WikipediaMainPage(context.driver)
    context.page_object.search(country, context)


@When('I click on All top read article link')
def step_impl(context):
    context.page_object = WikipediaMainPage(context.driver)
    context.page_object.scroll_to_all_top_read_articles()


@Then('I validate Country {country} and description {description} corresponding expected')
def step_impl(context, country, description):
    context.page_object = WikipediaMainPage(context.driver)
    assert_that(context.page_object.get_text_title_search(), is_(country))
    assert_that(context.page_object.get_text_subtitle_search(), is_(description))


@Then('I validate that Home page is displayed')
def step_impl(context):
    context.page_object = WikipediaMainPage(context.driver)
    assert_that(context.page_object.get_text_title_home(), is_('Wikipedia'))