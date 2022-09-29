from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time    
import utils


ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1) 
driver.implicitly_wait
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver .maximize_window()

file = "/Users/sathish/code/python testing/data1.xlsx"
rows = utils.getRowCount(file,"Sheet 1")
print(rows)
for r in range(2,rows+1):
	princ = utils.readData(file,"Sheet 1",r,1)
	rof = utils.readData(file,"Sheet 1",r,2)
	pre1 = utils.readData(file,"Sheet 1",r,3)
	pre2 = utils.readData(file,"Sheet 1",r,4)
	fre = utils.readData(file,"Sheet 1",r,5)
	exp_value = utils.readData(file,"Sheet 1",r,6)

	print(r)
	print(princ)

	driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(princ)
	driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rof)
	driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(pre1)
	preiod = Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
	preiod.select_by_visible_text(pre2)
	frequency = Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
	frequency.select_by_visible_text(fre)
	alertwindow=driver.switch_to.alert
	alertwindow.dismiss()
	# if r == 2:
	# 	driver.find_element(By.XPATH, "//*[@id='wzrk-cancel']").click()
	driver.find_element(By.XPATH,"//div[@class='cal_div']//a[1]").click()
	act_value = driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text


	if float(exp_value) == float(act_value):
		print("test passed")
		utils.writeData(file,"Sheet 1",r,8,"passed")
		utils.fillGreenColor(file,"Sheet 1",r,8)
	else:
		print("test failed")
		utils.writeData(file,"Sheet 1",r,8,"fail")
		utils.fillRedColor(file,"Sheet 1",r,8)
	driver.find_element(By.XPATH,"//img[@class='PL5']").click()
	time.sleep(2)

driver.close()	


	