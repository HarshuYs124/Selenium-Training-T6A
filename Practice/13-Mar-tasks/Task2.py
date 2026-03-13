from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()
sleep(2)
driver.get("https://www.amazon.in")
sleep(3)

# Update Location using ID
driver.find_element(By.ID, "nav-global-location-popover-link").click()
sleep(3)
driver.close()
driver.quit()
