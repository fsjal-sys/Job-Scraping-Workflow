from utils import *
from time import sleep
from CSS_selectors import Selectors

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

def login(driver):
    print("######## Beginning LOGIN PROCESS ########")

    email, password = get_credentials()

    driver.get("https://ca.indeed.com")

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

    print("######## LOGIN PROCESS COMPLETE ########\n")

def job_search(driver):
    print("######## Beginning JOB SEARCH PROCESS ########")

    search_term, location = get_search_terms()

    try_getting(Selectors.KEYWORDS_SEARCH_INPUT, driver).send_keys(search_term)
    try_getting(Selectors.LOCATION_SEARCH_INPUT, driver).clear()
    try_getting(Selectors.LOCATION_SEARCH_INPUT, driver).send_keys(location)
    rest()

def main():
    driver = driver_setup()
    login(driver)
    job_search(driver)
    
main()