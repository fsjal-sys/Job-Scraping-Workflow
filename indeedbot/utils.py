import undetected_chromedriver, time, pickle, os, re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from dotenv import load_dotenv
from os import getenv

def driver_setup(): return undetected_chromedriver.Chrome(driver_executable_path="./chromedriver-linux64/chromedriver")

def try_getting(element_selector, driver):
    print(f"Trying to find element: {element_selector}")
    getting = True
    element = None
    while getting :
        try:
            element = driver.find_element(By.CSS_SELECTOR, element_selector)
            getting = False
        except NoSuchElementException:
            pass
    return element

def try_getting_timed(element_selector, driver, timer):
    print(f"Trying to find element: {element_selector}")
    element = None
    start_time = time.time()

    while (time.time() - start_time) < timer:
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

def get_job_search_variables():
    load_dotenv()
    return getenv("SEARCH_TERM"), getenv("LOCATION"), getenv("DATE_POSTED"), getenv("DISTANCE"), getenv("JOB_TYPE")

def save_cookies(driver):
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

def load_cookies(driver):
    if os.path.exists("cookies.pkl"):
        cookies = pickle.load(open("cookies.pkl", "rb"))
        print("Loading cookies...")
        for cookie in cookies:
            driver.add_cookie(cookie)
        print("Cookies loaded.")
    else:
        print("No cookies file found.")

def clear_input_field(element):
    while (element.get_attribute("value") != ""):
        element.send_keys(Keys.BACK_SPACE)

def format_dropdown_text(option): return re.sub(r'\(\d+\)', "", option)