import undetected_chromedriver, time, pickle, os, re, traceback, inspect
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from CSS_selectors import Selectors
from time import sleep
from dotenv import load_dotenv
from os import getenv

def driver_setup():
    options = undetected_chromedriver.ChromeOptions()
    options.binary_location = "./chromium/chrome"
    return undetected_chromedriver.Chrome(driver_executable_path="./chromedriver-linux64/chromedriver", options=options)

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
        except NoSuchElementException:
            pass
    if element is not None: print(f"{element_selector} was found.")
    else: log_print(f"{element_selector} was not found.")
    return element

def try_getting_child_elements(parent_element, child_element_selector):
    child_elements = parent_element.find_elements(By.CSS_SELECTOR, child_element_selector)
    return child_elements

def rest(): 
    print("Resting...")
    while True: time.sleep(1)

def log_print(*args, **kwargs):
    frame_info = inspect.stack()[1]
    file_name = frame_info.filename
    line_no = frame_info.lineno
    function_name = frame_info.function
    print(f"{file_name}:{function_name}:{line_no} ---> ", *args, **kwargs)
    print("\n")

def get_credentials():
    load_dotenv()
    return getenv("EMAIL"), getenv("PASSWORD")

def get_job_search_variables():
    load_dotenv()
    return getenv("SEARCH_TERM"), getenv("LOCATION"), getenv("DATE_POSTED"), getenv("DISTANCE"), getenv("JOB_TYPE")

def get_job_application_variables():
    load_dotenv
    return getenv("FIRST_NAME"), getenv("LAST_NAME"), getenv("PHONE_NUMBER"), getenv("CITY")

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

def hCaptcha_check(element_selector, driver):
    # Returns True if hCaptcha is present, false if not present

    print("Doing a timed hCaptcha check...")
    hCaptcha_iFrame_element = try_getting_timed(element_selector, driver, 10)
    return hCaptcha_iFrame_element is not None

def job_alert_popup_present(driver):
    popup_element = try_getting_timed(Selectors.JOB_ALERT_POPUP, driver, 5)
    if popup_element == None: 
        print(f"Job Alert Popup Present: {False}")
        return False
    else:
        print(f"Job Alert Popup Present: {True}")
        return True

def job_alert_popup_close(driver): 
    print("Attempting to close popup...")
    try_getting(Selectors.JOB_ALERT_POPUP_CLOSE, driver).click()
    print("Popup closed.")

def hCaptcha_actions(element_selector, driver):
    hCaptcha_iFrame_element = try_getting(element_selector, driver)
    print("Switching to iFrame...")
    driver.switch_to.frame(hCaptcha_iFrame_element)
    print("Switched to hCaptcha iFrame")

    try_getting(Selectors.HCAPTCHA_CHECKBOX, driver).click()
    print("Waiting for hCaptcha checkbox feedback...")
    sleep(5)
    driver.switch_to.default_content()
    print("Back to default content.")

def indeed_cloudfare_check():
    pass

def is_logged_in(driver):
    print("Checking for autologin... ")

    current_URL = driver.current_url

    try_getting_timed(Selectors.LOGIN_CHECK_ELEMENT, driver, 1).click()

    if (driver.current_url == current_URL): return True
    else: return False

def set_dropdown_option(driver, options, menu, dropdown_option):
    print(f"Setting dropdown option: {dropdown_option}")
    sleep(1)
    try:
        try_getting(menu, driver).click()
        for option in options:
            text = try_getting(option, driver).text
            text = format_dropdown_text(text).rstrip()
            print(f"{dropdown_option} matches {text}: {text == dropdown_option}")
            if text == dropdown_option:
                try_getting(option, driver).click()
                print(f"Successfully set option: {text}")
                return
    except ElementClickInterceptedException:
        print("ERROR: Element click intercepted.")
        rest()