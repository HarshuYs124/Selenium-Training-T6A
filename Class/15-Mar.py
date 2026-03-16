from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
# o.add_argument('--headless')
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

driver.get("https://demoqa.com/webtables")
sleep(2)
salary=driver.find_element(By.XPATH,"//td[text()='Cantrell']/..//td[5] ")
print('salary of Centrell', salary.text)



#fetch element using indexing
driver.get("https://the-internet.herokuapp.com/tables")
driver.maximize_window()
sleep(4)
due=driver.find_element(By.XPATH,"//td[text()='Frank']/../td[4] ")
print('Due of Frank', due.text)
sleep(2)



driver.get("https://the-internet.herokuapp.com/tables")
driver.maximize_window()
sleep(2)
due = driver.find_element(By.XPATH, "//td[text()='Tim']/following-sibling::td[2]")
print("Due of Tim:", due.text)
sleep(2)





