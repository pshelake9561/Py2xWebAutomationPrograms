import pytest
import allure
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


@pytest.mark.positive
@allure.title("Verify search functionality")
@allure.description("Verify the list of items returned when useer search for 16gb")
def test_ebay():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.ebay.com")
    time.sleep(5)
    search_item = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
    search_item.send_keys("16gb")

    search_button = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    search_button.click()

    item_list = driver.find_elements(By.XPATH,"//span[@role='heading']")

    for item in item_list:
        item_name = item.text
        print(item_name)

   """ item_price_list = driver.find_elements(By.XPATH,"//span[@class='s-item__price']")

    total = []
    for price in item_price_list:
        item_price = price.text
        print(item_price)
        x = item_price.replace("$", " ").strip()
        total.append(x)

    total.sort()
    print(f"cheapest price is {total[1]}")"""

    product_price_element_list = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")
    prize = []
    for price in product_price_element_list:
        product_price = price.text
        print(product_price)
        x = product_price.replace("$", " ").strip()
        prize.append(x)

    prize.sort()

    #min_price = prize[1]
    print(f"cheapest price is {prize[1]}")

    time.sleep(5)

