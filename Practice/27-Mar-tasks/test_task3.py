from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()
driver.implicitly_wait(100)

def test_launch():
    driver.get("https://demowebshop.tricentis.com/")

def test_scroll_to_element():
    ele = driver.find_element(By.XPATH, '//li[@class="facebook"]')
    actions = ActionChains(driver)
    actions.scroll_to_element(ele).perform()

def test_new_page():
    driver.find_element(By.XPATH, '//li[@class="facebook"]//a').click()

def test_switch_window():
    driver.switch_to.window(driver.window_handles[1])

def test_email():
    driver.find_element(By.XPATH, "//input[@id='_r_1e_']").send_keys("harshita@gmail.com")

def test_password():
    driver.find_element(By.XPATH, "//input[@id='_r_1i_']").send_keys("1234567")

def test_login():
    driver.find_element(By.XPATH, "//div[@aria-label='Log in to Facebook']").click()

def test_quit():
    driver.quit()

