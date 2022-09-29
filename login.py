from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Selenium intialization
ser_obj=Service()
driver = webdriver.Chrome(service=ser_obj)
# Driver login details
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

# Test case
act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
	print("login test passed")
else:
    print("login test is failed")	
# Close Driver
driver.close()
