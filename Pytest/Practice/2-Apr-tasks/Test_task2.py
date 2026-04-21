"""
For smoke testing run -> pytest .\Test_task_2.py -vs -m "smoke"
For regression testing run -> pytest .\Test_task_2.py -vs -m "regression"
"""

import pytest

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_argument("--headless")
driver = Chrome(options=o)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/tables")

@pytest.mark.smoke
def test_dueAmt():
    due_amt = driver.find_element(By.XPATH, '//td[text()="Tim"]//following-sibling::td[2]').text

    assert "$50.00" == due_amt

    print(f"Due amount - {due_amt}")

@pytest.mark.smoke
def test_lastName():
    last_name = driver.find_element(By.XPATH, '//td[text()="Tim"]//preceding-sibling::td[1]').text

    assert "Conway" == last_name

    print(f"LastName - {last_name}")

@pytest.mark.regression
def test_email():
    email = driver.find_element(By.XPATH, '//td[text()="Tim"]//following-sibling::td[1]').text

    assert email == "tconway@earthlink.net"

    print(f"Email - {email}")

@pytest.mark.regression
def test_website():
    website = driver.find_element(By.XPATH, '//td[text()="Tim"]//following-sibling::td[3]').text

    assert "http://www.timconway.com" == website

    print(f"Website - {website}")




