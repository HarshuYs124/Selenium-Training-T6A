from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By


o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.zomato.com/jaipur/order")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//a[text()='Log in']").click()
sleep(2)
driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@id="auth-login-ui"]'))
driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@title="Sign in with Google Button"]'))
driver.find_element(By.XPATH,"//span[text()='Sign in with Google']").click()