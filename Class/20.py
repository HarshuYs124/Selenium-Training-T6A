from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("shoes for women")
sleep(3)
list=driver.find_elements(By.XPATH,"//div[@class='s-suggestion-container']")
#
# for i in list:
#     print(i.text)
list[2].click()
sleep(3)

#dropdowns
driver.get("file:///C:/Users/Harshita%20Yadav/AppData/Local/Packages/5319275A.WhatsAppDesktop_cv1g1gvanyjgm/LocalState/sessions/607B39ED87B5043A6CB0E552BDAC5396D0BB27DA/transfers/2026-12/E22_Dropdowns.html")
driver.maximize_window()

dropdown=driver.find_element(By.ID,'state')
option=Select(dropdown)
#option.select_by_visible_text('Maharastra')
option.select_by_value("MH")
sleep(5)
option.select_by_index(0)

dropdown=driver.find_element(By.ID,'hobby')
option=Select(dropdown)
option.select_by_visible_text('Dance')
option.select_by_index(1)
option.select_by_index(2)
sleep(3)

#deselect
option.deselect_by_index(1)
option.deselect_by_visible_text('Dance')
option.deselect_all()
