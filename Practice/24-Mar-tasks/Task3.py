from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://google.com")
driver.maximize_window()
driver.implicitly_wait(10)

print("Google")
print("Title: ",driver.title)
print("URL: ",driver.current_url)

driver.switch_to.new_window()
driver.get("https://www.flipkart.com/")
driver.switch_to.window(driver.window_handles[1])
print("Flipkart")
print("Title: ",driver.title)
print("URL: ",driver.current_url)

driver.switch_to.new_window()
driver.get("https://www.myntra.com/")
driver.switch_to.window(driver.window_handles[2])
print("Myntra")
print("Title: ",driver.title)
print("URL: ",driver.current_url)


driver.close()
driver.switch_to.window(driver.window_handles[1])
driver.close()