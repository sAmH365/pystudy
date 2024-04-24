from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request

import pyautogui
import pyperclip
import time

# options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument('--disable-blink-features=AutomationControlled')

options = ChromeOptions()
chrome_ver = '123.0.6312.58'

# userAgent 설정
user_agent = f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36'
options.add_argument(user_agent)

options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.set_page_load_timeout(3)
driver.maximize_window()

# 사이트 접속
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/')
time.sleep(2)
inputId = driver.find_element(By.CSS_SELECTOR, 'input[name=id]')
inputId.click()
pyperclip.copy('npower5377')
ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
time.sleep(2)

inputPw = driver.find_element(By.CSS_SELECTOR, 'input[name=pw]')
pyperclip.copy('3250med2@')
inputPw.click()
ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
time.sleep(2)

loginBtn = driver.find_element(By.CSS_SELECTOR, '.btn_login')
loginBtn.click()

time.sleep(1)

# 사과 검색
driver.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%82%AC%EA%B3%BC')
naverImgBtn = driver.find_elements(By.CSS_SELECTOR, 'a[role=tab]')[1]
naverImgBtn.click()
time.sleep(1)

btn = driver.find_element(By.CSS_SELECTOR, 'div[role=button]')
btn.click()
print('버튼 클릭 성공1')

# btn.click()이 제대로 안될때
# btn = driver.find_element(By.CSS_SELECTOR, 'div[role=button]') 버튼 요소 저장후
# driver.execute_script('arguments[0].click();', e) 자바스크립트 강제 실행

# 이미지 저장
imgUrl = driver.find_element(By.CSS_SELECTOR, 'img[class=_fe_image_viewer_image_fallback_target]').get_attribute('src')
print('imgurl ' + imgUrl)
urllib.request.urlretrieve(imgUrl, 'img/test2.jpg')
print('이미지 저장 완료')
