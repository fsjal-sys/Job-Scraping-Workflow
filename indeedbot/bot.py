from utils import *
from time import sleep
from CSS_selectors import Selectors

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
    if job_alert_popup_present(driver): job_alert_popup_close(driver)

    set_dropdown_option(driver, Selectors.DISTANCE_DROPDOWN_OPTIONS, Selectors.DISTANCE_DROPDOWN_MENU, distance)
    if job_alert_popup_present(driver): job_alert_popup_close(driver)

    set_dropdown_option(driver, Selectors.JOB_TYPE_DROPDOWN_OPTIONS, Selectors.JOB_TYPE_DROPDOWN_MENU, job_type)
    if job_alert_popup_present(driver): job_alert_popup_close(driver)

    rest()

def main():
    driver = driver_setup()
    login(driver)
    job_search(driver)
    
main()