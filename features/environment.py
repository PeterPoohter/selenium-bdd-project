# features/environment.py
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import config
import time

def before_all(context):
    edge_driver_path = r"C:\Users\jaypee\Documents\selenium_bdd_project\drivers\msedgedriver.exe"
    service = Service(edge_driver_path)
    context.driver = webdriver.Edge(service=service)
    context.driver.fullscreen_window()

    # 👉 Open login page and log in ONCE
    context.driver.get(config.BASE_URL)
    context.driver.find_element(By.NAME, "user-name").send_keys(config.USERNAME)
    context.driver.find_element(By.NAME, "password").send_keys(config.PASSWORD + Keys.RETURN)
    time.sleep(3)  # wait for dashboard

def after_all(context):
    context.driver.quit()
