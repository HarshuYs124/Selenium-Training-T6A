from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.lenskart.com/")
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element(By.XPATH,"//a[text()='EYEGLASSES']").click()
sleep(2)
expected='https://www.lenskart.com/eyeglasses.html'
actual=driver.current_url

assert expected == actual, "Invalid url"

driver.find_element(By.XPATH, "//label[text()='Sort By']").click()
sleep(2)

dropdown=driver.find_element(By.ID,'sortByDropdown')
option=Select(dropdown)
option.select_by_visible_text('Most Viewed')
sleep(5)
driver.save_screenshot("lenskart_eyeglasses.png")





