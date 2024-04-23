import pytest
import allure
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


@pytest.mark.positive
@allure.title("Verify Validations on Registration form")
@allure.description("Verify the validations on Registration form when user submit the empty input")
def test_submit_validations():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    time.sleep(3)
    driver.switch_to.frame(driver.find_element(By.ID, "result"))
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("test@123")
    driver.find_element(By.XPATH, "//input[@id='password2']").send_keys("test@123")
    driver.find_element(By.XPATH, "//*[text()='Submit']").click()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="empty-username", attachment_type=AttachmentType.PNG)
    error_message = driver.find_element(By.XPATH, "//input[@id='username']//following::small").text
    print(error_message)
    assert (error_message == "Username must be at least 3 characters")

