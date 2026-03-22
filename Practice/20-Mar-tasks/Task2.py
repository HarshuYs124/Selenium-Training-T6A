from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

driver.get("https://www.bmrc.co.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//span[.="English"]').click()
dropdown = driver.find_element(By.CLASS_NAME,"form-control.select.fare-selects")
option = Select(dropdown)
option.select_by_index(1)
sleep(2)
dropdown2 = driver.find_element(By.XPATH,"(//select[@class='form-control select fare-selects'])[2]")
option2 = Select(dropdown2)
option2.select_by_index(2)
driver.find_element(By.CLASS_NAME,"app-btn-box").click()
driver.close()