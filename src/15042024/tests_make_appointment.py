import pytest
import allure
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement


def test_verify_login_book_appointment_form():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_button = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_button.click()


def test_verify_make_appointment_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_button = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_button.click()
    curr_url = driver.current_url
    assert curr_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"


def test_verify_make_appointment_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(3)
    make_appointment_button = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_button.click()
    #username = driver.find_element(By.XPATH, "//input[@value='John Doe']").text
    #print(username)
    #password = driver.find_element(By.XPATH, "//input[@value='ThisIsNotAPassword']").text
    #print(password)
    time.sleep(2)
    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID, "btn-login").click()
    time.sleep(5)
    header = driver.find_element(By.TAG_NAME, "h2").text
    print(header)
    assert header == "Make Appointment"

