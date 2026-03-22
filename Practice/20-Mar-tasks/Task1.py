from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from websocket import send

o=ChromeOptions()
o.add_experimental_option("detach",True)

#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
driver=Chrome(options=o)
driver.get("https://www.zomato.com/jaipur/restaurants")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME,"sc-dBfaGr.dyyfrm").send_keys("waffle")
driver.find_element(By.CLASS_NAME,"sc-dBfaGr.dyyfrm").click()
list = driver.find_elements(By.XPATH,'//p[@class="sc-1hez2tp-0 sc-gFXMyG jkvifB"]')
for i in list:
    print(i.text)
list[1].click()