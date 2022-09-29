from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj=Service()
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

reglink = Keys.COMMAND + Keys.RETURN
driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)
# driver.switch_to.new_window('tab')  #---- this is only avaliable for selenium 4 
# driver.get("https://www.orangehrm.com") #---- this website will open in another tab or window if we mention
