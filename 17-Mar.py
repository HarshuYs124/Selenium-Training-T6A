from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
# from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# #EC means expected conditions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.find_element(By.XPATH, "//button[text()='Start']").click()
wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='finish'] ")))
text = driver.find_element(By.XPATH, "//div[@id='finish']").text
print(text)


#another example
driver.get("https://www.decathlon.in/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//a[@href="https://www.decathlon.in/shop/Winter-Collection"]').click()
wait=WebDriverWait(driver,10)

