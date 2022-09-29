from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1)

driver.get("https://jqueryui.com/datepicker/")
driver .maximize_window()

driver.switch_to.frame(0) 

#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("02/04/2020")

year="2023"
month="June"
day="30"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

while True:
	mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
	yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
	print(mon, yr)
	if mon == month and yr == year:
		break;
	else:
		driver.find_element(By.XPATH,"//a[@title='Next']").click()



days=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in days:
	if ele.text==day:
		ele.click()
		break;
	



#driver.quit()