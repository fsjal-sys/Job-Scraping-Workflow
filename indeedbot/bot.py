from utils import *

def setup(driver):
    driver.get("https:ca.indeed.com")
    rest()

def login():
    pass

def main():
    driver = driver_setup()
    #driver.get("https://www.google.com")
    email, password = get_credentials()
    print(email)
    print(password)
    setup(driver)

main()