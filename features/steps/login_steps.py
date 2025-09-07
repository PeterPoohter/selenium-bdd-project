from behave import given, when, then
import config
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@given("the user is logged in")
def step_impl(context):
    context.driver.get(config.BASE_URL)
    context.driver.find_element(By.NAME, "user-name").send_keys(config.USERNAME)
    context.driver.find_element(By.NAME, "password").send_keys(config.PASSWORD + Keys.RETURN)
    time.sleep(2) 