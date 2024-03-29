from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
url = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio"
browser.get(url)

browser.switch_to.frame('iframeResult')

elem = browser.find_element(By.XPATH, '//*[@id="html"]')    # 성공

# 선택이 안 되어 있으면 선택하기
if elem.is_selected() == False: # 라디오 버튼이 선택되어 있지 않으면
    print("선택 안 되어 있으므로 선택하기")
    elem.click() 
else:
    print("선택 되어 있으므로 아무것도 안함")

time.sleep(5)   # 5초 대기

browser.close()




