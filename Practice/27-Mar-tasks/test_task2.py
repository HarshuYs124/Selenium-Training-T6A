from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.support.ui import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)

def test_click():
    driver.find_element(By.XPATH, "//a[@href='/apparel-shoes']").click()

def test_dropdown1():
    dropdown = driver.find_element(By.ID, 'products-orderby')
    option = Select(dropdown)
    option.select_by_visible_text('Name: Z to A')

def test_dropdown2():
    dropdown = driver.find_element(By.ID, 'products-pagesize')
    option = Select(dropdown)
    option.select_by_visible_text('12')

def test_dropdown3():
    dropdown = driver.find_element(By.ID, 'products-viewmode')
    option = Select(dropdown)
    option.select_by_visible_text('List')
