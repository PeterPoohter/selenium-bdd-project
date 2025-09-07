from behave import given, when, then
from pages.login_page import LoginPage, AddToCart
import config
import time


# @given("the user is on the login page")
# def step_impl(context):
#     context.login_page = LoginPage(context.driver)
#     context.login_page.open(config.BASE_URL)
#     time.sleep(5)

# @when("the user enters valid credentials")
# def step_impl(context):
#     time.sleep(2)
#     context.login_page.login(config.USERNAME, config.PASSWORD)
#     time.sleep(3)

# @then("the user is redirected to the dashboard")
# def step_impl(context):
#     assert "inventory.html" in context.driver.current_url
#     assert "Swag Labs" in context.driver.title

# ----------------------------

@given("the user clicks the add to cart button")
def step_impl(context):
    context.add_to_cart = AddToCart(context.driver)
    context.add_to_cart.from_dashboard()
    context.add_to_cart.get_product()
    time.sleep(3)

@when("the user opens the cart")
def step_impl(context):
    context.add_to_cart.opens_cart()
    time.sleep(3)

@then("the user expects that the product is already on the cart and checks the product name")
def step_impl(context):
    context.add_to_cart.get_cart_items(context.add_to_cart.get_product())
    time.sleep(2)


# ----------------------------

@given("the user is on the cart and clicks the remove button")
def step_impl(context):
    assert "cart" in context.driver.current_url
    context.add_to_cart = AddToCart(context.driver)
    context.add_to_cart.remove_all_from_cart()
    time.sleep(2)

@when("the user clicks the continue shopping button")
def step_impl(context):
    context.add_to_cart.from_cart_to_inventory()
    assert "inventory" in context.driver.current_url
    time.sleep(2)






