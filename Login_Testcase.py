import time
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Create a Firefox driver
driver = webdriver.Firefox()

# Maximize the window size
driver.maximize_window()

# Open the website
driver.get("https://stage-exchange.worldtakeover.io/")
time.sleep(10)
driver.find_element(By.XPATH,"//button[@type='button']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys("atul@gmail.com")
#time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("Test@123")
#time.sleep(5)
