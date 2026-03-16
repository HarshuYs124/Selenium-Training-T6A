from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#userName").send_keys("Harshita") # we can put #id also in css_selector
driver.find_element(By.XPATH,"//input[@placeholder='Full Name']").send_keys("Harshita")
sleep(2)
driver.find_element(By.XPATH,"//button[type()='Submit']").click()
driver.find_element(By.XPATH,"//button[.='Submit']").click() #this or that^|
sleep(2)

driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,"//span[text()='Refrigerators']").click()
#xpath using contains attribute
driver.find_element(By.XPATH,"//a[contains(@href,'accelerator.amazon.in')]").click()
#xpath using contains text
driver.find_element(By.XPATH,"//span[contains(text(),'Cushion covers')]").click()
driver.find_element(By.XPATH,"(//div[@class='navFooterColHead'])[3]").click()

sleep(2)