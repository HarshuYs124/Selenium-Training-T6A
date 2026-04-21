from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://in.pinterest.com/")
driver.maximize_window()
driver.implicitly_wait(10)
sleep(5)
driver.save_screenshot("full_page_task1.png")

ele=driver.find_element(By.XPATH,"(//img)[8]")
action = ActionChains(driver)
action.scroll_to_element(ele).perform()
sleep(2)
ele.screenshot("element_task1.png")

