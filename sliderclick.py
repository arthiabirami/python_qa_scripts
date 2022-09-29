from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# Selenium intialization
ser_obj=Service()
driver = webdriver.Chrome(service=ser_obj)
# Driver login details
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()

act = ActionChains(driver)

# double click
button = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
act.double_click(button).perform()

# drag&drop
drag1 = driver.find_element(By.XPATH,"//img[@alt='the peaks of high tatras']")
drag2 = driver.find_element(By.XPATH,"//img[@alt='The chalet at the Green mountain lake']")
drop = driver.find_element(By.XPATH,"//div[@id='trash']")
act.drag_and_drop(drag1,drop).perform()
act.drag_and_drop(drag2,drop).perform()

slider = driver.find_element(By.XPATH,"//div//div//div//div//div//div//div//div//div//div[4]//div[1]//div[1]//span[1]")

print(slider.location) #{'x': 940, 'y': 1253}

act.drag_and_drop_by_offset(slider,350,0).perform()
slider = driver.find_element(By.XPATH,"//div//div//div//div//div//div//div//div//div//div[4]//div[1]//div[1]//span[1]")
print(slider.location)
# driver.quit

