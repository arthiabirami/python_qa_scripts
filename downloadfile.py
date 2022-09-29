from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import os
location = os.getcwd() #---this will choose the current location

def chrome_setup():
	from selenium.webdriver.chrome.service import Service
	ser_obj= Service()
	#downfile in desired location
	preferences={"download.defult_directory":location} 
	#-- this is the dictionary variable{variable:value}
	ops=webdriver.ChromeOptions() 
	ops.add_experimental_option("prefs",preferences)#-- creating object and caling method where "prefs" is like syntex
	driver = webdriver.Chrome(service=ser_obj,options=ops) # launch the browser
	return driver

def edge_setup():
	from selenium.webdriver.edge.service import Service
	ser_obj1 = Service()
	preferences={"download.defult_directory":location} #-- this is the dictionary variable{variable:value}
	ops=webdriver.ChromeOptions() 
	ops.add_experimental_option("prefs",preferences)#-- creating object and caling method where "prefs" is like syntex
	driver = webdriver.Edge(service=ser_obj1,options=ops) # launch the browser
	return driver

def firefox_setup():
	from selenium.webdriver.firefox.service import Service
	ser_obj1 = Service()
	#settings to avoid the ask window
	ops=webdriver.FirefoxOptions() 
	ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword") #-- application/msword is the mime type
	#to specify the type of file to download to refer https://www.sitepoint.com/mime-types-complete-list/
	ops.set_preference("browser.download.manager.showWhenStarting",False)
	ops.set_preference("browser.download.folderList",2)#0-desktop 1-default loc 2- desierd loc
	ops.set_preference("browser.download.dir",location)
	driver = webdriver.Firefox(service=ser_obj1,options=ops) # launch the browser
	return driver

 

driver=chrome_setup()
#driver=edge_setup()
#driver=firefox_setup()
driver.get("https://filesamples.com/formats/doc")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[1]/main/div[2]/div[2]/a").click()
# act = ActionChains(driver)
# act.moveToElement(ele).click().perform()








