from selenium.webdriver import Chrome, ChromeOptions
import pytest

@pytest.fixture
def setup():
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    driver = Chrome(options=o)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()