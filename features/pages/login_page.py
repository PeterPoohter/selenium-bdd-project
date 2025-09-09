import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.burger_menu = (By.ID, "react-burger-menu-btn")
        self.logout_btn = (By.ID, "logout_sidebar_link")
        self.username_locator = (By.NAME, "user-name")
        self.password_locator = (By.NAME, "password")
        self.login_btn = (By.ID, "login-button")
    
    def enter_username(self, username):
        # self.driver.find_element(*self.username_locator).send_keys(username)
        self.send_keys(self.username_locator, username)

    def enter_password(self, password):
        self.send_keys(self.password_locator, password)
        self.click(self.login_btn)
    def click_menu(self):
        menu = self.driver.find_element(*self.burger_menu)
        menu.click()
        time.sleep(1)

    def click_logout_btn(self):
        logout_btn = self.driver.find_element(*self.logout_btn)
        logout_btn.click()
        


        