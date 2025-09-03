from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "user-name")
        self.password_field = (By.NAME, "password")

    def open(self, url):
        self.driver.get(url)
        self.driver.execute_script("document.body.style.zoom='90%'")

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password + Keys.RETURN)


class AddToCart:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_locator = (By.XPATH, "//button[contains(@class, 'btn_inventory')]")
        self.product_name_locator = (By.XPATH, "(//div[@data-test='inventory-item-name'])[1]")
        self.cart_locator = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_prod_name = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
        self.remove_cart_btn_locator = (By.XPATH, "//button[contains(@class, 'cart_button')]")
        self.continue_shopping_locator = (By.CSS_SELECTOR, ".btn.btn_secondary.back.btn_medium")

    def from_dashboard(self):
        buttons = self.driver.find_elements(*self.add_to_cart_locator)
        assert buttons, "❌ No Add to Cart buttons found on dashboard!"
        buttons[0].click()


    def get_product(self):
        first_product_name = self.driver.find_element(*self.product_name_locator).text
        print("Product Name: ", first_product_name)
        return first_product_name
    
    def opens_cart(self):
        self.driver.find_element(*self.cart_locator).click()

    def get_cart_items(self, prod_name):
        prod_names = self.driver.find_elements(*self.cart_prod_name)
        assert any(prod_name in item.text for item in prod_names), "Fleece Jacket not found in cart"

    def remove_all_from_cart(self):
        remove_btns = self.driver.find_elements(*self.remove_cart_btn_locator)

        for btn in remove_btns:
            btn.click()

    def from_cart_to_inventory(self):
        continue_btn = self.driver.find_element(*self.continue_shopping_locator)
        continue_btn.click()
        
    


