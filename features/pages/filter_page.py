from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class FilterHighLow:
    def __init__(self, driver):
        self.driver = driver
        self.filter_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.filter_select = Select(driver.find_element("xpath", "//select[@class='product_sort_container']"))
        # self.prices_elements = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")
    
    # def open(self, url):   # <--- MUST be indented inside the class
    #     self.driver.get(url)

    def filter_hilo(self):
       self.filter_select.select_by_value("hilo")

    def check_price(self):
        prices_elements = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")
        prices = [float(price.text.replace("$", "")) for price in prices_elements]

        print("Displayed prices:", prices)

        assert prices == sorted(prices, reverse=True), f"Prices not sorted high-to-low: {prices}"

    def filter_a_to_z(self):
        self.filter_select.select_by_value("az")