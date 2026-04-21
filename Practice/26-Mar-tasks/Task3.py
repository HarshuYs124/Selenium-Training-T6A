from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.ID,'twotabsearchtextbox').send_keys("shoes")
sleep(2)

driver.find_element(By.XPATH,"//div[@id='sac-suggestion-row-4']").click()

dropdown=driver.find_element(By.ID,'s-result-sort-select')
option=Select(dropdown)
option.select_by_visible_text('Newest Arrivals')

# driver.find_element(By.XPATH, "//span[contains(text(),'Free Delivery')]").click()



# from time import sleep, time
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common import actions
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from websocket import send
#
#
#
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver = Chrome(options=o)
# import os
# driver.get("https://www.amazon.in")
# driver.maximize_window()
# driver.implicitly_wait(10)
# folder=os.path.join(os.getcwd(), "Pictures")
# os.makedirs(folder,exist_ok=True)
# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("watches")
# driver.find_element(By.XPATH,"//span[text()=' for women latest']").click()
# sleep(2)
# driver.find_element(By.XPATH,"//span[text()='Sort by:']").click()
# driver.find_element(By.XPATH,"//a[text()='Newest Arrivals']").click()
# driver.find_element(By.XPATH,"(//i[@class='a-icon a-icon-checkbox'])[3]").click()
# ele=driver.find_element(By.XPATH,"//span[text()='Rose Gold Watch AR11775']")
# price=driver.find_element(By.XPATH,"(//span[text()='18,495'])[1]")
# print("watch: ",ele.text)
# print("price: ",price.text)
# driver.quit()