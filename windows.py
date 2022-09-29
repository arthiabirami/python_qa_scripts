from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1) # launch the browser

driver.get("https://opensource-demo.orangehrmlive.com/")
driver .maximize_window()

# windowID= driver.current_window_handle
# print(windowID)    #CDwindow-D503413922F846CBFC36C79F113D54DA 
                    # The ID will change every execution


driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowIDs=driver.window_handles # this return both the id so we should cosider as a list variable

# parentwindow=windowIDs[0] # https://opensource-demo.orangehrmlive.com
# childwindow=windowIDs[1]  # "OrangeHRM, Inc"

# driver.switch_to.window(childwindow)
# print(driver.title)

# driver.switch_to.window(parentwindow)
# print(driver.title)

#approach 2
for winid in windowIDs:
	driver.switch_to.window(winid)
	if driver.title=="OrangeHRM":
		driver.close()



driver.close()