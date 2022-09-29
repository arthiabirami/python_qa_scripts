from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # this module is for dropdown list

ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1) # launch the browser

driver.get("https://testautomationpractice.blogspot.com/")
driver .maximize_window()

drop=driver.find_element(By.XPATH,"//select[@id='speed']")
speed=Select(drop)

File=driver.find_element(By.XPATH,"//select[@id='files']")
file=Select(File)

Product=driver.find_element(By.XPATH,"//select[@id='products']")
product=Select(Product)



#select option from the dropdown using buit in methods
speed.select_by_visible_text("Medium")
file.select_by_value("2")
#product.select_by_index(3)

#capture all the options and print 
allopts=product.options
print("total no of products:",len(allopts)) 

# for opt in allopts:
# 	print(opt.text)

#select option from dropdown without using buitl in methods

for opt in allopts:
	if opt.text=="Google":
		opt.click()
     

