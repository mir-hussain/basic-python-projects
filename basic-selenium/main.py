from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_web_driver = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_web_driver)

driver.get("https://www.python.org/")

menu = driver.find_element(
    By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

items = menu.find_elements(By.TAG_NAME, "li")

events = {}

for index, item in enumerate(items):
    events[index] = {
        "date": item.find_element(By.CSS_SELECTOR, "time").text,
        "name": item.find_element(By.TAG_NAME, "a").text
    }
