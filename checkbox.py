from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1) # launch the browser

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver .maximize_window()

#1) select specific checkbox
#driver.find_element(By.XPATH,"//input[@id='monday']").click()

#2)select all the checkboxes
chkbox=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,  'day')]")
print(len(chkbox))

#approach 1

for i in range (len(chkbox)):
	chkbox[i].click()

#approch 2

#for box in chkbox:
#	box.click()
	
#3)select multiple checkboxes in choice

#for box in chkbox:
#	day=box.get_attribute('id')
#	if day=='tuesday' or day=='wednesday':
#		box.click()

#4) selcect last two checkboxes
# for i in range (len(chkbox)-2,len(chkbox)):
# 	chkbox[i].click()

#5) select first 4 checkboxes
# for i in range (len(chkbox)):
# 	if i<5 :
# 		chkbox[i].click()

#6) clearing all checkboxes

for box in chkbox:
	if box.is_selected():
		box.click()

		












