import time
import pytest
import allure

from selenium import webdriver

def test_open_google():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com")
    page_title = driver.title
    page_source = driver.page_source
    print(page_title)
    #print(page_source)
    time.sleep(5)