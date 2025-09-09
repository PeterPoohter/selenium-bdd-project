from behave import given, when, then
import config
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


@given("that the current state is logged-out")
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    if "inventory" in context.driver.current_url:
        context.login_page.click_menu()
        context.login_page.click_logout_btn()
        time.sleep(2)

@when("the user logs-in with VALID credentials")
def step_impl(context):
    context.driver.get(config.BASE_URL)
    context.login_page.enter_username(config.USERNAME)
    time.sleep(3)
    context.login_page.enter_password(config.PASSWORD)
    time.sleep(2) 

@then("the user validates that it has successfully logged-in")
def step_impl(context):
    assert "inventory" in context.driver.current_url

 #Login with INVALID credentials

@when("the user logs-in with INVALID credentials")
def step_impl(context):
    context.driver.get(config.BASE_URL)
    context.login_page.enter_username(config.INVALID_KEYWORD)
    time.sleep(1)
    context.login_page.enter_password(config.INVALID_KEYWORD)
    time.sleep(2) 

@then("the user has unsuccessfully logged-in")
def step_impl(context):
    assert "Epic sadface: Username and password do not match any user in this service" in context.driver.page_source
    time.sleep(2) 



