from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_webdriver_path = "c:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_webdriver_path)


driver.get("https:www.facebook.com")


email = driver.find_element(By.NAME, "email")
email.send_keys("test@test.com")

password = driver.find_element(By.NAME, "pass")
password.send_keys("tore_kan_bolbo?")

login = driver.find_element(By.NAME, "login")
login.click()

while True:
    pass
