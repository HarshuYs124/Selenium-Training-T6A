from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
# o.add_argument('--headless')
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.NAME,'field-keywords').send_keys("mobiles")
sleep(2)
driver.find_element(By.ID,'nav-search-submit-button').click()
sleep(2)
driver.find_element(By.XPATH,"(//h2/span)[1]")

# price=driver.find_element(By.XPATH,"(//span[@class='a-price-whole'])[3]")
price=driver.find_element(By.XPATH,"//span[text()='iQOO Z10x 5G (Ultramarine, 8GB RAM, 256GB Storage) | 6500 mAh Large Capacity Battery | Dimensity 7300 Processor | Military-Grade Durability']/../../../..//span[@class='a-price-whole']").text
print("price of phone is: ",price)

driver.close()
