from utils import *
from time import sleep
from CSS_selectors import Selectors
from selenium.common.exceptions import ElementClickInterceptedException

def hCaptcha_check(element_selector, driver):
    # Returns True if hCaptcha is present, false if not present

    print("Doing a timed hCaptcha check...")
    hCaptcha_iFrame_element = try_getting_timed(element_selector, driver, 10)
    return hCaptcha_iFrame_element is not None

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

def is_logged_in(driver):
    print("Checking for autologin... ")

    current_URL = driver.current_url

    try_getting_timed(Selectors.LOGIN_CHECK_ELEMENT, driver, 5).click()

    if (driver.current_url == current_URL): return True
    else: return False

def set_dropdown_option(driver, options, menu, dropdown_option):
    print(f"Setting dropdown option: {dropdown_option}")
    sleep(1)
    try:
        try_getting(menu, driver).click()
        for option in options:
            text = try_getting(option, driver).text
            text = format_dropdown_text(text)
            print(text)
            if text == dropdown_option:
                try_getting(option, driver).click()
                print(f"Set option: {text}")
                return
    except ElementClickInterceptedException:
        print("ERROR: Element click intercepted.")
        rest()

def login(driver):
    print("######## Beginning LOGIN PROCESS ########")

    email, password = get_credentials()

    driver.get("https://ca.indeed.com")
    load_cookies(driver)

    logged_in = is_logged_in(driver)
    print(f"Autlogin: {logged_in}")

    if logged_in: return

    try_getting(Selectors.LOGIN_BUTTON, driver).click() # Click on login button
    sleep(1)
    try_getting(Selectors.EMAIL_INPUT, driver).send_keys(email) # Enter login details
    sleep(1)
    try_getting(Selectors.EMAIL_CONTINUE_BUTTON, driver).click() # Click on login button
    sleep(1)

    hCaptcha_present = hCaptcha_check(Selectors.LOGIN_HCAPTCHA_IFRAME, driver) # First potential hCaptcha check
    print(f"hCaptcha present: {hCaptcha_present}")
    if hCaptcha_present: 
        hCaptcha_actions(Selectors.LOGIN_HCAPTCHA_IFRAME, driver)
        try_getting(Selectors.EMAIL_CONTINUE_BUTTON, driver).click()
        sleep(1)

    try_getting(Selectors.LOGIN_WITH_PASSWORD_LINK, driver).click() # Click on link to login with password
    sleep(5)
    try_getting_timed(Selectors.PASSWORD_INPUT, driver, 5).send_keys(password)

    sleep(1)
    try_getting(Selectors.SIGN_IN_BUTTON, driver).click()

    hCaptcha_present = hCaptcha_check(Selectors.PASSWORD_HCAPTCHA_IFRAME, driver) # Second potential hCaptcha check
    print(f"hCaptcha present: {hCaptcha_present}")
    if hCaptcha_present: 
        hCaptcha_actions(Selectors.PASSWORD_HCAPTCHA_IFRAME, driver)
        try_getting_timed(Selectors.PASSWORD_INPUT, driver, 10).send_keys(password)
        sleep(1)
        try_getting(Selectors.SIGN_IN_BUTTON, driver).click()
    
    save_cookies(driver)

    print("######## LOGIN PROCESS COMPLETE ########\n")

def job_search(driver):
    sleep(3)
    print("######## Beginning JOB SEARCH PROCESS ########")

    search_term, location, date_posted, distance, job_type = get_job_search_variables()

    try_getting(Selectors.KEYWORDS_SEARCH_INPUT, driver).send_keys(search_term)
    clear_input_field(try_getting(Selectors.LOCATION_SEARCH_INPUT, driver))
    try_getting(Selectors.LOCATION_SEARCH_INPUT, driver).send_keys(location)
    try_getting(Selectors.JOB_SEARCH_BUTTON, driver).click()

    set_dropdown_option(driver, Selectors.DATE_POSTED_DROPDOWN_OPTIONS, Selectors.DATE_POSTED_DROPDOWN_MENU, date_posted)
    set_dropdown_option(driver, Selectors.DISTANCE_DROPDOWN_OPTIONS, Selectors.DISTANCE_DROPDOWN_MENU, distance)
    set_dropdown_option(driver, Selectors.JOB_TYPE_DROPDOWN_OPTIONS, Selectors.JOB_TYPE_DROPDOWN_MENU, job_type)

    rest()

def main():
    driver = driver_setup()
    login(driver)
    job_search(driver)
    
main()