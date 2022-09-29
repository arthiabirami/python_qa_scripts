from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # this module is for dropdown list


ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver .maximize_window()

driver.find_element(By.XPATH,"//input[@id='dob']").click()

month = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
month.select_by_visible_text("Dec")

year = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
year.select_by_visible_text("1990")

days=driver.find_elements(By.XPATH,"//table[contains(@class,'ui-datepicker-calendar')]/tbody/tr/td/a")

for ele in days:
	if ele.text == "24":
		ele.click()
		break;