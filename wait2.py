from selenium import webdriver
from selenium.common.exceptions import WebDriverException #which imports all kind of exceptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1) # launch the browser

driver.get("https://www.google.com/") # add /register for conditional commands
driver.maximize_window()

# declaration of explicit wait
mywait=WebDriverWait(driver,10,ignored_exceptions=[Exception]) 

searchbox=driver.find_element(By.NAME,"q")
searchbox.send_keys("selenium")
searchbox.submit()

#usage of explicity wait
searchlink=mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
# this will find the element until it capture the element

searchlink.click()

driver.quit()

