from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
location = os.getcwd() 


ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1) # launch the browser
driver.implicitly_wait(10)

driver.get("https://www.nopcommerce.com/en") # add /register for conditional commands
driver.maximize_window()

driver.save_screenshot(location+"\\homepage.png")

driver.quit()