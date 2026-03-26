from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By


o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_experimental_option("prefs",{"safebrowsing.enabled":True})
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
sleep(2)
alert= driver.switch_to.alert
#print alert text
print("alert text :",alert.text)
alert.accept()
sleep(2)

#js confirm
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
sleep(2)
alert= driver.switch_to.alert
#print alert text
print("alert text :",alert.text)
alert.accept()
sleep(2)

#js prompt
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
sleep(2)
alert= driver.switch_to.alert
#print alert text

alert.send_keys("hello")
print("alert text :",alert.text)
alert.accept()
sleep(2)
driver.quit()