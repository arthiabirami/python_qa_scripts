import requests as requests #used for broken link
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1) 

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window

links=driver.find_elements(By.XPATH,'//a') #or (By.TAGNAME,'a')
print("total no of links :",len(links))
count=0

# for link in links:
#   print(link.text)

for link in links:
  url=link.get_attribute("href")

  try:
    res = requests.head(url) # to hit the url
  except:
    None

  if res.status_code >= 400: #to check is it a broken link
    print(url,"  is brokenline")
    count+=1
driver.quit()   