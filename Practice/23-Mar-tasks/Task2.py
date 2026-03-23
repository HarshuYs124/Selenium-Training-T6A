from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

from selenium.webdriver.common.keys import Keys

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

# launch
driver.get("https://www.nike.in/")
driver.maximize_window()
driver.implicitly_wait(10)

ele = driver.find_element(By.XPATH,'//span[text()="Kids"]')
actions = ActionChains(driver)
sleep(5)

# Hover on kids
actions.move_to_element(ele).perform()
ele.send_keys(Keys.ENTER)
shop = driver.find_element(By.XPATH,'//a[@href="/elevate-their-style/c/94039"]')

# Scroll to shop
actions.scroll_to_element(shop).perform()
actions.scroll_by_amount(0,200).perform()

# click shop
shop.send_keys(Keys.ENTER)

actions.scroll_by_amount(0,600).perform()

# select shoe and click
shoe = driver.find_element(By.XPATH,'//div[text()="Nike Air Max Nova"]').click()
driver.switch_to.window(driver.window_handles[-1])
sleep(2)

# select size
size = driver.find_element(By.XPATH, "//label[contains(text(),'UK 4.5')]").click()

# click Add to bag
driver.find_element(By.XPATH,'//button[text()="Add to Bag"]').click()
sleep(2)

driver.quit()
