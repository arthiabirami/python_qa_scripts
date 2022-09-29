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

#admin->usermanagement->users
driver.find_element(By.XPATH,"//a[@id='menu_admin_viewAdminModule']").click()
driver.find_element(By.XPATH,"//a[@id='menu_admin_UserManagement']").click()
driver.find_element(By.XPATH,"//a[@id='menu_admin_viewSystemUsers']").click()

rows=len(driver.find_elements(By.XPATH,"//table[@id='resultTable']/tbody/tr"))
for r in range(1, rows):
	tds = driver.find_elements(By.XPATH,"//table[@id='resultTable']/tbody/tr["+str(r)+"]/td")
	#print(tds[1].text)
	if tds[2].text == "ESS":
	# 	print (tds[3].text)
		print(tds[1].text,"   ",tds[2].text)


driver.quit()
# driver.find_elements(By.XPATH,"//table[@id='resultTable']/tbody/tr/td[3]")
