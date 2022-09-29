from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# Selenium intialization
ser_obj=Service()
driver = webdriver.Chrome(service=ser_obj)
# Driver login details
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
driver.implicitly_wait()


button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
act = ActionChains(driver)
act.context_click(button).perform()

List=driver.find_elements(By.XPATH,"//ul[@class='context-menu-list context-menu-root']/li")

for li in List:
	if li.text == "Copy":
		li.click()
		break
