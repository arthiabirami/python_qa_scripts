from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1) # launch the browser
driver.implicitly_wait(10) #sometimes it may delay in loadind to perform some actions on the element where 'no such element' can be thrown
                           # to overcome we are using implicitly wait.

driver.get("https://www.google.com/") # add /register for conditional commands
driver.maximize_window()

searchbox=driver.find_element(By.NAME,"q")
searchbox.send_keys("selenium")
searchbox.submit() #To perform the action of enter key

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
driver.quit() #also qiut the implicitly wait
