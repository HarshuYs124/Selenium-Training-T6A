from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()
sleep(2)
driver.get("https://www.facebook.com")
sleep(3)

driver.find_element(By.NAME, "email").send_keys("harshita@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("12345")

sleep(3)
driver.quit()