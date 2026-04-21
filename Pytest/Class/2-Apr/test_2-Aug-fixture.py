# #skip test
# import pytest
# @pytest.mark.skip
# def test_in():
#     l=[1,2,3,4]
#     assert 2 in l, "Not in list"
#
# # skip if
# @pytest.mark.skipif(True, reason="not in list")
# def test_in():
#     l=[1,2,3]
#     assert 3 in l, "Not in list"
#
# # paramitrized
# @pytest.mark.parametrize('a,b', [(1,2),(2,3)])
# def test_add(a,b):
#     print(a+b)
# import pytest
#
#
# @pytest.fixture
# def greet():
#     print("hello")
#     yield
#     print("bye")
#
# def test_morning(greet):
#     print('Good Morning !')
#
# def test_evening():
#     print('Good Evening !')
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from selenium import webdriver

@pytest.fixture(scope='class')
def setup():
    driver = webdriver.Chrome()
    driver.get("https://demowebshop.tricentis.com/register")
    time.sleep(3)
    yield driver
    driver.close()

class TestRegister():
    def test_gender(self, setup):
        setup.find_element(By.ID, "gender-female").click()
        time.sleep(3)

    def test_firstname(self, setup):
        setup.find_element(By.ID, 'FirstName').send_keys("Harshita")
        time.sleep(3)

    def test_lastname(self, setup):
        setup.find_element(By.ID, 'LastName').send_keys("Yadav")
        time.sleep(3)

    def test_email(self, setup):
        setup.find_element(By.ID, 'Email').send_keys("harshita@gmail.com")
        time.sleep(3)

    def test_password(self, setup):
        setup.find_element(By.ID, 'Password').send_keys("abcdefgh")
        time.sleep(3)

    def test_confirmpass(self, setup):
        setup.find_element(By.ID, 'ConfirmPassword').send_keys("abcdefgh")
        time.sleep(3)

    def test_submit(self, setup):
        setup.find_element(By.ID, "register-button").click()
