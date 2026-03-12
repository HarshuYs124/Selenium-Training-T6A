from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.wikipedia.com")
sleep(5)
driver.refresh()
sleep(5)
title=driver.title
print(title)
driver.get("https://www.amazon.com")
print(driver.title)
sleep(5)
driver.back()
sleep(3)
driver.close()