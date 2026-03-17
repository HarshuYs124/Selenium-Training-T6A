from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
# o.add_argument('--headless')
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.NAME,'q').send_keys("watches for women")
sleep(2)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
sleep(2)
price = driver.find_element(By.XPATH, "//a[text()='Big Dial Analog Watch  - For Women 106408499']/../../../..//div[contains(text(),'₹')]").text
print(price)

driver.close()
