import pytest
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o= ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--disable-notifications")
driver = Chrome(options=o)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.implicitly_wait(100)

@pytest.mark.parametrize('a,b',[('standard_user','secret_sauce'),('akshat','tated'),('standard_user','secret_sauce')])
def test_add(a,b):
    driver.find_element(By.XPATH,'//input[@id="user-name"]').send_keys(a)
    driver.find_element(By.XPATH,'//input[@id="password"]').send_keys(b)
    driver.find_element(By.XPATH,'//input[@id="login-button"]').click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', driver.refresh()
    driver.back()