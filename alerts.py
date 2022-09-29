from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1) # launch the browser

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver .maximize_window()


driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)


alertwindow=driver.switch_to.alert  #this is built in method in selenium

print(alertwindow.text)
alertwindow.send_keys("welcome")
#alertwindow.accept()  # this will click ok button
alertwindow.dismiss()  #this will click cancel button
