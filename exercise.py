from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


ser_obj1 = Service()
driver = webdriver.Chrome(service=ser_obj1) # launch the browser
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver .maximize_window()


search=driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']")
search.send_keys("selenium")
search.submit()

elements = driver.find_elements(By.XPATH, "//div[@id='Wikipedia1_wikipedia-search-results']//a")

#print(elements)
for ele in elements:
	ele.click()
	#print(ele.get_attribute("href"))


windows=driver.window_handles
# print(windows)

for i,win in enumerate(windows):  #iterating index
	driver.switch_to.window(win)
	if i>3:
		driver.close()
