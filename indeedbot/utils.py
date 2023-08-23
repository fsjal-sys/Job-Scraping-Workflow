from undetected_chromedriver import Chrome, ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

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

def rest(): sleep(10000)