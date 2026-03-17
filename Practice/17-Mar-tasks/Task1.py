from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")
driver.maximize_window()

rem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class = 'b3wTlE']"))).click()
txt = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//input[@class = "nw1UBF v1zwn25"]'))).send_keys("Mobiles")

ser = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@class = "XFwMiH"]'))).click()

pho = WebDriverWait(driver, 10).until(EC.presence_of_element_located(((By.XPATH, "(//div[@class = 'RG5Slk'])[5]"))))
print("Your Phone is:",pho.text)


driver.quit()
