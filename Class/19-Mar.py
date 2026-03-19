from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_argument('--headless')

driver = Chrome(options=o)

driver.get("https://google.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.TAG_NAME,"a").click()

links=driver.find_elements(By.TAG_NAME,'a')
print(links)
print(len(links))
for i in links:
    print (i.text)



ele=driver.find_element(By.XPATH,'//a[@class="gb_A"]')
sleep(2)
print(ele.get_attribute('aria-label'))


'''Facebook'''
#is_enabled,  is_displayed
driver.get("https://www.facebook.com")
driver.maximize_window()
driver.implicitly_wait(10)
ele=driver.find_element(By.XPATH,'//div[@aria-label="Log in"]')
print(ele.is_displayed())
print(ele.is_enabled())



'''naukri'''
driver.get("https://www.naukri.com/")
driver.maximize_window()
driver.implicitly_wait(10)
ele = driver.find_element(By.XPATH, '//a[text()="Register"]')
print(ele.is_enabled())
print(ele.is_displayed())


'''Internet herokuapp'''

driver.get("http://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()
driver.implicitly_wait(10)

cb=driver.find_element(By.XPATH,"//input[@type='checkbox'][1]")
print("selected : ",cb.is_selected())
cb2=driver.find_element(By.XPATH,"//input[@type='checkbox'][2]")
print("selected : ",cb2.is_selected())
driver.find_element(By.XPATH,"//input[@type='checkbox'][1]").click()
cb=driver.find_element(By.XPATH,"//input[@type='checkbox'][1]")
print("selected : ",cb.is_selected())

'''Forms'''
driver = Chrome(options=o)

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.ID, 'firstName').send_keys("Harshita")
driver.find_element(By.ID, 'lastName').send_keys("Yadav")
driver.find_element(By.ID, 'userEmail').send_keys("harshita@gmail.com")
driver.find_element(By.XPATH, '//label[text()="Female"]').click()
driver.find_element(By.ID, 'userNumber').send_keys("9876543210")
driver.find_element(By.ID, 'dateOfBirthInput').click()
driver.find_element(By.XPATH, '//div[text()="19"]').click()
driver.find_element(By.ID, 'subjectsInput').send_keys("Maths")
driver.find_element(By.XPATH, '//label[text()="Reading"]').click()
driver.find_element(By.ID, 'uploadPicture').send_keys(r"C:\Users\Harshita Yadav\OneDrive\Desktop\download.webp")
driver.find_element(By.ID, 'currentAddress').send_keys("jaipur, Rajasthan")
driver.find_element(By.XPATH,'//div[@class=css-1wy0on6]').click()

state = driver.find_element(By.ID, "react-select-3-input").send_keys("Rajasthan")
driver.find_element(By.ID, 'react-select-4-input').send_keys("Jaipur")
