from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
import time


class AddToCart(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10) 
        self.add_to_cart_locator = (By.XPATH, "//button[contains(@class, 'btn_inventory')]")
        # self.product_name_locator = (By.XPATH, "(//div[@data-test='inventory-item-name'])[1]")
        self.produc_name_locator = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
        self.cart_locator = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_prod_name = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
        self.remove_cart_btn_locator = (By.XPATH, "//button[contains(@class, 'cart_button')]")
        self.continue_shopping_locator = (By.CSS_SELECTOR, ".btn.btn_secondary.back.btn_medium")
        self.badge_locator = (By.CLASS_NAME, "shopping_cart_badge")

    def from_dashboard(self, num_to_add):
        buttons = self.driver.find_elements(*self.add_to_cart_locator)
        assert buttons, "❌ No Add to Cart buttons found on dashboard!"

        for i in range(num_to_add):
            buttons[i].click()
            time.sleep(1)

    def get_product(self):
    # get all product names currently in the dashboard
        product_elements = self.driver.find_elements(*self.produc_name_locator)
        product_names = [elem.text for elem in product_elements[:5]]  # limit to first 5 added
        print("Products added: ", product_names)
        return product_names

    
    def opens_cart(self):
        self.driver.find_element(*self.cart_locator).click()

    def get_cart_items(self, expected_products):
        cart_items = [item.text for item in self.driver.find_elements(*self.cart_prod_name)]
        print("Products in cart: ", cart_items)

        for prod in expected_products:
            assert prod in cart_items, f"❌ {prod} not found in cart"
        print("✅ All selected products are in the cart!")
        return cart_items


    def remove_all_from_cart(self):
        remove_btns = self.driver.find_elements(*self.remove_cart_btn_locator)

        for btn in remove_btns:
            btn.click()
            time.sleep(1)

    def from_cart_to_inventory(self):
        continue_btn = self.driver.find_element(*self.continue_shopping_locator)
        continue_btn.click()

    def check_badge(self, expected_badge_num):
        actual_badge_num = self.text_to_num(self.badge_locator)
        assert str(expected_badge_num) == str(actual_badge_num)

    def check_cart(self):
        badge_present = self.driver.find_elements(*self.badge_locator)
        assert badge_present

        
    


