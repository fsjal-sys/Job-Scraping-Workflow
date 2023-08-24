import undetected_chromedriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv
from os import getenv

def driver_setup(): return undetected_chromedriver.Chrome(driver_executable_path="./chromedriver-linux64/chromedriver")

def try_getting(element_selector, driver):
    print(f"Trying to find element: {element_selector}")
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
    print("Resting...")
    while (True): sleep(1)

def get_credentials():
    load_dotenv()
    return getenv("EMAIL"), getenv("PASSWORD")
