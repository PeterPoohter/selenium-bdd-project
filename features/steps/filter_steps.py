from behave import given, when, then
from features.pages.filter_page import FilterHighLow
import config
import time

@given("the user is on the main dashboard")
def step_impl(context):
    context.filter_page = FilterHighLow(context.driver)
    assert "inventory" in context.driver.current_url
    time.sleep(2)

@when("the user filters the displayed product's price from hi to low")
def step_impl(context):
    context.filter_page.filter_hilo()
    time.sleep(1)

@then("the user expects the first product to have the highest price")
def step_impl(context):
    context.filter_page.check_price()
    time.sleep(1)

#-----------------------------

@when("the user filters the displayed product from a to z")
def step_impl(context):
    context.filter_page.filter_a_to_z()
    time.sleep(2)


    
