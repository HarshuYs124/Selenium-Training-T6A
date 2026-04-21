''''saucedemo'''

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
import pytest
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

@pytest.mark.parametrize("user,passwd",[("standard_user","secret_sauce"),('performance_glitch_user','secret_sauce')])
def test_login(user,passwd):
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.ID,"user-name").send_keys(user)
    driver.find_element(By.ID,"password").send_keys(passwd)
    driver.find_element(By.ID,"login-button").click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
