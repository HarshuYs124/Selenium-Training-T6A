from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_argument('--headless')

driver = Chrome(options=o)

driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.ID,"twotabsearchtextbox").send_keys("watch")
driver.find_element(By.ID,"nav-search-submit-button").click()
#
# lin=driver.find_elements(By.TAG_NAME,"img")
# print(len(lin))
products = driver.find_elements(By.XPATH, "//img[@class='s-image']")

print(len(products))
products[5].click()

driver.quit()