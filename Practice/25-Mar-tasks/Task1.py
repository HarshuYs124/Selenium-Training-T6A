
from selenium.webdriver import Chrome,ChromeOptions

from selenium.webdriver.common.by import By


o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
import os
driver.get("https://www.saucedemo.com")
driver.maximize_window()
driver.implicitly_wait(10)
folder=os.path.join(os.getcwd(), "Pictures")
os.makedirs(folder,exist_ok=True)

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("123")
driver.find_element(By.ID,"login-button").click()
expected="https://www.saucedemo.com/inventory.html"
actual= driver.current_url
# if expected == actual:
#     print("Success")
# else:
#     driver.save_screenshot(f"{folder}/screenshot2.png")

assert expected == actual, driver.save_screenshot(f"{folder}/screenshot2.png")