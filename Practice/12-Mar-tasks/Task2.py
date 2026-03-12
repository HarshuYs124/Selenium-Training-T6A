from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.wikipedia.com")
print(driver.current_url)