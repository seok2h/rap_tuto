# Quiz) Selenium을 이용하여 아래 업무를 자동으로 수행하는 프로그램을 작성하시오

# 1. https://www.w3schools.com 접속 (URL은 구글에서 w3schools 검색)
# 2. 화면 중간 LEARN HTML 클릭
# 3. 상단 메뉴 중 HOW TO 클릭
# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
# 5. 입력란에 아래 값 입력
#     First Name : 나도
#     Last Name : 코딩
#     Country : Canada
#     Subject : 퀴즈 완료하였습니다. 
# 6. 5초 대기 후 Submit 버튼 클릭
# 7. 5초 대기 후 브라우저 종료

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://www.w3schools.com/'

# 브라우저 실행
browser = webdriver.Chrome()
browser.get(url)

# LEARN HTML click
browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]').click()
# HOW TO click
browser.find_element(By.XPATH, '//*[@id="subtopnav"]/a[8]').click()
# Contact Form menu click
browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[120]').click()

# first name에 '나도'입력
first_name = browser.find_element(By.XPATH, '//*[@id="fname"]')  # first name
first_name.send_keys('나도')

# last name에 '코딩' 입력
last_name = browser.find_element(By.XPATH, '//*[@id="lname"]')
last_name.send_keys('코딩')

# 국적 캐나다로 설정
option_bar = browser.find_element(By.XPATH, '//*[@id="country"]')
option_bar.click()
browser.find_element(By.XPATH, '//*[@id="country"]/option[2]').click()  # 캐나다 클릭

# text area에 "퀴즈 완료했습니다." 입력
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea').send_keys('퀴즈 완료하였습니다.')

# 버튼
submit_button = browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/a')
time.sleep(5)
submit_button.click()

time.sleep(5)
browser.quit()


