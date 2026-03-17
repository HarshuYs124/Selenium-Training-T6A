# from time import sleep
# from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.common.by import By
#
#
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
#
# driver.get("https://demoqa.com/webtables")
# driver.maximize_window()
#
# # Wait so you can manually add data
# input("👉 Add data manually, then press ENTER...")
#
# # Fetch last row (your added data)
# name = driver.find_element(By.XPATH, "(//div[@role='row']//div[1])[last()]").text
# salary = driver.find_element(By.XPATH, "(//div[@role='row']//div[5])[last()]").text
#
# print(f"{name}:{salary}")
#
#

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.implicitly_wait(10)
driver.get("https://demoqa.com/webtables")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[@id = 'addNewRecordButton']").click()
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Tom")
driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Holland")
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("tom@gmail.com")
driver.find_element(By.XPATH, "//input[@id='age']").send_keys("35")
driver.find_element(By.XPATH, "//input[@id='salary']").send_keys("50000000")
driver.find_element(By.XPATH, "//input[@id='department']").send_keys("Acting")
driver.find_element(By.XPATH, "//button[@id = 'submit']").click()

salary = driver.find_element(By.XPATH, "//td[text() = 'Tom']/..//td[5]")
print("Tom's salary is:",salary.text)

driver.quit()