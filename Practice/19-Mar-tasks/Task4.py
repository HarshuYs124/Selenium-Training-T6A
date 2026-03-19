from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

finput = driver.find_element(By.XPATH, "(//input[@type='file'])[2]")
# files = [
#     r"C:\Users\Harshita Yadav\OneDrive\Desktop\file1.txt",
#     r"C:\Users\Harshita Yadav\OneDrive\Desktop\file2.txt",
#     r"C:\Users\Harshita Yadav\OneDrive\Desktop\file3.txt"
# ]
# for f in files:
#     finput.send_keys(f)

files = r"C:\Users\Harshita Yadav\OneDrive\Desktop\file1.txt"+'\n'+r"C:\Users\Harshita Yadav\OneDrive\Desktop\file2.txt" + '\n'+ r'C:\Users\Harshita Yadav\OneDrive\Desktop\file3.txt'

driver.find_element(By.XPATH, '//input[@id="multipleFilesInput"]').send_keys(files)

driver.quit()