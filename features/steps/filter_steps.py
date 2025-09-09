from behave import given, when, then
from features.pages.filter_page import FilterHighLow
import config
import time


# High to Low
@given("the user is on the main dashboard")
def step_impl(context):
    context.filter_page = FilterHighLow(context.driver)
    assert "inventory" in context.driver.current_url
    time.sleep(1)

@when("the user filters the displayed product's price from hi to low")
def step_impl(context):
    context.filter_page.filter("hilo")
    time.sleep(0.5)

@then("the user expects the first product to have the highest price")
def step_impl(context):
    context.filter_page.check_price(True)
    time.sleep(0.5)

#----------------------------- Low to High


@when("the user filters the displayed product's price from low to hi")
def low_high(context):
    context.filter_page.filter("lohi")
    time.sleep(0.5)

@then("the user expects the first product to have the lowest price")
def step_impl(context):
    context.filter_page.check_price(False)
    time.sleep(0.5)

#----------------------------- A to Z

@when("the user filters the displayed product from a to z")
def step_impl(context):
    context.filter_page.filter("az")
    time.sleep(0.5)

@then("the user expects the product list to be sorted alphabetically (a-z)")
def step_impl(context):
    context.filter_page.check_sorting(False)

#----------------------------- Z to A

@when("the user filters the displayed product from z to a")
def step_impl(context):
    context.filter_page.filter("za")
    time.sleep(0.5)

@then("the user expects the product list to be sorted alphabetically (z-a)")
def step_impl(context):
    context.filter_page.check_sorting(True)



    
