from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1)

driver.get("https://admin-demo.nopcommerce.com/login")
#driver.find_element(By.ID,"Email").clear()
usrname=driver.find_element(By.XPATH,"//input[@id='Email']")
usrname.clear()
usrname.send_keys("admin@yourstore.com")
print(usrname.get_attribute('id'))  
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

act_title = driver.title
exp_title = "Dashboard / nopCommerce administration"

if act_title == exp_title:
    print("login test pass")
else:
    print("login test failed")   




driver.close()

