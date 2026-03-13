from selenium.webdriver import Chrome
driver=Chrome()
from selenium.webdriver import Edge
driver=Edge()
from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)


#TO OPEN A WEB PAGE
driver.get("https://www.google.com")


#MAXIXMIZE MINIMIZE AND FULLSCREEN ARE BROWSER WINDOW METHODS

#TO MAXIMISE THE OPENED WINDOW
driver.maximize_window() #the return type of this maximise command is none

#TO MINIMISE THE OPENED WINDOW
driver.minimize_window()

#TO FULLSCREEN THE OPENED WINDOW
driver.fullscreen_window()

driver.get("https://www.google.com")
driver.maximize_window()
sleep(2)
driver.minimize_window()
sleep(2)
driver.fullscreen_window()
sleep(2)

#  TO FETCH THE TITLE OF PAGE
#TITLE is a VERIFICATION property
# TITLE ,current_url,and page_source are the verification properties these are not functions or methods so to call them we dont have to use ().these are not methods these are properties
title=driver.title
print(title)
print(driver.current_url)
print(driver.page_source)


#PRACTICE OF THE ABOVE
driver.get("https://google.com/")
driver.maximize_window()
sleep(2)
driver.minimize_window()
sleep(2)
driver.fullscreen_window()
title=driver.title
print(title)
print(driver.current_url)
print(driver.page_source)
name=driver.name
print(name)
sleep(7)
driver.close() # only the driver opened tab will be closed
driver.quit() # entire browser all the tabs will be closed

from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)


#TO OPEN A WEB PAGE
driver.get("https://www.amazon.com")
print(driver.title)
driver.back()
sleep(10)
driver.forward()
sleep(5)
driver.refresh()
