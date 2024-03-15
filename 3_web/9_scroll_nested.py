import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')
browser.maximize_window()

time.sleep(5)

elem = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[61]')

# 방법 1 : ActionChain
actions = ActionChains(browser)
actions.move_to_element(elem).perform()

# 방법 2 :
xy = elem.location_once_scrolled_into_view
print("type: ", type(xy))
print("value : ", xy)
elem.click()

time.sleep(5)
browser.quit()




















































