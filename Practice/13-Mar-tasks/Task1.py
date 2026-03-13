# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get("https://www.selenium.dev")
# sleep(2)
# driver.find_element(By.LINK_TEXT, "Downloads").click()
#
# driver.find_element(By.PARTIAL_LINK_TEXT, "Other Languages Exist").click()
#
# print(driver.title)
# sleep(2)

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.implicitly_wait(10)

# Open Selenium website
driver.get("https://www.selenium.dev/")
sleep(2)
driver.find_element(By.LINK_TEXT, "Downloads").click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "other languages exist").click()
sleep(2)
driver.find_element(By.LINK_TEXT, "Register Now").click()
sleep(2)

# Fetch page title
print(driver.title)

driver.quit()
