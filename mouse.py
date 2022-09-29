from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# Selenium intialization
ser_obj=Service()
driver = webdriver.Chrome(service=ser_obj)
# Driver login details
driver.get("https://opensource-demo.orangehrmlive.com/")


driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
time.sleep(3)

admin = driver.find_element(By.XPATH,"//a[@id='menu_admin_viewAdminModule']")
usrmgnt = driver.find_element(By.XPATH,"//a[@id='menu_admin_UserManagement']")
users = driver.find_element(By.XPATH,"//a[@id='menu_admin_viewSystemUsers']")



act = ActionChains(driver)
act.move_to_element(admin).move_to_element(usrmgnt).move_to_element(users).click().perform()

searchbtn = driver.find_element(By.XPATH,"//input[@id='searchBtn']")
act.context_click(searchbtn).perform()