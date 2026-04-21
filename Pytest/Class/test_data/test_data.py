# from selenium.webdriver.common.by import By
# from selenium.webdriver import Chrome, ChromeOptions
# import pytest
# from sheet02 import get_test_data
#
#
# @pytest.fixture
# def setup():
#     o = ChromeOptions()
#     o.add_experimental_option("detach", True)
#     driver = Chrome(options=o)
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#
#
# @pytest.mark.parametrize("user,passwd", get_test_data())
# def test_login(setup, user, passwd):
#     setup.get("https://www.saucedemo.com/")
#     setup.maximize_window()
#
#     setup.find_element(By.ID, "user-name").send_keys(user)
#     setup.find_element(By.ID, "password").send_keys(passwd)
#     setup.find_element(By.ID, "login-button").click()
#
#     assert setup.current_url == "https://www.saucedemo.com/inventory.html"

from selenium.webdriver.common.by import By
import pytest
from sheet02 import get_test_data


@pytest.mark.parametrize("user,passwd", get_test_data())
def test_login(setup, user, passwd):
    setup.get("https://www.saucedemo.com/")
    setup.maximize_window()

    setup.find_element(By.ID, "user-name").send_keys(user)
    setup.find_element(By.ID, "password").send_keys(passwd)
    setup.find_element(By.ID, "login-button").click()

    assert setup.current_url == "https://www.saucedemo.com/inventory.html"