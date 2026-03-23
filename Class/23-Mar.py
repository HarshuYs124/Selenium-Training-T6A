from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
driver=Chrome(options=o)


''' Keyboard Actions '''
driver.get("https://www.amazon.com")
driver.maximize_window()
sleep(2)
ele=driver.find_element(By.ID,"twotabsearchtextbox")
ele.send_keys("shoes")
ele.send_keys(Keys.ENTER)  # ENTER is a keyboard action


''' Copy and Paste Keyboard Actions '''
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(2)
ele=driver.find_element(By.ID,'currentAddress')
ele.send_keys("60,kalwad road jhotwara jaipur")
ele.send_keys(Keys.CONTROL,'a')
ele.send_keys(Keys.CONTROL,'c')
ele2= driver.find_element(By.ID,'permanentAddress')
ele2.send_keys(Keys.CONTROL,'v')


# action chains classmethod
# -->create object
# --> store actions
# -->perform using .perform

''' Action Chains '''
driver.get("https://demoqa.com/buttons")
driver.maximize_window()
sleep(2)
ele=(driver.find_element(By.XPATH,"//button[text()='Click Me']"))
actions = ActionChains(driver)
actions.click(ele).perform()
sleep(2)

''' Double click '''
ele1=(driver.find_element(By.XPATH,"//button[text()='Double Click Me']"))
actions = ActionChains(driver)
actions.double_click(ele1).perform()
sleep(2)

ele2= driver.find_element(By.XPATH,"//button[text()='Right Click Me']")
actions = ActionChains(driver)
actions.context_click(ele2).perform()


''' Scrolling '''
driver.get("https://www.amazon.in/")
driver.maximize_window()

sleep(2)
ele1 = driver.find_element(By.XPATH, "(//div[@class='a-section feed-carousel-viewport'])[1]")
action = ActionChains(driver)

# scroll to element
action.scroll_to_element(ele1).perform()
sleep(2)

#scroll by amount
action.scroll_by_amount(0,500).perform()
action.scroll_by_amount(0,500).perform() # it will perform after the previous coordinate not fron starting
ele2= driver.find_element(By.XPATH,"(//div[@class='a-section a-spacing-none feed-carousel'])[1]")
sleep(2)

#scroll from origin - points a particular point as origin
origin=ScrollOrigin.from_element(ele2)
action = ActionChains(driver)
action.scroll_from_origin(origin,0,500).perform()

''' mouse hover '''
ele= driver.find_element(By.ID,"nav-link-accountList-nav-line-1")
action=ActionChains(driver)
action.move_to_element(ele).perform()

''' click and hold '''
driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
driver.maximize_window()
sleep(3)
ele2=driver.find_element(By.XPATH,"//*[@id='password']")
ele2.send_keys("dhcbjhbs")
ele3= driver.find_element(By.XPATH,'(//img[@class="ng-star-inserted"])[1]')
action=ActionChains(driver)
action.click_and_hold(ele3).release().pause(5).perform()


''' drag and drop '''
driver.get("https://demoqa.com/droppable")
driver.maximize_window()
sleep(3)
drag = driver.find_element(By.ID,"draggable")
drop=driver.find_element(By.ID,"droppable")
action = ActionChains(driver)
action.pause(3).drag_and_drop(drag,drop).perform()


''' Multiple window handling'''
#to fetch the address of current window -->current_window_handle
#to fetch id of all the window --> window_handles
#to switch window -->switch.to.window(_)


driver.get("https://www.google.com")
driver.maximize_window()
sleep(5)

#manually open three tabs
print("before:")
print(driver.current_window_handle) # gives id of current window
print(driver.title) # gives title of current window

driver.switch_to.new_window() #switches to new window
driver.get("https://www.amazon.in")
sleep(3)
print(driver.window_handles) # gives ids for all the windows

print("after: ")
print(driver.current_window_handle)
print(driver.title)

driver.switch_to.window(driver.window_handles[0]) # switches to next window or backward through indexing
sleep(3)
driver.find_element(By.LINK_TEXT,'About').click()