from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome,ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://amazon.in/")
