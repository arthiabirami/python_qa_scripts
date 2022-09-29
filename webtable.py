from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1)

driver.get("https://testautomationpractice.blogspot.com/")
driver .maximize_window()


#1) count number of rows and columns
rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
columns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))

#print(rows,columns)

#2)read specific row & column data
data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[2]/td[2]").text
#print(data)

#3)printing all the datas in  rows and columns 

# for r in range(2,rows+1):
#   for c in range(1,columns+1):   # to iterate the rows and columns 
#       data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#       print(data,end='          ')
#   print() 

#4)read data on condition base

for r in range(2,rows+1):
    price=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]") 
    if price == "300":
      author=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]")
      print(author,"      ",price)

driver.quit()