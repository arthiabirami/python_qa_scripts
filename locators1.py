from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1) # launch the browser

driver.get("http://facebook.com")
driver.maximize_window() 

#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("arthi") #tag and class
#driver.find_element(By.CSS_SELECTOR,"input#pass").send_keys("acbur") #tag and id

#driver.find_element(By.XPATH,"//input[@id='email']").send_keys("arthi") #relative Xpath
#driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input").send_keys("abi") #fullxpath

driver.find_element(By.XPATH,"//input[@id='email' or @name='search_quey']").send_keys("arthi") #or
driver.find_element(By.XPATH,"//input[@name='pass' and @class='inputtext _55r1 _6luy _9npi']").send_keys("arthi") #and