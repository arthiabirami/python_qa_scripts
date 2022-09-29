from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1) # launch the browser

driver.get("http://automationpractice.com")
driver.maximize_window() #this will maximize the window
#locator by name 
driver.find_element(By.NAME,"search_query").send_keys("women T-shirts") #search box
driver.find_element(By.NAME,"submit_search").click()
#link text and partial link text
driver.find_element(By.LINK_TEXT,"Women").click() #opens the sublink women in the webpage
                                                  #has to give fulltext of the title in <a tag
driver.find_element(By.PARTIAL_LINK_TEXT,"Sleeve T-shirts").click()#has to give partialtext
driver.find_element(By.NAME,"Submit").click() #add to cart
#driver.find_element(By.XPATH("//span[contains(@class,'continue btn btn-default button exclusive-medium') and contains(text(), 'Continueshopping')]")).click()



#driver.close()

