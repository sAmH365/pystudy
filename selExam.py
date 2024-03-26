from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


# # 사이트 접속하기
# driver.get('https://instagram.com')
# time.sleep(2)
# e = driver.find_element(By.CLASS_NAME, '_aa4u').text

# # 인풋창에 입력
# e = driver.find_element(By.CSS_SELECTOR, 'input[name=username]')
# e.send_keys('내 아이디')
# e.send_keys(Keys.ENTER)

driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/')
time.sleep(2)
e = driver.find_element(By.CSS_SELECTOR, 'input[name=id]')
e.send_keys('npower5377')
e = driver.find_element(By.CSS_SELECTOR, 'input[name=pw]')
e.send_keys('1234')
e = driver.find_element(By.CSS_SELECTOR, '.btn_login')
e.click()

# e = driver.find_element(By.CSS_SELECTOR, 'input[name=username]').text
print(e)


