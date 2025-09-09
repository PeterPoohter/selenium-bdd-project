from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class FilterHighLow:
    def __init__(self, driver):
        self.driver = driver
        self.filter_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.filter_select = Select(driver.find_element("xpath", "//select[@class='product_sort_container']"))
        self.prices_elements = (By.CSS_SELECTOR, ".inventory_item_price") #- the element locator is set on the step function to get the actual sorted prices when asserting
        self.product_name = (By.CSS_SELECTOR, ".inventory_item_name")

    def filter(self, sort_value):
        self.filter_select.select_by_value(sort_value)
        
    def check_price(self, true_false):
        prices_list = self.driver.find_elements(*self.prices_elements)
        prices = [float(price.text.replace("$", "")) for price in prices_list]

        print("Displayed prices:", prices)

    
        assert prices == sorted(prices, reverse=true_false), f"Prices not sorted properly: {prices}"

    # def filter_a_to_z(self):
    #     self.filter_select.select_by_value("az")

    def check_sorting(self, true_false):
        product_name_list = self.driver.find_elements(*self.product_name)
        prod_name = [name.text for name in product_name_list]
        assert prod_name == sorted(prod_name, reverse=true_false), f"Name not sorted A-Z: {prod_name}"