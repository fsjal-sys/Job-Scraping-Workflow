from utils import *
from time import sleep
from CSS_selectors import Selectors

def login(driver):
    email, password = get_credentials()

    driver.get("https://ca.indeed.com")
    
    try_getting(Selectors.LOGIN_BUTTON, driver).click()
    sleep(1)
    try_getting(Selectors.EMAIL_INPUT, driver).send_keys(email)
    sleep(1)
    try_getting(Selectors.EMAIL_CONTINUE_BUTTON, driver).click()
    sleep(1)
    try_getting(Selectors.LOGIN_WITH_PASSWORD_LINK, driver).click()
    sleep(1)
    try_getting(Selectors.PASSWORD_INPUT, driver).send_keys(password)
    sleep(1)
    try_getting(Selectors.SIGN_IN_BUTTON, driver).click()

    rest()

def main():
    driver = driver_setup()
    login(driver)
    
main()