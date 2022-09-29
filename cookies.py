from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service()
ops=webdriver.ChromeOptions()
ops.headless=True  #-----headless mode
driver = webdriver.Chrome(service=ser_obj,options=ops)
driver.implicitly_wait(10)


driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

cookie=driver.get_cookies() # each cookie have dictionary type pf values
print(len(cookie))

for c in cookie:
	print(c.get('name'),":",c.get('value'))
	#print (c)

driver.add_cookie({"name":"mycookie","value":"124444"})
cookie=driver.get_cookies()
print (len(cookie))

#driver.delete_cookies("any value of the attribute") 
#driver.delete_all_cookies()

driver.quit()