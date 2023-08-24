from utils import *
from time import sleep
from CSS_selectors import Selectors

def hCaptcha_check(driver):
    print("Doing an hCaptcha check...")
    hCaptcha_iFrame_element = try_getting(Selectors.HCAPTCHA_IFRAME, driver)
    print("Switching to iFrame...")
    driver.switch_to.frame(hCaptcha_iFrame_element)
    print("Switched to hCaptcha iFrame")

    try_getting(Selectors.HCAPTCHA_CHECKBOX, driver).click()
    print("Waiting for hCaptcha checkbox feedback...")
    sleep(5)
    driver.switch_to.default_content()
    print("Back to default content.")


def login(driver):
    email, password = get_credentials()

    driver.get("https://ca.indeed.com")

    try_getting(Selectors.LOGIN_BUTTON, driver).click() # Click on login button
    sleep(1)
    try_getting(Selectors.EMAIL_INPUT, driver).send_keys(email) # Enter login details
    sleep(1)
    try_getting(Selectors.EMAIL_CONTINUE_BUTTON, driver).click() # Click on login button
    sleep(1)

    hCaptcha_check(driver) # First potential hCaptcha check
    rest()

    try_getting(Selectors.LOGIN_WITH_PASSWORD_LINK, driver).click() # Click on link to login with password
    sleep(1)
    try_getting(Selectors.PASSWORD_INPUT, driver).send_keys(password)
    sleep(1)
    try_getting(Selectors.SIGN_IN_BUTTON, driver).click()

def job_search(driver):
    search_term, location = get_search_terms()

    try_getting(Selectors.KEYWORDS_SEARCH_INPUT, driver).send_keys(search_term)
    try_getting(Selectors.LOCATION_SEARCH_INPUT, driver).send_keys(location)
    rest()

def main():
    driver = driver_setup()
    login(driver)
    job_search(driver)
    
main()