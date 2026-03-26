#iframe --> mini webpage inside a webpage
# make three webpages with second's address in first
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions


o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("file:///C:/Users/Harshita%20Yadav/OneDrive/Desktop/New%20folder%20(4)/capgemini/training/page1.html")
driver.maximize_window()
sleep(4)
driver.find_element(By.ID,"inp1").send_keys("first")
#switching by class
driver.switch_to.frame('frame1')
driver.find_element(By.ID,"inp2").send_keys("second")
#switching through index
driver.switch_to.frame(0)
driver.find_element(By.ID,"inp3").send_keys("third")


#switching to parent
driver.switch_to.parent_frame()
driver.find_element(By.ID,"inp2").clear()
driver.find_element(By.ID,"inp2").send_keys("i am back")
driver.switch_to.parent_frame()
#to clear
driver.find_element(By.ID,"inp1").clear()
driver.find_element(By.ID,"inp1").send_keys("i am back")

#switch to main page
driver.switch_to.default_content()
driver.find_element(By.ID,"inp2").send_keys("i am back")

#handling alerts

o.add_argument("--diable-notifications")
driver = Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(4)
driver.find_element(By.XPATH,"//button[text()='Simple Alert']").click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()
driver.find_element(By.XPATH,"//button[text()='Confirmation Alert']").click()
alert2= driver.switch_to.alert
alert2.dismiss()
driver.find_element(By.XPATH,"//button[text()='Prompt Alert']").click()
alert3= driver.switch_to.alert
alert3.send_keys("harshita")
alert3.accept()

#popup disable
#use this for diable (o.add_argument("--diable-notifications"))
driver.get("https://www.easemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(10)

'''calender irctc'''
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//span[@class="ng-tns-c69-9 ui-calendar"]').click()
driver.find_element(By.XPATH,'//span[@class="ui-datepicker-month ng-tns-c69-9 ng-star-inserted"]').click()
driver.find_element(By.XPATH,"//a[@class='ui-state-default ng-tns-c69-9 ng-star-inserted']").click()


'''calender demoqa'''
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID,"dateOfBirthInput").click()
driver.find_element(By.XPATH,'//select[@class="react-datepicker__month-select"]').click()
driver.find_element(By.XPATH,"//option[@value='4']").click()

driver.find_element(By.XPATH, '//select[@class="react-datepicker__year-select"]').click()
driver.find_element(By.XPATH, '//option[.="2004"]').click()

driver.find_element(By.XPATH, '//div[.="15"]').click()
