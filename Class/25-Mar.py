import time
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.implicitly_wait(10)

import os
driver.get("https://www.google.com")
driver.maximize_window()
#driver.save_screenshot("screenshot-1.png")

folder=os.path.join(os.getcwd(),'screenshot')
os.makedirs(folder,exist_ok=True)
driver.save_screenshot(f'{folder}/screenshot.png')

ele=driver.find_element(By.XPATH,"//textarea[@title='Search']")
ele.send_keys("Books")
ele.screenshot(f'{folder}/screenshot_page.png')

timestamp=time.strftime("%Y%m%d-%H%M%S")
ele.screenshot(f'{folder}/screenshot_ele_{timestamp}.png')
# expected='Google'
# actual=driver.title
# assert expected==actual,"Title mismatched"  #after comma in inverted commas we write the error that will be shown in case of an error as an error message
#
# driver.find_element(By.XPATH,"//textarea[@title='Search']").send_keys("Books")


#PRACTICE
driver.get("https://www.amazon.in")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()
expected='Amazon.in Bestsellers: The most popular items on Amazon'
actual=driver.title
assert expected==actual,"TITLE MISMATCHED"
driver.quit()