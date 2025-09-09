from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    def text_to_num(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return int(element.text)
    
    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()  # optional: clears existing text
        element.send_keys(text)

    def click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()
