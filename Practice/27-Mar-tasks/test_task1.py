from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
driver.implicitly_wait(10)

def test_gender():
    driver.find_element(By.ID, "gender-female").click()
def test_firstname():
    driver.find_element(By.ID,'FirstName').send_keys("Harshita")
def test_lastname():
    driver.find_element(By.ID, 'LastName').send_keys("Yadav")
def test_email():
    driver.find_element(By.ID, 'Email').send_keys("harshita@gmail.com")
def test_password():
    driver.find_element(By.ID, 'Password').send_keys("abcdefgh")
def test_confirmpass():
    driver.find_element(By.ID, 'ConfirmPassword').send_keys("abcdefgh")
def test_submit():
    driver.find_element(By.ID, "register-button").click()