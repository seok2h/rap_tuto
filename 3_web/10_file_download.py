from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory': r'C:\Users\dnswn\OneDrive\Desktop\AILab\rpa_basic'})

url = 'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download'
browser = webdriver.Chrome(options=chrome_options)

browser.get(url)

browser.switch_to.frame('iframeResult')

elem = browser.find_element(By.XPATH, '/html/body/p[2]/a')
elem.click()

time.sleep(5)
browser.quit()