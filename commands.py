from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1) # launch the browser

driver.get("https://www.nopcommerce.com/en") # add /register for conditional commands
driver.maximize_window()

#textbox=driver.find_element(By.XPATH,"//input[@id='FirstName']")
#print("display status",textbox.is_displayed())
#print("enable status",textbox.is_enabled())

#country=driver.find_element(By.XPATH,"//input[@id='Newsletter']")
#print(country.is_selected())

#find_element
#element=driver.find_element(By.XPATH,"//footer[@class='footer']//a")
#print(element.text)

#find_elements
elements=driver.find_elements(By.XPATH,"//footer[@class='footer']//a")
print(len(elements))
for ele in elements:
	print(ele.text)






driver.quit()