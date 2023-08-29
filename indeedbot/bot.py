from utils import *
from time import sleep
from CSS_selectors import Selectors

# Will refactor all code in a later date, after application functionality is put in
def login(driver):
    print("######## BEGINNING LOGIN PROCESS ########")

    email, password = get_credentials()

    driver.get("https://ca.indeed.com")
    load_cookies(driver)

    logged_in = is_logged_in(driver)
    print(f"Autologin: {logged_in}")

    if logged_in: 
        print("######## LOGIN PROCESS COMPLETE ########\n")
        return

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
    password_input_selector = input("Enter the CSS Selector for the password input here: ")
    password_input_field_element = try_getting_timed(password_input_selector, driver, 5)
    password_input_field_element.send_keys(password)
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
    print("######## BEGINNING JOB SEARCH PROCESS ########")

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

    print("######## JOB SEARCH PROCESS COMPLETE ########\n")

def check_for_employer_questions(driver):
    
    current_URL = driver.current_url
    rest()

def send_application(driver):
    first_name, last_name, phone_number, city = get_job_application_variables()

    if (is_indeed_application(driver)):
        print("This job has an Indeed application.")
        try_getting(Selectors.INDEED_APPLY_BUTTON, driver).click()
        driver.switch_to.window(driver.window_handles[1])

        clear_input_field(try_getting(Selectors.FIRST_NAME_INPUT_FIELD, driver))
        try_getting(Selectors.FIRST_NAME_INPUT_FIELD, driver).send_keys(first_name)
        clear_input_field(try_getting(Selectors.LAST_NAME_INPUT_FIELD, driver))
        try_getting(Selectors.LAST_NAME_INPUT_FIELD, driver).send_keys(last_name)
        clear_input_field(try_getting(Selectors.CITY_INPUT_FIELD, driver))
        try_getting(Selectors.CITY_INPUT_FIELD, driver).send_keys(city)
        clear_input_field(try_getting(Selectors.PHONE_NUMBER_INPUT_FIELD, driver))
        try_getting(Selectors.PHONE_NUMBER_INPUT_FIELD, driver).send_keys(phone_number)
        try_getting(Selectors.INDEED_APPLICATION_CONTACT_CONTINUE_BUTTON, driver).click()
        try_getting(Selectors.INDEED_SELECT_RESUME, driver).click()

        indeed_applcation_resume_continue_button = try_getting(Selectors.INDEED_APPLICATION_RESUME_CONTINUE_BUTTON, driver)
        indeed_applcation_resume_continue_button.click()

        check_for_employer_questions(driver)
    else:
        print("This job has an external application.")

def is_indeed_application(driver):
    indeed_apply_button = try_getting_timed(Selectors.INDEED_APPLY_BUTTON, driver, 3)
    if indeed_apply_button == None:
        apply_button_link = try_getting_timed(Selectors.APPLY_BUTTON_LINK, driver, 3)
        if apply_button_link == None: print("Error finding apply button.")
        else: return False
    else: return True

def job_applications(driver):
    print("######## BEGINNING JOB APPLICATION PROCESS ########")

    """
    applied_jobs = []
    open_jobs = []

    job_list = try_getting_child_elements(try_getting(Selectors.JOB_SEARCH_LEFT_PANE, driver), "#mosaic-provider-jobcards > ul > li")
    for job in job_list:
        job_details = try_getting_child_elements(job, Selectors.CHILD_JOB_VISIT_STATUS)
        for detail in job_details: 
            if (detail.text.split(" ")[0] == "Visited"): 
                applied_jobs.append(job)
            else: 
                open_jobs.append(job)

    for job in open_jobs:
        send_application()
    """

    job_list = try_getting_child_elements(try_getting(Selectors.JOB_SEARCH_LEFT_PANE, driver), "#mosaic-provider-jobcards > ul > li")
    for job in job_list:
        job.click()
        send_application(driver)

    rest()

def main():
    driver = driver_setup()
    login(driver)
    job_search(driver)
    job_applications(driver)
    
main()