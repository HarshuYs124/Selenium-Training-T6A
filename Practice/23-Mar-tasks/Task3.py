from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(10)

sleep(3)
actions = ActionChains(driver)
actions.scroll_by_amount(0, 8000).perform()

print("Flipkart: ")
print("ID : ",driver.current_window_handle)
print("Title : ",driver.title)
print("URL : ",driver.current_url)

sleep(3)

myntra=driver.find_element(By.LINK_TEXT, "Myntra").click()
driver.switch_to.window(driver.window_handles[1])
print("Myntra: ")
print("ID : ",driver.current_window_handle)
print("Title : ",driver.title)
print("URL : ",driver.current_url)

sleep(3)
driver.switch_to.window(driver.window_handles[0])
Cleartrip=driver.find_element(By.LINK_TEXT, "Cleartrip").click()
driver.switch_to.window(driver.window_handles[2])
print("Cleartrip: ")
print("ID : ",driver.current_window_handle)
print("Title : ",driver.title)
print("URL : ",driver.current_url)

sleep(3)
driver.switch_to.window(driver.window_handles[0])
Shopsy=driver.find_element(By.LINK_TEXT, "Shopsy").click()
driver.switch_to.window(driver.window_handles[3])
print("Shopsy: ")
print("ID : ",driver.current_window_handle)
print("Title : ",driver.title)
print("URL : ",driver.current_url)

driver.quit()