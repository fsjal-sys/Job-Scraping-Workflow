from utils import *
from selectors import l

def setup(driver):
    driver.get("https:ca.indeed.com")
    rest()

def login():
    pass

def main():
    driver = driver_setup()
    setup(driver)

main()