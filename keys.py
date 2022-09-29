from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser_obj=Service()
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://text-compare.com")
driver.maximize_window()
driver.implicitly_wait(3)


text1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
text2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
text1.send_keys("welcome to selenium")

def actions(s, act):
	act.key_down(Keys.COMMAND)
	act.send_keys(s)
	act.key_up(Keys.COMMAND)
	act.perform()

act = ActionChains(driver)

actions("a", act)
actions("c", act)
act.send_keys(Keys.TAB).perform()
actions("v", act)

