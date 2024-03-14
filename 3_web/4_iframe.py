from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
url = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio"
browser.get(url)

browser.switch_to.frame('iframeResult')

elem = browser.find_element(By.XPATH, '//*[@id="html"]')    # 성공

elem.click()
print("클릭 명령 전달")

browser.switch_to.default_content()     # 상위로 빠져 나옴
elem = browser.find_element(By.XPATH, '//*[@id="html"]')    # 실패

elem.click()

time.sleep(5)
