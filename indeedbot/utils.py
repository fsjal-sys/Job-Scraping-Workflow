from undetected_chromedriver import Chrome, ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv
from os import getenv

def driver_setup():
    options = ChromeOptions()
    return Chrome(options=options)

def try_getting(element_selector, driver):
    getting = True
    element = None
    while getting:
        try:
            element = driver.find_element(By.CSS_SELECTOR, element_selector)
            getting = False
        except NoSuchElementException:
            pass
    return element

def rest(): 
    while (True): sleep(1)

def get_credentials():
    load_dotenv()
    return getenv("EMAIL"), getenv("PASSWORD")