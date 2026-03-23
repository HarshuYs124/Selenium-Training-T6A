from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

''' Dynamic Button '''
ele = driver.find_element(By.XPATH,'//button[text()="START"]')
ele.send_keys(Keys.ENTER)

''' Mouse Hover'''
ele = driver.find_element(By.XPATH,'//button[text()="Point Me"]')
action = ActionChains(driver)
sleep(4)
action.move_to_element(ele).perform()

''' Double Click '''
ele = driver.find_element(By.XPATH,'//input[@id="field1"]')
action = ActionChains(driver)
sleep(3)
action.double_click(ele).perform()
ele.send_keys(Keys.CONTROL,'a')
ele.send_keys(Keys.CONTROL,'c')
ele2=driver.find_element(By.XPATH,'//input[@id="field2"]')
ele2.send_keys(Keys.CONTROL,'v')

''' Drag and Drop '''
ele=driver.find_element(By.XPATH,'//div[@id="draggable"]')
ele2=driver.find_element(By.XPATH,'//div[@id="droppable"]')
action = ActionChains(driver)
sleep(3)
action.pause(2).drag_and_drop(ele,ele2).perform()

driver.close()