from behave import *
from iOS.Wikipedia.features.pages.wikipedia_articles_page import WikipediaArticlesPage


@Then('I print all titles')
def step_impl(context):
    context.page_object = WikipediaArticlesPage(context.driver)
    context.page_object.print_titles()